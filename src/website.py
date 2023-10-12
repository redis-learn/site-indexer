import hashlib
import base64
from bs4 import BeautifulSoup

'''
Describes a web site

We are not interested in the entire content of the HTML page. The CSS selector allows us considering only specific
blocks.
'''
class WebSite:
    def __init__(self, url, categories, content, text_selector, title_selector="h1"):
        self.id = base64.b64encode(bytes(url, 'utf-8')).decode()
        self.url = url
        self.checksum = hashlib.md5(content.encode('utf-8')).hexdigest()
        self.categories = categories
        self.content = content
        self.title = self._to_text(title_selector)
        self.text = self._to_text(text_selector)
        self.segments = self._extract_segments(text_selector)

    '''
    Converts the relevant (selected) content of the site into plain text
    '''
    def _to_text(self, selector):
        result = None
        soup = BeautifulSoup(self.content, "html.parser")
        html = soup.select_one(selector)

        if html:
            result = html.text

        return result

    '''
    Extracts text segments from the content
    '''
    def _extract_segments(self, main_selector, seperator="h2"):
        pre_soup = BeautifulSoup(self.content, "html.parser")
        html = str(pre_soup.select_one(main_selector))
        soup = BeautifulSoup(html, "html.parser")
        headings = soup.find_all(seperator)
        segments = {}
        for h in headings:
            text = ""
            for sibling in h.find_next_siblings():
                if sibling.name == "h2":
                    break
                text = text + sibling.text
            segments[h.text] = text
        return segments