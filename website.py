# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars


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
   # taking out verification as no longer displayed on page  
   # mslib.wait_for_element_present(self,sel,"link="+user)
   # if sel.is_element_present("link=sub_writer"):
   #     print "logged in as: " + user
   # else:
   #     mslib.AppendErrorMessage(self,sel,"login failed")

def Login(self,sel,auth_type):
    # auth_type can be either ".twitter", ".open-id", "google"
    sel.click(testvars.WebsiteUI["Login_Button"])
    mslib.wait_for_element_present(self,sel,"css=."+auth_type)
    sel.click("css=." +auth_type)

def start_demo(self,sel):
    mslib.wait_for_element_present(self,sel,"css=a:contains('Try the Demo')")
    sel.click("css=a:contains('Try the Demo')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    

def start_sub_widget(self,sel):
    # Click Subtitle Me -> Add Subtitles
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["SubtitleMe_menu"])
    sel.click_at(testvars.WidgetUI["SubtitleMe_menu"], "")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["AddSubtitles_menuitem"])
    sel.click_at(testvars.WidgetUI["AddSubtitles_menuitem"], "")

def start_new_video_sub(self,sel,url):
    sel.open(testvars.MSTestVariables["Site"]+"videos/create/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if sel.is_element_present("link=Restart this Step"):
        # If it loads the widget automatically
        sel.click("link=Restart this Step")
        self.failUnless(re.search(r"^Are you sure you want to start over[\s\S] All subtitles will be deleted\.$", sel.get_confirmation()))
    else:
        start_sub_widget(self,sel)
    sel.select_frame("relative=top")

