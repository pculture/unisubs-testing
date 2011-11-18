import unittest
from base_test_case import BaseTestCase
from html.watch_page import WatchPage
from html.search_results_page import SearchResultsPage


class TestWatchPage(BaseTestCase):
    """
    Tests for Unisubs watch page layout and search function.
    
    """
    _SIMPLE_SEARCH_TEXT = "monkey"
    _NO_RESULTS_SEARCH_TEXT = "asd0asd9f as0d9f8asd asd0f98asd"


    def test_watch_page_simple_search(self):
        """Simple search from the Watch page.
        
        """
        watch_pg = WatchPage()
        watch_pg.open_watch_page()
        r = watch_pg.basic_search(self._SIMPLE_SEARCH_TEXT)
        self.assertTrue(r.search_has_results())
            

    def test_watch_page_no_results(self):
        """No results search from the Watch page.
        
        """
        watch_pg = WatchPage()      
        watch_pg.open_watch_page()
        results_pg = watch_pg.basic_search(self._NO_RESULTS_SEARCH_TEXT)
        self.assertTrue(results_pg.search_has_no_results())
    

if __name__ == "__main__":
    unittest.main()

    
