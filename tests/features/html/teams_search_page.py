#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class TeamSearchPage(UnisubsPage):

    _VIDEO = "div.view ul.videos li h3 a"
    """
     A team search performs a search against a particular team for a logged in team member.  

    The search term returns results that match the video title. 
    """
 
    _URL = "/teams/ted?q=%s"
    

    def open_search_page(self):
        self.open_page(self._URL)
    
    def team_search(self, search_term):
        """open the url with the team and search term.  

        This should be updated to not use a specific team.
        """
        search_url = self._URL % search_term
        self.open_page(search_url)
        time.sleep(1)

    def click_first_search_result(self):
        self.click_by_css(self._VIDEO)

