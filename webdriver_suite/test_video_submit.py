from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from base_test_case import BaseTestCase
import testsetup
from html.create_page import CreatePage
from html.video_page import VideoPage
from html.shared_actions import SharedActions


class TestHomePage(BaseTestCase):
    """
    Tests for Unisubs home page basic layout and functionality.
    
    """


    def submit_and_verify_embed(self, url):
        action = SharedActions()
        action.find_and_delete_existing_video(url)
        del action        
        create_pg = CreatePage()
        create_pg.open_create_page()
        create_pg.submit_video(url)
        self.assertTrue(create_pg.submit_success())
        del create_pg
        video_pg = VideoPage()
        self.assertTrue(video_pg.video_embed_present)
        del video_pg
        

    def test_submit_blip_ogv_video(self):
        """Submit a blip .ogv video.
        
        """
        url = "http://blip.tv/file/get/Pycon-PyCon2011PythonTheSecretSauceInTheOpenCloud878.ogv"
        self.submit_and_verify_embed(url)
 
    
    def test_submit_blip_flv_video(self):
        """Submit a blip flv video for flowplayer embed test.
        
        """
        url = "http://blip.tv/file/get/Linuxconfau-LightningTalks606.flv"
        self.submit_and_verify_embed(url)
        
     
    def test_submit_dailymotion_video(self):
        """Submit a video from DailyMotion.

        """
        url = "http://www.dailymotion.com/video/xlh9h1_fim-syndicat-des-apiculteurs-de-metz-environs_news"


    def test_submit_youtube_video(self):
        """Submit a video from DailyMotion.

        """
        url = "www.youtube.com/watch?v=WqJineyEszo"
 

    def test_submit_vimeo_video(self):
        """Submit a video from Vimeo.

        """
        url = "http://vimeo.com/26487510"
        self.submit_and_verify_embed(url)
 
        

        

if __name__ == "__main__":
    unittest.main()

    
