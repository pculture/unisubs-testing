#!/usr/bin/env python
from lettuce import *


@step('the video is not in the unisubs db "(.*?)"')
def delete_video_from_unisubs(self, url):
    world.dj_admin.find_and_delete_existing_video(url)
    

@step('I submit a video "(.*?)"')
def submit_and_verify_embed(self, url):
    world.create_pg.open_create_page()
    world.create_pg.submit_video(url)
    assert world.create_pg.submit_success(), True

@step('the feed is not in the unisubs db "(.*?)"')
def delete_video_from_unisubs(step, url):
    world.dj_admin.delete_video_feed(url)
    
@step('I submit a feed "(.*?)"')     
def bulk_submit_videos_by_feed(self, url):    
    world.create_pg.open_create_page()
    world.create_pg.submit_feed_url(url)

@step('I see the submit successful message')
def create_page_successful_message(step):
    assert world.create_pg.multi_submit_successful(), True

@step('I submit a youtube user feed "(.*?)"')
def bulk_submit_videos_from_youtube_user(self, youtube_user):     
    world.create_pg.open_create_page()
    world.create_pg.submit_youtube_users_videos(youtube_user, save=True)


@step('I submit a youtube user page "(.*?)"')
def bulk_submit_videos_from_youtube_page(self, url):      
    world.create_pg.open_create_page()
    world.create_pg.submit_youtube_user_page(url, save=True)
    
