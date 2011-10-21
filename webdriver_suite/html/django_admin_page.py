#!/usr/bin/env python

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
    _VIDEOS_LINK = "th a[href*=/videos/video]"
    

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

    def delete_video_feed(self, url):
        self.open_page(self._URL)
        self.django_admin_login()
        self.page_down([self._VIDEOS_LINK])
        self.click_link_text("Video feeds")
        if self.is_text_present(url):
            self.click_link_text(url)
            self.click_link_text("Delete")
            self.click_by_css("form div input")
            self.django_admin_logout()
        
        
            
           
           
        


        
            
        
        
        
        
        
    

        
        
        

        
    

        
        



    
            
        
        
    
