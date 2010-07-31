# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars, widget


#Login as a user

def TwitterAuth(self,sel,user,passw):
    print "twitter auth: "+ user+":"
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"username_or_email")
    sel.type("username_or_email", user)
    sel.type("session[password]", passw)
    sel.click("allow")



def OpenIdAuth(self,sel,user,passw):
    print "open id auth: "+ user
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"openid_url")
    sel.type("css=.openid", testvars.openiduser)
    sel.click("css=.open-id")
    mslib.wait_for_element_present(self,sel,"signin_button")
    sel.type("password", testvars.passw)
    sel.click("signin_button")
    

def GmailAuth(self,sel,user,passw):
    sel.select_pop_up("null")
    print "gmail auth: "+ user
    mslib.wait_for_element_present(self,sel,"signIn")
    sel.type("Email", user)
    sel.type("Passwd", passw)
    sel.click("signIn")

def start_youtube_widget_null(self,sel):
        sel.open("http://pculture.org/mirosubs_tests/staging-widget-null.html")
        #left column is the youtube video
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabText")
        sel.click_at("css=.left_column span.mirosubs-tabText","")
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
        sel.click_at(testvars.WebsiteUI["AddSubtitles_menuitem"], "")
        widget.close_howto_video(self,sel)
        
def start_ogg_widget_null(self,sel):
    sel.open("http://pculture.org/mirosubs_tests/staging-widget-null.html")
    #right column is the .ogg video
    mslib.wait_for_element_present(self,sel,"css=.right_column span.mirosubs-tabText")
    sel.click_at("css=.right_column span.mirosubs-tabText","")
    handle_warning_popup(self,sel)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
    sel.click_at(testvars.WebsiteUI["AddSubtitles_menuitem"], "")
    widget.close_howto_video(self,sel)

def handle_warning_popup(self,sel):
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

        
    
