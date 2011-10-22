from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from base_test_case import BaseTestCase
from html.offsite_page import OffsitePage


class TestGapminderPage(BaseTestCase):
    """NY Times pagedemo page tests.
    
    """
    _URL = "pagedemo/gapminder"
    _SUBS_WIDGET = "div.entry-content span.unisubs-widget"

    def test_gapminder_sub_playback_position(self):
        """Open NY Times page, start playback, pause when subs appear and verify correct position.
        
        """
        
        pg = OffsitePage()
        pg.open_page(self._URL)
        pg.pause_playback_when_subs_appear(0)
        self.assertTrue(pg.displays_subs_in_correct_position)
        

if __name__ == "__main__":
    unittest.main()

    
