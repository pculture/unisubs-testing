#!/usr/bin/env python
from lettuce import *
from html.watch_page import WatchPage

@step('I am on the watch page')
def open_watch_page(self):
   watch_pg = WatchPage()
   watch_pg.open_watch_page()


@step('I enter a search for "(.*?)"')
def submit_a_search(self, search_term):
    watch_pg = WatchPage()
    watch_pg.basic_search(search_term)
 
    
