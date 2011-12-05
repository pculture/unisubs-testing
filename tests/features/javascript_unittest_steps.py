#!/usr/bin/env python
from lettuce import *

@step('I am on the javascript test page')
def open_js_page(self):
    world.javascript_pg.open() 

@step('When I start the tests')
def start_tests(self):
    world.javascript_pg.click_start()
    
@step('Then they complete with no failures')
def check_results(self):
    assert(0 == world.javascript_pg.num_failed_tests())
    
