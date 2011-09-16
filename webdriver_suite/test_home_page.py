from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from base_test_case import BaseTestCase
import testsetup
from unisubs_page import UnisubsPage


class TestHomePage(BaseTestCase):
    """
    Tests for Unisubs home page basic layout and functionality.
    
    """

    def test_feedback_tab(self):
        """Click feedback tab and verify tenderapp page displayed.

        For https://unisubs.sifterapp.com/projects/12298/issues/426162/comments
        """
        unisubs_page_obj = UnisubsPage(testsetup)
        unisubs_page_obj.open_universal_subtitles()
        unisubs_page_obj.log_out()
        unisubs_page_obj.click_feedback()
        loc  = unisubs_page_obj.browser.current_url
        self.assertEqual(loc, "https://universalsubtitles.tenderapp.com/")

    def test_site_login(self):
        """Log in to site with admin site account.
        
        """
        unisubs_page_obj = UnisubsPage(testsetup)
        unisubs_page_obj.open_universal_subtitles()
        unisubs_page_obj.log_in(testsetup.admin_user,testsetup.admin_pass)
        

        

if __name__ == "__main__":
    unittest.main()

    
