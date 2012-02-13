#!/usr/bin/env python

from lettuce import *
from nose.tools import assert_true


@step('I am on the site "(.*?)"')
def open_site(self, site):
    world.offsite_pg.open_page(site)

@step('I start playback on the "(.*?)" embedded video')
def start_video_playback(self, position):
    world.offsite_pg.start_playback(str(position))

@step('I see the subtitles for the "(.*?)" embedded video')
def subtitles_are_displayed(self, position):
    world.offsite_pg.pause_playback_when_subs_appear(int(position))

@step('the subititles are correctly positioned on the video')
def verify_subtitle_placement(self):
    assert_true(world.offsite_pg.displays_subs_in_correct_position())
