#!/usr/bin/env python
from lettuce import *
from html.search_results_page import SearchResultsPage


@step('search results (are|are not) displayed')
def search_results_displayed(self, expected_result):
    results_pg = SearchResultsPage()
    if expected_result == 'are':
        assert results_pg.search_has_results()
    elif expected_result == 'are not':
        assert results_pg.search_has_no_results()
    else:
        assert False

@step('the search term is displayed for the "(.*?)"')
def search_text_displayed(self, search):
    results_pg = SearchResultsPage()
    assert results_pg.page_heading_contains_search_term(search), True    
    
