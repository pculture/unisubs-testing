"""
Terrain file for Lettuce - documentation on how to use
at http://lettuce.it/reference/terrain.html

Allows you to set some generic "world" components as globals
through-out all lettuce functional tests.
"""
from lettuce import before, after
from lettuce import world
from selenium import webdriver
import testsetup
from html.watch_page import WatchPage
from html.video_page import VideoPage
from html.create_page import CreatePage
from html.search_page import SearchPage
from html.search_results_page import SearchResultsPage
from html.django_admin_page import DjangoAdminPage
from html.offsite_page import OffsitePage
from html.js_test_page import JsTestPage
from html.teams_page import TeamsPage
from html.a_team_page import ATeamPage
from html.unisubs_page import UnisubsPage

#@before.each_feature
#@before.each_scenario


#@before.each_step

@before.all
def setup_browser():
    world.browser = webdriver.Firefox()
    #django.conf.settings.DEBUG = True

@before.all
def instantiate_pages():
    world.watch_pg = WatchPage()
    world.video_pg = VideoPage()
    world.create_pg = CreatePage()
    world.search_pg = SearchPage()
    world.dj_admin = DjangoAdminPage()
    world.results_pg = SearchResultsPage()
    world.offsite_pg = OffsitePage()
    world.javascript_pg = JsTestPage()
    world.a_team_pg = ATeamPage()
    world.teams_pg = TeamsPage()
    world.unisubs_pg = UnisubsPage()

@after.all
def teardown_browser(total):
    pass
    #world.browser.quit()
