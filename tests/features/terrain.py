"""
Terrain file for Lettuce - documentation on how to use
at http://lettuce.it/reference/terrain.html

Allows you to set some generic "world" components as globals
through-out all lettuce functional tests.
"""
from lettuce import before, after
from lettuce import world
from selenium import webdriver


#@before.each_feature
#@before.each_scenario


#@before.each_step

@before.all
def setup_browser():
    world.browser = webdriver.Firefox()
    #django.conf.settings.DEBUG = True

@after.all
def teardown_browser(total):
    pass
    #world.browser.quit()
