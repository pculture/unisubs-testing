#!/usr/bin/env python
from html.video_page import VideoPage
from lettuce import *

@step('I see the embedded video')
def verify_video_embed(self):
    video_pg = VideoPage()
    assert video_pg.video_embed_present(), True
    
