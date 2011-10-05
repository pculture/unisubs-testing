#!/usr/bin/env python
from search_page import SearchPage

class WatchPage(SearchPage):
    """
     Unisubs page contains common web elements found across
     all Universal Subtitles pages. Every new page class is derived from
     UnisubsPage so that every child class can have access to common web 
     elements and methods that pertain to those elements.
    """
 
 
    _URL = "videos/watch"
    _ADV_SEARCH_PULLDOWN = "form.search-form div#watch_search a#advanced_search.btn_active"
    _ADV_SEARCH_ORIG_LANG = "div.menu_item select#id_video_lang"
    _ADV_SEARCH_TRANS_LANG = "div.menu_item select#id_langs"
    
    _FEATURED_SECTION = "div#featured_videos"
    _POPULAR_SECTION = "div#popular_videos"
    _LATEST_SECTION = "div#latest_videos"



    def open_watch_page(self):
        self.open_page(self._URL)

    def advanced_search(self, search_term, orig_lang=None, trans_lang=None):
        pass

        
    

        
        



    
            
        
        
    
