import json
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from core.settings import MODELTRANSLATION_LANGUAGES

try:
    import lxml

    PARSER = "lxml"
except (ImportError, Exception) as e:
    print(e)
    PARSER = "html.parser"


def update_response_html(content, base_url):
    if "<a" not in content and "<img" not in content:
        return content
    soup = BeautifulSoup(content, PARSER)
    for tag in soup.find_all(["img", "a"]):
        if tag.name == "img" and tag.get("src"):
            tag["src"] = urljoin(base_url, tag["src"])
        elif tag.name == "a" and tag.get("href"):
            tag["href"] = urljoin(base_url, tag["href"])
    return str(soup)


class UpdateDescriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_regex = re.compile(r"http://\d+\.\d+\.\d+\.\d+(:\d+)?/")

    def __call__(self, request):
        if not request.path.startswith("/api"):
            return self.get_response(request)

        response = self.get_response(request)
        content_type = response.get("Content-Type", "")

        if "application/json" in content_type:
            try:
                data = json.loads(response.content)
            except Exception:
                return response

            base_url = request.build_absolute_uri("/")

            if "localhost" in base_url or self.ip_regex.match(base_url):
                base_url = base_url.replace("https://", "http://")
            else:
                base_url = base_url.replace("http://", "https://")

            def recursive_update(item):
                if isinstance(item, dict):
                    for field in ["description", "content"]:
                        keys = [field] + [f"{field}_{lang}" for lang in MODELTRANSLATION_LANGUAGES]
                        for key in keys:
                            if key in item and isinstance(item[key], str) and item[key].strip():
                                item[key] = update_response_html(item[key], base_url)
                    for value in item.values():
                        recursive_update(value)
                elif isinstance(item, list):
                    for elem in item:
                        recursive_update(elem)

            recursive_update(data)
            response.content = json.dumps(data)
        return response
