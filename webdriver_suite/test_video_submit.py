from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from base_test_case import BaseTestCase
import testsetup
from html.create_page import CreatePage
from html.shared_actions import SharedActions


class TestHomePage(BaseTestCase):
    """
    Tests for Unisubs home page basic layout and functionality.
    
    """


    def test_submit_blip_ogv_video(self):
        """Submit a blip .ogv video
        
        """
        url = "http://blip.tv/file/get/Pycon-PyCon2011PythonTheSecretSauceInTheOpenCloud878.ogv"
        
        action = SharedActions()
        action.find_and_delete_existing_video(url)
        del action        
        create_pg = CreatePage()
        create_pg.open_create_page()
        create_pg.submit_video(url)
        self.assertTrue(create_pg.submit_success())
     
       
               

if __name__ == "__main__":
    unittest.main()

    
