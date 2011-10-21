import unittest
from urlparse import urlsplit
from base_test_case import BaseTestCase
from html.create_page import CreatePage
from html.video_page import VideoPage
from html.django_admin_page import DjangoAdminPage

class TestHomePage(BaseTestCase):
    """
    Tests for Unisubs home page basic layout and functionality.
    
    """


    def submit_and_verify_embed(self, video_url):
        dj_admin = DjangoAdminPage() 
        dj_admin.find_and_delete_existing_video(video_url)       
        create_pg = CreatePage()
        create_pg.open_create_page()
        create_pg.submit_video(video_url)
        video_pg = create_pg.submit_success()
        self.assertTrue(video_pg.video_embed_present)
        

    def bulk_submit_videos_by_feed(self, url):
        dj_admin = DjangoAdminPage()
        dj_admin.delete_video_feed(url)       
        create_pg = CreatePage()
        create_pg.open_create_page()
        create_pg.submit_feed_url(url)
        self.assertTrue(create_pg.multi_submit_successful)

    def bulk_submit_videos_from_youtube_user(self, youtube_user):
        feedurl =  "https://gdata.youtube.com/feeds/api/users/%s/uploads" % youtube_user
        dj_admin = DjangoAdminPage()
        dj_admin.delete_video_feed(feedurl)       
        create_pg = CreatePage()
        create_pg.open_create_page()
        create_pg.submit_youtube_users_videos(feedurl, save=True)
        self.assertTrue(create_pg.multi_submit_successful)

    def bulk_submit_videos_from_youtube_page(self, youtube_page_url):
        youtube_user = urlsplit(youtube_page_url).path.split('/')[-1]
        feedurl =  "https://gdata.youtube.com/feeds/api/users/%s/uploads" % youtube_user
        dj_admin = DjangoAdminPage()
        dj_admin.delete_video_feed(feedurl)       
        create_pg = CreatePage()
        create_pg.open_create_page()
        create_pg.submit_youtube_user_page(feedurl, save=True)
        self.assertTrue(create_pg.multi_submit_successful)
        

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
        self.submit_and_verify_embed(url)


    def test_submit_youtube_video(self):
        """Submit a video from DailyMotion.

        """
        url = "http://www.youtube.com/watch?v=WqJineyEszo"
        self.submit_and_verify_embed(url)
 

    def test_submit_vimeo_video(self):
        """Submit a video from Vimeo.

        """
        feed_url = "http://vimeo.com/26487510"
        self.submit_and_verify_embed(feed_url)

    def test_bulk_submit_vimeo_feed(self):
        """Submit a feed from Vimeo.

        """
        feed_url = "http://vimeo.com/jeroenhouben/videos/rss"
        self.bulk_submit_videos_by_feed(feed_url)

    def test_bulk_submit_dailymotion_feed(self):
        """Submit a feed from Dailymotion.

        """
        feed_url = "http://www.dailymotion.com/rss/user/WildFilmsIndia/1"
        self.bulk_submit_videos_by_feed(feed_url)

    def test_bulk_submit_blip_feed(self):
        """Submit a feed from Blip

        """
        feed_url = "http://blip.tv/weird-america/rss/flash"
        self.bulk_submit_videos_by_feed(feed_url)
        
    def test_bulk_submit_blip_video_with_rss_skin_feed(self):
        """Submit a video from Blip with skin=rss to pretend to be feed.

        """
        feed_url = "http://blip.tv/cord-cutters/cord-cutters-sync-mobile-media-with-miro-4-5280931?skin=RSS"
        self.bulk_submit_videos_by_feed(feed_url)
        
    def test_bulk_submit_youtube_feed(self):
        """Submit a feed from YouTube.

        """
        feed_url = "http://gdata.youtube.com/feeds/api/users/katyperrymusic/uploads"
        self.bulk_submit_videos_by_feed(feed_url)

    def test_bulk_submit_youtube_page(self):
        """Submit a YouTube User page.

        """
        url = "http://www.youtube.com/user/SeveFanClub"
        self.bulk_submit_videos_from_youtube_page(url)

    def test_bulk_submit_youtube_user(self):
        """Submit a YouTube User name

        """
        youtube_user = "croatiadivers"
        self.bulk_submit_videos_from_youtube_user(youtube_user)            

    def test_bulk_submit_large_dailymotion_feed(self):
        """Submit a very large DailyMotion Feed.

        """
        feed_url = "http://www.dailymotion.com/rss/user/LocalNews-GrabNetworks/1"
        self.bulk_submit_videos_by_feed(feed_url)

if __name__ == "__main__":
    unittest.main()

    
