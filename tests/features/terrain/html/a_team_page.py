#!/usr/bin/env python
import time

from unisubs_page import UnisubsPage

class ATeamPage(UnisubsPage):
    """Defines the actions for specific teams pages like 'unisubs test team' (default) or others. 
    """

    _JOIN_TEAM = "div.join a#join"
    _APPLY_TEAM = "div.join p a#apply"
    _APPLY_BUTTON = "Apply to Join"
    _JOIN_LOGGED_IN = "Join this team now!"
    _JOIN_NOT_LOGGED_IN = "Sign in to Join Team"
    _APPLICATION = "div#apply-modal"
    _APPLICATION_TEXT = "div#apply-modal div.form textarea"
    _SUBMIT_APPLICATION = "div#apply-modal 


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
        button = self._JOIN_TEAM
        join_button = self.get_text_by_css(button)
        if self.logged_in(): 
           assert join_button == self._JOIN_LOGGED_IN
        else:
           assert join_button == self._JOIN_NOT_LOGGED_IN

    def apply_exists(self):
        button = self._APPLY_TEAM
        join_button = self.get_text_by_css(button)
        if self.logged_in(): 
           assert join_button == self._APPLY_BUTTON
        else:
           assert join_button == self._JOIN_NOT_LOGGED_IN

    def application_displayed(self):
        assert(self.is_element_present(self._APPLICATION)

    def submit_application(self, text):
        self.application_displayed()
        self.type_by_css(self._APPLICATION_TEXT, text)
        self.click_by_css(self._SUBMIT_APPLICATION)

    def join_team(self):
        self.click_by_css(self._JOIN_TEAM)
    
    def apply_team(self):
        self.click_by_css(self._APPLY_TEAM) 
