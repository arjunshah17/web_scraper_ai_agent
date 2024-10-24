from WebScraper.client import WebScraperClient

if __name__ == "__main__":
    client = WebScraperClient()
    instructions = "Find information about product features and customer FAQs."
    documents = client.scrape("https://example.com", instructions)
    print(documents)
