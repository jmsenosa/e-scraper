import requests
import json
from playwright.sync_api import sync_playwright

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
}


class Websites:
    def __init__(self, url):
        self.url = url

    def get_website_data(self):
        response = requests.get(self.url, headers=DEFAULT_HEADERS, timeout=30)
        if response.ok:
            return response.text

        if response.status_code in (401, 403, 429):
            return self._fetch_with_browser()

        response.raise_for_status()
        return self._convert_html_to_json(response.text)

    def _fetch_with_browser(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                page = browser.new_page()
                page.goto(self.url, wait_until="domcontentloaded", timeout=60_000)
                page.wait_for_timeout(5_000)
                return page.content()
            finally:
                browser.close()

    def _convert_html_to_json(self, html):
        #convert html to json
        soup = BeautifulSoup(html, "html.parser")
        print(soup.prettify())
        return json.dumps(soup.prettify())
