# website.py

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

def Login(self,sel,auth_type):
    # auth_type can be either ".twitter", ".open-id", "google"
    sel.click(testvars.WebsiteUI["Login_Button"])
    mslib.wait_for_element_present(self,sel,"css=."+auth_type)
    sel.click("css=." +auth_type)

def start_demo(self,sel):
    mslib.wait_for_element_present(self,sel,"css=a:contains('Try the Demo')")
    sel.click("css=a:contains('Try the Demo')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    #widget.close_howto_video


def start_sub_widget(self,sel):
    # Click Subtitle Me -> Add Subtitles
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["SubtitleMe_menu"])
    sel.click_at(testvars.WidgetUI["SubtitleMe_menu"], "")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["AddSubtitles_menuitem"])
    sel.click_at(testvars.WidgetUI["AddSubtitles_menuitem"], "")
    widget.close_howto_video(self,sel)

def start_new_video_sub(self,sel,url):
    sel.open(testvars.MSTestVariables["Site"]+"videos/create/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if sel.is_element_present(testvars.WidgetUI["SubtitleMe_menu"]):
        #in this case the button probably says "Continue subtitling"
        sel.click_at(testvars.WidgetUI["SubtitleMe_menu"], "")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["AddSubtitles_menuitem"])
        sel.click_at(testvars.WidgetUI["AddSubtitles_menuitem"], "")
        widget.close_howto_video(self,sel)
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-steps")
    while sel.is_text_present("Back to") or sel.is_text_present("Return to"):
        sel.click("css=.mirosubs-backTo")
        time.sleep(3)
        
    if sel.is_element_present("css=.mirosubs-restart"):
        # If it loads the widget automatically
        sel.click("css=.mirosubs-restart")
        self.failUnless(re.search(r"^Are you sure you want to start over[\s\S] All subtitles will be deleted\.$", sel.get_confirmation()))
    sel.select_frame("relative=top")

