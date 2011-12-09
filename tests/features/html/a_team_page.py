#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class ATeamPage(UnisubsPage):
    """Defines the actions for specific teams pages like 'unisubs test team' (default) or others. 
    """

    _JOIN = "a.button"
    _JOIN_LOGGED_IN = "Join this team now!"
    _JOIN_NOT_LOGGED_IN = "Sign in to Join Team"

#   DEFAULT TEST TEAMS BY TYPE    
    _DEFAULT_TEAMS = {"open": "unisubs-test-team",
                   "private": "arthur-top-secret",
                   "application-only": "by-application",
                   }

    def _team_stub(self, team_type):
        if team_type == None:
            team_type = "open"
        if team_type in self._DEFAULT_TEAMS.iterkeys():
            team_url = "/teams/%s" % self._DEFAULT_TEAMS[team_type]
        else:
            team_stub = team_type.replace(' ', '-')
            team_url = "/teams/%s" %team_stub
        return team_url
    

    def open_a_team_page(self, team_type=None):
        team_url = self._team_stub(team_type)        
        print "opening team page: %s" % team_url
        self.open_page(team_url)

    def is_member(self, team_type):
        team_url = self._team_stub(team_type)
        print team_url
        current_teams = self.current_teams()
        for team in current_teams:
            if team_url in team:
                return True
                break
        
    
    def team_search(self, team):
        pass

    def join_exists(self):
        join_button = self.get_text_by_css(self._JOIN)
        if self.logged_in(): 
           assert join_button == self._JOIN_LOGGED_IN
        else:
           assert join_button == self._JOIN_NOT_LOGGED_IN

    def click_join(self):
        self.click_by_css(self._JOIN)
    
