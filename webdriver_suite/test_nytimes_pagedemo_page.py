from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from base_test_case import BaseTestCase
from html.offsite_page import OffsitePage


class TestNYTimesPagedemoPage(BaseTestCase):
    """
    Tests for Unisubs home page basic layout and functionality.
    
    """
    _URL = "pagedemo/nytimes_youtube_embed"
    _SUBS_WIDGET = "div.entry-content span.unisubs-widget"

    def test_nytimes_sub_playback_position(self):
        """Log in to site with admin site account.
        
        """
        
        nyt_pg = OffsitePage()
        nyt_pg.open_page(self._URL)
        nyt_pg.scroll_page_to_video(self._SUBS_WIDGET)
        nyt_pg.pause_playback_when_subs_appear(0)
        self.assertTrue(nyt_pg.displays_subs_in_correct_position)
        

if __name__ == "__main__":
    unittest.main()

    
