"""
offsite.py
    Defines actions that don't take place directly on the universalsubtitles website or widget
"""
from selenium import selenium
import unittest
import time
import mslib
import testvars
import widget


def TwitterAuth(self,sel,user,passw):
    """
    Description: Perform twitter account sign-in once window
                 has been launced via website or widget.
    Requires: valid username and password
    """
    print "twitter auth: "+ user+":"
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"username_or_email")
    sel.type("username_or_email", user)
    sel.type("session[password]", passw)
    sel.click("allow")



def OpenIdAuth(self,sel,user,passw):
    """
    Description: Perform open id [from http://myopenid.com ]account sign-in once window
                 has been launced via website or widget.
    Requires: valid username and password
    """
    print "open id auth: "+ user
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"openid_url")
    sel.type("css=.openid", testvars.openiduser)
    sel.click("css=.open-id")
    mslib.wait_for_element_present(self,sel,"signin_button")
    sel.type("password", testvars.passw)
    sel.click("signin_button")
    

def GmailAuth(self,sel,user,passw):
    """
    Description: Perform gmail account sign-in once window
                 has been launced via website or widget.
    Requires: valid username and password
    """
    sel.select_pop_up("null")
    print "gmail auth: "+ user
    mslib.wait_for_element_present(self,sel,"signIn")
    sel.type("Email", user)
    sel.type("Passwd", passw)
    sel.click("signIn")

def start_youtube_widget_null(self,sel):
    """
    Description: Opens the widet for subtitling a YouTube video against
                 dev.universalsubtitles.org in the null sandbox.

                 Test site http://pculture.org/mirosubs_tests/dev-widget-null.html, has
                 multiple embedded widgets.

                 After running this, user should be in step 1 or edit dialog of widget.
                 
                 See http://s3.staging.universalsubtitles.org/embed00081.js for embed
                 code documentation.
            
    """
    sel.open("http://pculture.org/mirosubs_tests/staging-widget-null.html")
    #left column is the youtube video
    mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabText")
    sel.click_at("css=.left_column span.mirosubs-tabText","")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
    sel.click_at(testvars.WebsiteUI["AddSubtitles_menuitem"], "")
    widget.close_howto_video(self,sel)
        
def start_ogg_widget_null(self,sel):
    """
    Description: Opens the widet for subtitling an ogg video against
                 dev.universalsubtitles.org in the null sandbox.

                 Test site http://pculture.org/mirosubs_tests/dev-widget-null.html, has
                 multiple embedded widgets.
                 
                 After running this, user should be in step 1 or edit dialog of widget.
                 
                 See http://s3.staging.universalsubtitles.org/embed00081.js for embed
                 code documentation.
    """
    sel.open("http://pculture.org/mirosubs_tests/staging-widget-null.html")
    #right column is the .ogg video
    mslib.wait_for_element_present(self,sel,"css=.right_column span.mirosubs-tabText")
    sel.click_at("css=.right_column span.mirosubs-tabText","")
    handle_warning_popup(self,sel)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
    sel.click_at(testvars.WebsiteUI["AddSubtitles_menuitem"], "")
    widget.close_howto_video(self,sel)

def handle_warning_popup(self,sel):
    """
    Description: Closes the warning pop-up for offsite widgets

    """
    sel.select_pop_up("null")
    if sel.is_element_present("css=.mirosubs-warning"):
        sel.click("link=Continue")
        for i in range(60):
            try:
                if not sel.is_element_present("css=.mirosubs-warning"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    sel.select_window("null")

        
    
