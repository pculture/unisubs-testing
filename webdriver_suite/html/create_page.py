#!/usr/bin/env python
from unisubs_page import UnisubsPage


class CreatePage(UnisubsPage):
    """
     Video Page contains the common elements in the video page.
    """
 
 
    _URL = "videos/create" #%s is the unique onsite video id

    _SINGLE_URL_ENTRY_BOX = "input#submit_video_field.main_video_form_field"

    _SUBMIT_BUTTON = "form.main_video_form button.green_button"
    _MULTI_SUBMIT_LINK = " div#submit_multiple_toggle a#btn_submit_multiple_toggle.toogle-create-form"
    _YOUTUBE_USER_FIELD = "div#submit_multiple_videos form#bulk_create. ul li input#id_usernames"
    _YOUTUBE_PAGE_FIELD = "div#submit_multiple_videos form#bulk_create. ul li input#id_youtube_user_url"
    _FEED_URL = "div#submit_multiple_videos form#bulk_create. ul li input#id_feed_url"
    _SAVE_OPTION = "div#submit_multiple_videos form#bulk_create ul li input#id_save_feed"
    _SUBMIT_MULTI = "div#submit_multiple_videos form#bulk_create button.green_button"

    _SUBMIT_ERROR = "ul.errorlist li"
    _MULTI_SUBMIT_SUCCESS = "h2.success"


    def open_create_page(self):
        self.open_page(self._URL)

    def submit_video(self, video_url):
        self.type_by_css(self._SINGLE_URL_ENTRY_BOX, video_url)
        self.click_by_css(self._SUBMIT_BUTTON)

    def submit_youtube_users_videos(self, youtube_usernames, save=False):
        """Submit 1 or several youtube user names.
        Type 1 or several youtube user names in hte Youtube usernames field.

        """
        
        self.click_by_css(self._MULTI_SUBMIT_LINK, self._YOUTUBE_USER_FIELD)
        for name in youtube_usernames:
            self.type_by_css(self._YOUTUBE_USER_FIELD, name)
        if save == True:
            self.click_by_css(self._SAVE_OPTION)
        self.click_by_css(self._SUBMIT_MULTI)

    def submit_youtube_user_page(self, youtube_user_url, save=False):
        """Submit videos from youtube user url.

        Enter a youtube user's page url.
        """
        
        self.click_by_css(self._MULTI_SUBMIT_LINK, self._YOUTUBE_PAGE_FIELD)
        self.type_by_css(self._YOUTUBE_PAGE_FIELD, name)
        if save == True:
            self.click_by_css(self._SAVE_OPTION)
        self.click_by_css(self._SUBMIT_MULTI)

    def submit_feed_url(self, feed_url, save=False):
        """Submit videos from a supported feed type.

        """       
        self.click_by_css(self._MULTI_SUBMIT_LINK, self._FEED_URL)
        self.type_by_css(self._FEED_URL, feed_url)
        if save == True:
            self.click_by_css(self._SAVE_OPTION)
        self.click_by_css(self._SUBMIT_MULTI)   


    def multi_submit_successful(self, expected_error=False):
        if self.is_element_present(self._MULTI_SUBMIT_SUCCESS):
            return True
        elif self.is_element_present(self._SUBMIT_ERROR):
                error_msg = self.get_text_by_css(self._SUBMIT_ERROR)
                if expected_error == True:
                    return error_msg
                else:
                    raise "Submit failed: site says %s" % error_msg
        else:
            raise "unexpected error encountered on multi video submit"

    def submit_success(self, expected_error=False):
        if expected_error == False and self.is_element_present(self._SUBMIT_ERROR):
            error_msg = self.get_text_by_css(self._SUBMIT_ERROR)
            raise "Submit failed: site says %s" % error_msg
        elif expected_error == True and self.is_element_present(self._SUBMIT_ERROR):
            return error_msg
        else:
            return True


        
            
        
        
        
        
        
    

        
        
        

        
    

        
        



    
            
        
        
    
