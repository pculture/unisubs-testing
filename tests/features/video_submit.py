#!/usr/bin/env python
from html.create_page import CreatePage
from html.video_page import VideoPage
from html.django_admin_page import DjangoAdminPage
from lettuce import *


@step('the video is not in the unisubs db "(.*?)"')
def delete_video_from_unisubs(step, url):
    dj_admin = DjangoAdminPage() 
    dj_admin.find_and_delete_existing_video(url)
    

@step('I submit a video "(.*?)"')
def submit_and_verify_embed(self, video_url):
    create_pg = CreatePage()
    create_pg.open_create_page()
    create_pg.submit_video(video_url)

@step('I see the embedded video')
def verify_video_embed(step):
    create_pg = CreatePage()
    video_pg = create_pg.submit_success()
    assert video_pg.video_embed_present(), True

@step('the feed is not in the unisubs db "(.*?)"')
def delete_video_from_unisubs(step, url):
    dj_admin = DjangoAdminPage()
    dj_admin.delete_video_feed(url)
    
@step('I submit a feed "(.*?)"')     
def bulk_submit_videos_by_feed(self, url):    
    create_pg = CreatePage()
    create_pg.open_create_page()
    create_pg.submit_feed_url(url)

@step('I see the submit successful message')
def create_page_successful_message(step):
    create_pg = CreatePage()
    assert create_pg.multi_submit_successful(), True

@step('I submit a youtube user feed "(.*?)"')
def bulk_submit_videos_from_youtube_user(self, youtube_user):     
    create_pg = CreatePage()
    create_pg.open_create_page()
    create_pg.submit_youtube_users_videos(youtube_user, save=True)


@step('I submit a youtube user page "(.*?)"')
def bulk_submit_videos_from_youtube_page(self, url):      
    create_pg = CreatePage()
    create_pg.open_create_page()
    create_pg.submit_youtube_user_page(url, save=True)
        

if __name__ == "__main__":
    unittest.main()

    
