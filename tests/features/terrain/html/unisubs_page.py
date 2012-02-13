#!/usr/bin/env python
import time
from page import Page
from lettuce import world

class UnisubsPage(Page):
    """
     Unisubs page contains common web elements found across
     all Universal Subtitles pages. Every new page class is derived from
     UnisubsPage so that every child class can have access to common web 
     elements and methods that pertain to those elements.
    """
 
 
    _LOGIN = "a[href*=login]"
    _LOGOUT = "a[href*=logout]"
    _USER_MENU = "li#me_menu"    
    _CREATE_NAV = "li#nav_submit a"
    _FEEDBACK_BUTTON = ".feedback_tab"

    _USER_TEAMS = "li#me_menu  div#user_menu div#menu ul#dropdown li[id^=team] a"
    _SITE_LOGIN_USER_ID = "input#id_username"
    _SITE_LOGIN_USER_PW = "input#id_password"
    _SITE_LOGIN_SUBMIT  = "form button[value=login]"

    _ERROR_MESSAGE = "div#messages h2.error"

    USER_NAMES = {"normal": ["PollyGlott", "talks.alot"],
                 "admin": ["sub_writer", "sub.writer"],
                 "team-owning":["sub_writer", "sub.writer"],
                 }

    def error_message_present(self, message):
         if self.is_text_present(self._ERROR_MESSAGE, message): return True

    def open_universal_subtitles(self):
        self.browser.get(self.base_url)

    def logged_in(self):
        if self.is_element_present(self._USER_MENU): return True
   
    def log_out(self):
        if self.logged_in() == True:
            self.click_by_css(self._LOGOUT)

    def log_in(self, user="normal"):
        """Log in with the specified account type - default as a no-priv user.

        """
        curr_page = self.browser.current_url
        if "auth" not in curr_page and not self.logged_in():
            self.click_by_css(self._LOGIN)
        self.type_by_css(self._SITE_LOGIN_USER_ID, self.USER_NAMES[user][0])
        self.type_by_css(self._SITE_LOGIN_USER_PW, self.USER_NAMES[user][1])
        self.click_by_css(self._SITE_LOGIN_SUBMIT)
        self.wait_for_element_present(self._USER_MENU)
        time.sleep(5)

    def current_teams(self):
        """Returns the href value of any teams that use logged in user is currently a memeber.

        """
        user_teams = []
        if self.logged_in() == True:
            elements = self.browser.find_elements_by_css_selector(self._USER_TEAMS)
            for e in elements:
                user_teams.append(e.get_attribute('href'))
        return user_teams


    def click_feeback(self):
        self.click_by_css(self._FEEDBACK_BUTTON)


