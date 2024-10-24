from WebScraper.crawler import WebCrawler
from WebScraper.extractor import DataExtractor

class WebScraperClient:
    def __init__(self):
        self.crawler = WebCrawler()
        self.extractor = DataExtractor()

    def scrape(self, url, instructions):
        raw_data = self.crawler.crawl(url)
        structured_data = self.extractor.extract(raw_data, instructions)
        return structured_data
