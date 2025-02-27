import json
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from core.settings import MODELTRANSLATION_LANGUAGES


def update_description_html(content, base_url):
    """
    HTML ichidagi nisbiy URL-larni absolute URL-larga aylantiradi.
    <img> teglaridagi src va <a> teglaridagi href atributlari yangilanadi.
    """
    soup = BeautifulSoup(content, "html.parser")
    for tag in soup.find_all(["img", "a"]):
        if tag.name == "img" and tag.get("src"):
            tag["src"] = urljoin(base_url, tag["src"])
        elif tag.name == "a" and tag.get("href"):
            tag["href"] = urljoin(base_url, tag["href"])
    return str(soup)


class UpdateDescriptionMiddleware:
    """
    JSON javob ichidagi "description" va "data" maydonlari (hamda ularning til versiyalari)
    topilib, HTML kod ichidagi nisbiy URL-larni absolute URL-larga aylantiradi.
    """

    def __init__(self, get_response):
        self.get_response = get_response

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

            def recursive_update(item):
                if isinstance(item, dict):
                    for field in ["description", "data"]:
                        keys = [field] + [
                            f"{field}_{lang}" for lang in MODELTRANSLATION_LANGUAGES
                        ]
                        for key in keys:
                            if (
                                    key in item
                                    and isinstance(item[key], str)
                                    and item[key].strip()
                            ):
                                item[key] = update_description_html(item[key], base_url)
                    for value in item.values():
                        recursive_update(value)
                elif isinstance(item, list):
                    for elem in item:
                        recursive_update(elem)

            recursive_update(data)
            response.content = json.dumps(data)

        return response
