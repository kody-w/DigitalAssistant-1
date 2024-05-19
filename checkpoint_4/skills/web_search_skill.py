from skills.basic_skill import BasicSkill
import requests
from bs4 import BeautifulSoup

class WebSearchSkill(BasicSkill):
    def __init__(self):
        self.name = 'WebSearch'
        self.metadata = {
            "name": self.name,
            "description": "This skill allows the user to perform a basic search on the web and returns the first few results",
            "parameters": {
                "type": "object",
                "properties": {
                    "search_query": {
                        "type": "string",
                        "description": "The query that the user wants to search for on the web"
                    },
                },
                "required": ["search_query"]
            }
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, search_query):
        # Use the 'requests' library to send a GET request to Google
        response = requests.get(f'https://www.google.com/search?q={search_query}')

        # Parse the response text with BeautifulSoup to find the results
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', {'class': 'BNeawe UPmit AP7Wnd'})

        # Extract and return the text of the first few results
        results = [result.text for result in search_results[:5]]
        return "\n".join(results)
