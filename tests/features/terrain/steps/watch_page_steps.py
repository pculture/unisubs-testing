#!/usr/bin/env python
from lettuce import *


@step('I am on the watch page')
def open_watch_page(self):
   world.watch_pg.open_watch_page()


@step('I enter a search for "(.*?)"')
def submit_a_search(self, search_term):
    world.watch_pg.basic_search(search_term)
 
    
