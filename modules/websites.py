from pprint import pprint
import requests
import json
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import sys

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
        self.current_pagination = 1
        self.current_url = url

    def get_website_data(self):
        response = requests.get(self.url, headers=DEFAULT_HEADERS, timeout=30)
        if response.ok:
            html = response.text
        if response.status_code in (401, 403, 429):                                                                                
            html = self._fetch_with_browser()  
        response.raise_for_status()
        links = self._get_html_links(html)
        pagination = self._get_pagination(links)
        
        return pagination
    
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

    def _get_html_links(self, html):
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        return [link.get("href") for link in links]

    def _get_pagination(self, links):
        pagination = {}
        pagination_links = [] 
        pagination_end_page = None
        for link in links:
            if "page" in link:
                #if pagination is not in the list, then add it
                if link not in pagination_links:
                    pagination_links.append(link) 
    
        #complete missing pagination links
        pagination_end_page = max(pagination_links)
        last_segment = pagination_end_page.split("/")[-1]

        # Convert to integer
        page_number = int(last_segment)
        pagination_links = []
        for i in range(self.current_pagination, page_number + 1):
            pagination_links.append(f"{self.url}/page/{i}")
    
        pagination = {
            "start_page" : pagination_links[0],
            "end_page" : pagination_end_page,
            "pages" : pagination_links 
        }

        return pagination
 
 
 