import json
import logging
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from django.utils.translation import get_language_from_request

from core.settings import MODELTRANSLATION_LANGUAGES

try:
    import lxml

    PARSER = "lxml"
except ImportError:
    PARSER = "html.parser"

logger = logging.getLogger(__name__)

SPECIFIC_FIELDS = ["description", "content"]


def update_response_html(content, base_url):
    """Ensure all image and anchor links have absolute URLs."""
    if "<a" not in content and "<img" not in content:
        return content

    soup = BeautifulSoup(content, PARSER)

    for img in soup.find_all("img", src=True):
        img["src"] = urljoin(base_url, img["src"])

    for a in soup.find_all("a", href=True):
        a["href"] = urljoin(base_url, a["href"])

    return str(soup)


class UpdateDescriptionMiddleware:
    """Middleware to update empty descriptions with fallback translations and fix relative URLs."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_regex = re.compile(
            r"^(https?)://(\d{1,3}(\.\d{1,3}){3}|\[[0-9a-fA-F:]+\])"
        )

    def __call__(self, request):
        if not request.path.startswith("/api"):
            return self.get_response(request)

        response = self.get_response(request)
        content_type = response.get("Content-Type", "")

        if "application/json" in content_type:
            try:
                data = json.loads(response.content.decode("utf-8"))
            except json.JSONDecodeError as e:
                logger.error(f"JSON parse error: {e}")
                return response

            base_url = request.build_absolute_uri("/")
            if "localhost" in base_url or self.ip_regex.match(base_url):
                base_url = base_url.replace("https://", "http://")
            else:
                base_url = base_url.replace("http://", "https://")

            preferred_lang = (
                get_language_from_request(request) or MODELTRANSLATION_LANGUAGES[0]
            )
            logger.debug(f"Preferred language: {preferred_lang}")
            lang_keys = [preferred_lang] + list(MODELTRANSLATION_LANGUAGES)

            def recursive_update(item):
                if isinstance(item, dict):
                    for field in SPECIFIC_FIELDS:
                        keys = [field] + [f"{field}_{lang}" for lang in lang_keys]

                        if field in item and (
                            not item[field]
                            or item[field].strip() in ["", "<p>&nbsp;</p>"]
                        ):
                            print(f"Empty {field} found, trying alternatives")
                            for lang_key in keys[1:]:
                                if (
                                    lang_key in item
                                    and isinstance(item[lang_key], str)
                                    and item[lang_key].strip()
                                    not in ["", "<p>&nbsp;</p>"]
                                ):
                                    print(f"Updating {field} with {lang_key}")
                                    item[field] = item[lang_key]
                                    break

                        for key in keys:
                            if (
                                key in item
                                and isinstance(item[key], str)
                                and item[key].strip()
                            ):
                                item[key] = update_response_html(item[key], base_url)

                    for field in SPECIFIC_FIELDS:
                        keys = [f"{field}_{lang}" for lang in lang_keys]
                        for key in keys:
                            if key in item:
                                del item[key]

                    for value in item.values():
                        recursive_update(value)
                elif isinstance(item, list):
                    for elem in item:
                        recursive_update(elem)

            recursive_update(data)
            response.content = json.dumps(data).encode("utf-8")
            response["Content-Length"] = str(len(response.content))

        return response
