#!/usr/bin/env python
from search_page import SearchPage


class SearchResultsPage(SearchPage):
    """
     Unisubs page contains common web elements found across
     all Universal Subtitles pages. Every new page class is derived from
     UnisubsPage so that every child class can have access to common web 
     elements and methods that pertain to those elements.
    """


    _PAGE_HEADING = "h2.search-header"
    _NO_RESULTS = "div#main_col ul.video_list h3"
    _SEARCHING_INDICATOR = "div div img"
    _SORT_HEADING = "div#sidebar h2"
    _LANGUAGES_SORT = "div#sidebar ul li a[value=languages_count]"
    _VIEWS_TODAY_SORT = "div#sidebar ul li a[value=today_views]"
    _VIEWS_WEEK_SORT = "div#sidebar ul li a[value=week_views]"
    _VIEWS_MONTH_SORT = "div#sidebar ul li a[value=month_views]"
    _VIEWS_TOTAL_SORT = "div#sidebar ul li a[value=total_views]"

    _ORIG_LANG_RESULTS_COUNT = "div#sidebar ul li:nth-child(%s) > a span"


   
    def search_has_no_results(self):
        self.wait_for_element_not_present(self._SEARCHING_INDICATOR)
        if self.is_text_present(self._NO_RESULTS, "No video found"):
            return True
        else:
            return False
        
    def search_has_results(self):
        self.wait_for_element_not_present(self._SEARCHING_INDICATOR)
        lang = self.get_text_by_css(self._ORIG_LANG_RESULTS_COUNT % '5')
        num_matches = self.nums_regex.match(lang)
        num_langs = int(num_matches.group(2))
        if num_langs > 0:
            return True
        

    def sort_results(self, sort_by):
        pass

    def filter_original_languages(self, lang_code):
        pass

    def filter_translated_languages(self, lang_code):
        pass


    
    
        
        



    
            
        
        
    
