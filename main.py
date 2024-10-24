from WebScraper.client import RufusClient

if __name__ == "__main__":
    client = RufusClient()
    instructions = "Find information about product features and customer FAQs."
    documents = client.scrape("https://example.com", instructions)
    print(documents)
