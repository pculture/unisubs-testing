#!/usr/bin/env python
from page import Page

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

    _SITE_LOGIN_USER_ID = "input#id_username"
    _SITE_LOGIN_USER_PW = "input#id_password"
    _SITE_LOGIN_SUBMIT  = "form button[value=login]"




    def open_universal_subtitles(self):
        self.browser.get(self.base_url)
   
    def log_out(self):
        if self.is_element_present(self._LOGIN):
            print "already logged out"
        else:
            logout_url = self.get_attr(self._LOGOUT, 'href')
            self.open_page(logout_url)

    def log_in(self,username,password):
        if self.is_element_present(self._USER_MENU):
            self.log_out()
        
        self.click_by_css(self._LOGIN, self._SITE_LOGIN_USER_ID)
        self.type_by_css(self._SITE_LOGIN_USER_ID, self.username)
        self.type_by_css(self._SITE_LOGIN_USER_PW, self.password)
        self.click_by_css(self._SITE_LOGIN_SUBMIT, self._USER_MENU)

        

    def click_feeback(self):
        self.click_by_css(self._FEEDBACK_BUTTON)


