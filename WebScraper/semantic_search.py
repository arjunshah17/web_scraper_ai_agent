from fias import FIAS

class SemanticSearch:
    def __init__(self):
        self.model = FIAS()

    def search(self, content, query):
        # Use FIAS model for semantic search based on query
        results = self.model.semantic_search(content, query)
        return results
