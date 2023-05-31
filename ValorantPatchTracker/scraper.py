import pip._vendor.requests as requests
from bs4 import BeautifulSoup
# from utils import url_generator, PATCH_V

class Scraper():
    def __init__(self, url) -> None:
        self.url = url
        self.soup = self._soup()
        
    def _soup(self):
        """Fetches the webpage from the given URL and parses it using BeautifulSoup

        Returns:
            BeautifulSoup object: Parsed HTML of the webpage
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
    
        return soup

    
    def general_updates(self):
        """Finds GENERAL UPDATES section and returns a list of updates

        Returns:
            List[str]: List of updates in the 'GENERAL UPDATES' section.
            If 'GENERAL UPDATES' section does not exist, returns None
        """
        h2 = self.soup.find('h2', string='GENERAL UPDATES')
        updates = []
        try:
            ul = h2.find_next_sibling('ul')
        except AttributeError:
            return None
        
        for li in ul.find_all('li', recursive=False):  # Using recursive=False to not go into inner ul
            inner_ul = li.find('ul')  # Find the inner ul
            if inner_ul:  # if li contains an inner ul
                nested_li_text = '. '.join(nested_li.get_text(strip=True) for nested_li in inner_ul.find_all('li'))
                inner_ul.extract()  # remove the inner ul from the li
                li_text = li.get_text(strip=True) + '. ' + nested_li_text  # Concatenate the outer li text and the inner li text
            else:
                li_text = li.get_text(strip=True)  # Get the text of the outer li if there's no inner ul
                
            updates.append(li_text)
                
        return updates
    
#     def agent_updates(self):
#         h2 = self.soup.find('h2', string='AGENT UPDATES')
        


# url = url_generator(PATCH_V)
# scraper = Scraper(url)

# print(scraper.general_updates())