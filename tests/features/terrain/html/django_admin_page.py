#!/usr/bin/env python
import time
from unisubs_page import UnisubsPage
from search_page import SearchPage


class DjangoAdminPage(UnisubsPage):
    """Sequences the require objects from multiple pages.
    """

    _URL = "admin"
    _ADMIN_LINK = "div#admin_controls a span"
    _DJANGO_LOGIN_USER_ID = "input#id_username"
    _DJANGO_LOGIN_USER_PW = "input#id_password"
    _DJANGO_LOGIN_SUBMIT = "form#login-form div.submit-row input"
    _DJANGO_ADMIN_LOGOUT = "/admin/logout"
    _ADMIN_DELETE_VID_URL = "/videos/%s/staff/delete"
    _SEARCH = "input#searchbar"
    _SEARCH_SUBMIT = "input[type=submit]"
    _SELECT_ALL = "th.action-checkbox-column input"
    _GO_BUTTON = "button[type=submit]"
    _DJANGO_CONFIRM = "input[type=submit]"
    
    _FOOTER = "div#footer"


    def open_djadmin(self):
        self.open_page(self._URL)

    def open_django_admin_page_from_site_link(self):
        if not self.is_element_present(self._ADMIN_LINK):
            raise Exception("Must be logged in as Admin User to open from Link")
        else:
            self.click_by_css(self._ADMIN_LINK)
    
    def django_admin_login(self):
        if self.is_element_present(self._DJANGO_LOGIN_USER_ID):
            self.type_by_css(self._DJANGO_LOGIN_USER_ID, self.username)
            self.type_by_css(self._DJANGO_LOGIN_USER_PW, self.password)
            self.click_by_css(self._DJANGO_LOGIN_SUBMIT)
            
    def django_admin_logout(self):
        self.open_page(self._DJANGO_ADMIN_LOGOUT)


    def delete_video(self, video_id):
        self.open_page(self._ADMIN_DELETE_VID_URL % video_id)
        self.django_admin_login()
        self.django_admin_logout()
        

    def find_and_delete_existing_video(self, url):
        """Search for a video by url and delete via django admin ui.

        url - refers to the videos original url, not local site url.
        """
        search_pg = SearchPage()
        search_pg.open_search_page()
        result_pg = search_pg.basic_search(url)
        if result_pg.search_has_results():
            vid_pg = result_pg.click_first_search_result()
            vid_id = vid_pg.video_id()
            self.delete_video(vid_id)
            self.django_admin_logout

    def delete_user_from_all_teams(self, user):
        username = self.USER_NAMES[user][0]
        self.open_page('admin/teams/teammember')
        time.sleep(3)
        self.django_admin_login()
        time.sleep(3)
        self.browser.find_element_by_id("searchbar").clear()
        self.type_by_css(self._SEARCH, username)
        self.click_by_css(self._SEARCH_SUBMIT)
        if self.is_element_present(self._SELECT_ALL):
            self.click_by_css(self._SELECT_ALL)
            self.click_by_css("option[value=delete_selected]")
            self.click_by_css(self._GO_BUTTON, self._DJANGO_CONFIRM)
            self.click_by_css(self._DJANGO_CONFIRM)
        self.django_admin_logout()
        self.open_page("/")
 

    def delete_video_feed(self, url):
        self.open_page(self._URL)
        self.django_admin_login()
        self.wait_for_element_present(self._FOOTER)
        self.page_down(self._FOOTER)
        self.click_link_text("Video feeds")
        if self.is_text_present("td", url):
            self.click_link_text(url)
            self.click_link_text("Delete")
            self.click_by_css("form div input")
        self.django_admin_logout()
        
        
            
           
           
        


        
            
        
        
        
        
        
    

        
        
        

        
    

        
        



    
            
        
        
    
