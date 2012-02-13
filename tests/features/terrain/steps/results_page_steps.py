#!/usr/bin/env python
from lettuce import *
from nose.tools import assert_true

@step('search results (are|are not) displayed')
def search_results_displayed(self, expected_result):
    if expected_result == 'are':
        assert_true(world.results_pg.search_has_results())
    if expected_result == 'are not':
        assert_true(world.results_pg.search_has_no_results())

@step('the search term is displayed for the "(.*?)"')
def search_text_displayed(self, search):
    assert_true(world.results_pg.page_heading_contains_search_term(search))    
    
