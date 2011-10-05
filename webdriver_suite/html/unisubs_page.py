#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Support
#
# The Initial Developer of the Original Code is
# Mozilla
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

from html_fragment import HtmlFragment

class UnisubsPage(HtmlFragment):
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

    _DJANGO_LOGIN_USER_ID = "input#id_username"
    _DJANGO_LOGIN_USER_PW = "input#id_password"
    _DJANGO_LOGIN_SUBMIT = "form#login-form div.submit-row input"
    _DJANGO_ADMIN_LOGOUT = "/admin/logout"


    @property
    def is_the_current_page(self):
        page_title = self.browser.title()
        if re.search(self._page_title, page_title) is None:
            self.record_error()
            try:
                raise Exception("Expected page title to be: '" + self._page_title + "' but it was: '" + page_title + "'")
            except Exception:
                raise Exception('Expected page title does not match actual page title.')
        else:
            return True

    def open_universal_subtitles(self):
        self.browser.get(self.base_url)
   
    def log_out(self):
        if self.is_element_present(self._LOGIN):
            print "already logged out"
        else:
            self.click_by_css(self._LOGOUT, self._LOGIN)

    def log_in(self,username,password):
        if self.is_element_present(self._USER_MENU):
            self.logout
        
        self.click_by_css(self._LOGIN, self._SITE_LOGIN_USER_ID)
        self.type_by_css(self._SITE_LOGIN_USER_ID, self.username)
        self.type_by_css(self._SITE_LOGIN_USER_PW, self.password)
        self.click_by_css(self._SITE_LOGIN_SUBMIT, self._USER_MENU)


    def django_admin_login(self):
        if self.is_element_present(self._DJANGO_LOGIN_USER_ID):
            self.click_by_css(self._DJANGO_LOGIN, self._DJANGO_LOGIN_USER_ID)
            self.type_by_css(self._DJANGO_LOGIN_USER_ID, self.username)
            self.type_by_css(self._DJANGO_LOGIN_USER_PW, self.password)
            self.click_by_css(self._DJANGO_LOGIN_SUBMIT)
            
    def django_admin_logout(self):
        self.open(self._DJANGO_ADMIN_LOGOUT)
        

    def click_feeback(self):
        self.click_by_css(self._FEEDBACK_BUTTON)



    
            
        
        
    
