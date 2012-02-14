#!/usr/bin/env python
from lettuce import *
from nose.tools import assert_true

@step('the video is not in the unisubs db "(.*?)"')
def delete_video_from_unisubs(self, url):
    world.dj_admin.find_and_delete_existing_video(url)
    

@step('I submit a (unique|duplicate) video "(.*?)"')
def submit_and_verify_embed(self, submission, url):
    if submission == 'unique': world.dj_admin.delete_video_feed(url)
    world.create_pg.open_create_page()
    world.create_pg.submit_video(url)
    assert_true(world.create_pg.submit_success())

@step('the feed is not in the unisubs db "(.*?)"')
def delete_feed_from_unisubs(self, url):
    world.dj_admin.delete_video_feed(url)
    
@step('I submit a (unique|duplicate) feed "(.*?)"')     
def bulk_submit_videos_by_feed(self, submission, url):
    if submission == 'unique':  world.dj_admin.delete_video_feed(url)
    world.create_pg.open_create_page()
    world.create_pg.submit_feed_url(url)

@step('I see the submit successful message')
def create_page_successful_message(self):
    assert_true(world.create_pg.multi_submit_successful())

@step('I submit a (unique|duplicate) youtube user feed "(.*?)"')
def bulk_submit_videos_from_youtube_user(self, submission, youtube_user):
    if submission == 'unique': world.dj_admin.delete_video_feed(youtube_user)     
    world.create_pg.open_create_page()
    world.create_pg.submit_youtube_users_videos(youtube_user, save=True)


@step('I submit a youtube user page "(.*?)"')
def bulk_submit_videos_from_youtube_page(self, url):      
    world.create_pg.open_create_page()
    world.create_pg.submit_youtube_user_page(url, save=True)
    
