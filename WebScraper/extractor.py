import pandas as pd
from WebScraper.semantic_search import SemanticSearch

class DataExtractor:
    def __init__(self):
        self.semantic_search = SemanticSearch()

    def extract(self, raw_data, instructions):
        content = raw_data['content']
        links = raw_data['links']

        relevant_content = self.semantic_search.search(content, instructions)

        # Synthesize data into structured format (JSON)
        data = {"instructions": instructions, "relevant_content": relevant_content, "links": links}
        return pd.DataFrame([data]).to_json(orient="records")
