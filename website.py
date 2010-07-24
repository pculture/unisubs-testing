# website.py
# SiteLogIn
# SiteLogout
# Login (for offsite login)
# start_demo
# submit_video
# start_sub_widget

from selenium import selenium

import unittest, time, re
import mslib, testvars, widget


#Login as a user

def SiteLogIn(self,sel,user,passw):
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    sel.click(testvars.WebsiteUI["Login_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("id_username", user)
    sel.type("id_password", passw)
    sel.click("//button[@value='login']")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])

def SiteLogout(self,sel):
    sel.open(testvars.MSTestVariables["Site"] +"logout/")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    

def Login(self,sel,auth_type):
    # auth_type can be either ".twitter", ".open-id", "google"
    sel.click(testvars.WebsiteUI["Login_Button"])
    mslib.wait_for_element_present(self,sel,"css=."+auth_type)
    sel.click("css=." +auth_type)
    #After login, use offsite to do auth

def start_demo(self,sel):
    mslib.wait_for_element_present(self,sel,"css=.try_link")
    sel.click("css=.try_link span:contains('Try the Demo')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    #widget.close_howto_video

def submit_video(self,sel,url):
    sel.open(testvars.MSTestVariables["Site"]+"videos/create/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])

def start_sub_widget(self,sel,skip=True):
    # Click Subtitle Me (Continue Subtitling -> Add Subtitles)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    self.failIf(sel.is_element_present(testvars.WebsiteUI["ChooseLanguage_menu"]))
    sel.click_at(testvars.WebsiteUI["SubtitleMe_menu"], "")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
    sel.click_at(testvars.WebsiteUI["AddSubtitles_menuitem"], "")
    widget.close_howto_video(self,sel,skip)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-steps")
    sel.select_frame("relative=top")

def verify_login(self,sel):
    sel.open(testvars.MSTestVariables["Site"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])
    start_demo(self,sel)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click_at(testvars.WebsiteUI["SubtitleMe_menu"], "")
    self.failUnless(sel.is_element_present(testvars.WebsiteUI["Logout_menuitem"]))
    
