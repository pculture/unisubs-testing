#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class MyTeam(UnisubsPage):
    """Defines the actions for specific teams pages like 'unisubs test team' (default) or others. 
    """
    _URL = "/teams/my"
    _TEAM = "ul.listing li"
    _TEAM_NAME = "h3 a"
    _LEAVE = "ul.admin_controls li a#leave"
      



    def _team_elem(self, team):
        """Given the team's text name, return the element.

        """
        teams = self.browser.find_elements_by_css_selector(self._TEAM)
        for el in teams:
            team_name = el.find_element_by_css(self._TEAM_NAME).text
            print team, team_name
            if team == team_name: return el        
        
    def open_my_teams_page(self):
        self.open_page(self._URL)

    def open_my_team(self, team=None):
        if self._URL not in self.browser.current_url:
            self.open_my_teams_page()
        if not team: 
            self.click_by_css(self._TEAM)
        else:
            team_el = self._team_elem(team)
            team = team_el.find_element_by_css_selector(self._TEAM_NAME)
            team.click()
                
    def leave_team(self, team):
        if self._URL not in self.browser.current_url:
            self.open_my_teams_page()
        team_el = self._team_elem(team)
        leave = team_el.find_element_by_css_selector(self._LEAVE)
        leave.click()
            



       
