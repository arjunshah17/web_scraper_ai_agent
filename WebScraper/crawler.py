import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from WebScraper.utils import handle_errors

class WebCrawler:
    def __init__(self):
        self.visited = set()

    @handle_errors
    def crawl(self, url):
        print(f"Crawling URL: {url}")
        content = self._get_page_content(url)
        if content:
            soup = BeautifulSoup(content, "html.parser")
            links = self._extract_links(soup, url)
            return {"content": soup.get_text(), "links": links}
        return {"content": "", "links": []}

    def _get_page_content(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None

    def _extract_links(self, soup, base_url):
        links = []
        for anchor in soup.find_all("a", href=True):
            link = urljoin(base_url, anchor['href'])
            if link not in self.visited:
                self.visited.add(link)
                links.append(link)
        return links
