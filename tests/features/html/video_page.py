#!/usr/bin/env python

from lettuce import *
from unisubs_page import UnisubsPage
from urlparse import urlsplit

class VideoPage(UnisubsPage):
    """
     Video Page contains the common elements in the video page.
    """
 
 
    _URL = "videos/%s" #%s is the unique onsite video id
    _VIDEO_TITLE = "div.content h2.main-title a.title-container"
    _EMBEDDED_VIDEO = "div.unisubs-widget div.unisubs-videoTab-container"
    _SUBTITLE_MENU = "a.unisubs-subtitleMeLink span.unisubs-tabTextchoose"
    _LIKE_FACEBOOK = "a.connect_widget_like_button span.liketext"
    _POST_FACEBOOK = "div.unisubs-share ul li.unisubs-facebook a"
    _POST_TWITTER = "div.unisubs-share ul li.unisubs-twitter-share a"
    _EMAIL_FRIENDS = "div.unisubs-share ul li.unisubs-friends a"
    _FOLLOW = "div#video_follow button"
    _EMBED_HELP = "div.unisubs-share h3 a.embed_options_link"
    _EMBED_CODE = "div.unisubs-share p.unisubs-embed textarea"
    _PERMALINK = "div.unisubs-share a.unisubs-permalink"

    #VIDEO SIDE SECTION
    _INFO = "ul#video-menu.left_nav li:nth-child(1) > a"
    _ADD_TRANSLATION = "li.contribute a#add_translation"
    _UPLOAD_SUBTITLES = "li.contribute a#upload-subtitles-link"

    #SUBTITLES_SIDE_SECTION
    _VIDEO_ORIGINAL = "ul#subtitles-menu li a"
    _VIDEO_LANG = ""

    #TEAM_SIDE_SECTION
    _ADD_TO_TEAM_PULLDOWN = "ul#moderation-menu.left_nav li div.sort_button div.arrow"
    _TEAM_LINK = "ul#moderation-menu.left_nav li div.sort_button ul li a[href*='%s']"
    

    #ADMIN_SIDE_SECTION
    _DEBUG_INFO = ""
    _EDIT = ""

    #TRANSCRIPTS
    _SUBTITLES = "div#transcripts-tab tr td"
    _START_TIME_DATA = "span.time-span span.data"
    _SUB_LINE = "div.sub_content"

   

    def open_video_page(self, video_id):
        self.open_page(self._URL % video_id)

    def add_translation(self):
        self.click_by_css(self._ADD_TRANSLATION)

    def upload_subtitles(self):
        self.click_by_css(self._UPLOAD_SUBTITLES)

    def open_info_page(self):
        self.click_by_css(self._INFO)

    def add_video_to_team(self, team_name):
        self.click_by_css(self._ADD_TO_TEAM_PULLDOWN)
        self.click_by_css(self._TEAM_LINK % team_name)

    def video_id(self):
        self.wait_for_element_present(self._PERMALINK)
        permalink = self.get_text_by_css(self._PERMALINK)
        url_parts = urlsplit(permalink).path
        urlfrag = url_parts.split('/')[3]
        return urlfrag

    def video_embed_present(self):
        if self.is_element_present(self._EMBEDDED_VIDEO):
            return True
    

    def page_up_to_orig_lang(self):
        self.wait_for_element_present(self._VIDEO_ORIGINAL)
        elem = self.browser.find_element_by_css_selector(self._VIDEO_ORIGINAL)
        elem.send_keys("PAGE_UP")         

          
    def open_original_lang(self):
        self.wait_for_element_present(self._VIDEO_ORIGINAL)
        elem = self.browser.find_element_by_css_selector(self._VIDEO_ORIGINAL)
        elem.send_keys("PAGE_DOWN")         
        elem.click()

    def open_translation(self, lang):
        print lang
    #    vid_url = self.browser.current_url
    #    lang_url = urlsplit(vid_url).path+lang_code
        elem = self.browser.find_element_by_partial_link_text(lang)
        elem.send_keys("PAGE_DOWN")  
        elem.click()

    def verify_sub_content(self, external_subs):
        elems = self.browser.find_elements_by_css_selector(self._SUBTITLES)
        for time, text in external_subs.iteritems():
            if self.is_text_present(text):
                print text
            else:
                print 'text: %s not found' % text
        
        
