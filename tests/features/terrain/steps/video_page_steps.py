#!/usr/bin/env python
from lettuce import *
from nose.tools import assert_true

@step('I see the embedded video')
def verify_video_embed(self):
    assert_true(world.video_pg.video_embed_present())
    
