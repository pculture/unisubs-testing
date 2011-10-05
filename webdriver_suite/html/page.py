import re
from html_fragment import HtmlFragment

class Page(HtmlFragment):
    @property
    def is_the_current_page(self):
        page_title = self.browser.title()
        if re.search(self._page_title, page_title) is None:
            self.record_error()
            try:
                raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + page_title + "'")
            except Exception:
                raise Exception('Expected page title does not match actual page title.')
        else:
            return True

    def get_absolute_url(self, url):
        if url.startswith("http"):
            full_url = url
        else:
            full_url = self.base_url + url
        return full_url
   
    def open_page(self, url):
        self.browser.get(self.get_absolute_url(url))


    def go_back(self):
        self.browser.back()

    def page_down(self, elements):
        """elements are a list not a single element to try to page down.

        """
        for x in elements:
            if self.is_element_present(x):
                elem = self.browser.find_element_by_css_selector(x)
                break        
        elem.send_keys("PAGE_DOWN")
