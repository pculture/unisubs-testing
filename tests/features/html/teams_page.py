#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class TeamsPage(UnisubsPage):
    """
     Search page is the main search page stub.  Watch Page and Search Results page 
    """
 
 
    _URL = "/teams"
       


    def open_team_page(self):
        self.open_page(self._URL)
    
    def team_search(self, team):
        pass
