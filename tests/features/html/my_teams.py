#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class MyTeam(UnisubsPage):
    """Defines the actions for specific teams pages like 'unisubs test team' (default) or others. 
    """
    _URL = "/teams/my"
    _TEAM = "ul.listing li h3 a"
      

    def open_my_teams_page(self):
        self.open_page(self._URL)

    def open_my_team(self, team=None):
        if self._URL not in self.browser.current_url:
            self.open_my_teams_page()
        if not team: 
            self.click_by_css(self._TEAM)
        else:
            teams = self.browser.find_elements_by_css_selector(element)
            for el in teams:
                if team in el.text(): el.click()



       
