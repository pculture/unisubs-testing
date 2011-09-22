#!/usr/bin/env python

from unisubs_page import UnisubsPage

class SearchPage(UnisubsPage):
    """
     Search page is the main search page stub.  Watch Page and Search Results page 
    """
 
 
    _URL = "/search"
    _SEARCH = "form.search-form div#watch_search input#id_q"
    _SEARCH_UNFOCUSED = "form.search-form div#watch_search input#id_q.prefocus"
       


    def open_search_page(self):
        self.open_unisubs_page(self._URL)
    
    def basic_search(self,search_term):
        self.submit_form_text_by_css(self._SEARCH, search_term)
            
            
        
        
    
