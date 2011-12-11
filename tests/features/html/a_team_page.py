#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class ATeamPage(UnisubsPage):
    """Defines the actions for specific teams pages like 'unisubs test team' (default) or others. 
    """

    _JOIN_LEAVE = "div.controls a#%s"
    _JOIN_LOGGED_IN = "Join this team now!"
    _JOIN_NOT_LOGGED_IN = "Sign in to Join Team"

#   DEFAULT TEST TEAMS BY TYPE with [slug, owner]      
    DEFAULT_TEAMS = {"open": ["unisubs-test-team", "sub_writer"],
                   "private": ["arthur-top-secret", "arthur"],
                   "application-only": ["by-application", "maggie_s"]
                   }

    def _team_stub(self, team_type):
        if team_type == None:
            team_type = "open"
        if team_type in self.DEFAULT_TEAMS.iterkeys():
            team_url = "/teams/%s" % self.DEFAULT_TEAMS[team_type][0]
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
            if team_url in team: return True
        
    
    def team_search(self, team):
        pass

    def join_exists(self):
        button = self._JOIN_LEAVE % "join"
        join_button = self.get_text_by_css(button)
        if self.logged_in(): 
           assert join_button == self._JOIN_LOGGED_IN
        else:
           assert join_button == self._JOIN_NOT_LOGGED_IN

    def join_or_leave_team(self, action):
        button = self._JOIN_LEAVE % action
        print button
        self.click_by_css(button)
    
