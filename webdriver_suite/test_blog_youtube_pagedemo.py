from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from base_test_case import BaseTestCase
from html.offsite_page import OffsitePage


class TestBlogYouTubePage(BaseTestCase):
    """NY Times pagedemo page tests.
    
    """
    _URL = "pagedemo/blog_youtube_embed"
    _SUBS_WIDGET = "div.entry-content span.unisubs-widget"

    def test_nytimes_sub_playback_position(self):
        """Open YouTube Blog Page, start playback, pause when subs appear and verify correct position.
        
        """
        try:
            yt_pg = OffsitePage()
            yt_pg.open_page(self._URL)
            yt_pg.pause_playback_when_subs_appear(0)
            self.assertTrue(yt_pg.displays_subs_in_correct_position)
        except:
            yt_pg.record_error()
        

if __name__ == "__main__":
    unittest.main()

    
