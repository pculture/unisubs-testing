#!/usr/bin/env python
from lettuce import *

@step('I see the embedded video')
def verify_video_embed(self):
    assert world.video_pg.video_embed_present(), True
    
