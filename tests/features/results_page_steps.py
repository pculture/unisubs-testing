#!/usr/bin/env python
from lettuce import *

@step('search results (are|are not) displayed')
def search_results_displayed(self, expected_result):
    if expected_result == 'are':
        assert world.results_pg.search_has_results()
    elif expected_result == 'are not':
        assert world.results_pg.search_has_no_results()
    else:
        assert False

@step('the search term is displayed for the "(.*?)"')
def search_text_displayed(self, search):
    assert world.results_pg.page_heading_contains_search_term(search), True    
    
