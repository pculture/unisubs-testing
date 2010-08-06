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
    """
    Description: Login to site using the website login button and a site account
    
    Requires: valid site user name and password.
    
    Pre-condition: user is on the site page.


    
    Post-condition: user is still on the site page
    """
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    sel.click(testvars.WebsiteUI["Login_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("id_username", user)
    sel.type("id_password", passw)
    sel.click("//button[@value='login']")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])

def SiteLogout(self,sel):
    """
    Description: Logout of site using site Logout button.

    """
    sel.open(testvars.WebsiteUI["SiteLogoutUrl"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    

def Login(self,sel,auth_type):
    """
    Description: Log on using website button and select an external login option.
    auth_type can be either '.twitter', '.open-id', or '.google'

    Requires: valid account for selected login.  See testvars for existing accounts.

    Pre-condition: user is on the site page
    
    Post-condition: offsite login form displayed, see offsite
    
    
    """
    # auth_type can be either ".twitter", ".open-id", "google"
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_Button"])
    sel.click(testvars.WebsiteUI["Login_Button"])
    mslib.wait_for_element_present(self,sel,"css=."+auth_type)
    sel.click("css=." +auth_type)
    #After login, use offsite to do auth

def start_demo(self,sel):
    """
    Description: Starts the demo widget from the site

    Pre-condition: site page is opened

    Post-condition: /demo page is opened, usually next step is start_sub_widget
    """
    sel.open(testvars.MSTestVariables["Site"]+"demo/")
#    mslib.wait_for_element_present(self,sel,"css=.try_link")
#    sel.click("css=.try_link span:contains('Demo')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    time.sleep(3) #safari is too fast

def submit_video(self,sel,url):
    """
    Description: Submit a video using the site button

    Pre-condition: site page is opened

    Post-condition: the widget is launched immediately.
    You'll need to deal with the help video, see widget.close_howto_video
    """
    sel.click(testvars.WebsiteUI["Subtitle_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])

def start_sub_widget(self,sel,skip="True"):
    """
    Description: Start the Subtitle Widget using the Subtitle Me menu.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where Subtitle Me menu is present.
    Test will fail if Choose Language menu is present.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
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
    """
    Description: Verifies user is logged in by finding the logout button on the
    website and then starting the demo and looking for logout menu item on the
    Subtitle Me button.

    Pre-Condition: must be logged into site.

    Post-Condition: will be on the /demo page
    """
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])
    start_demo(self,sel)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click_at(testvars.WebsiteUI["SubtitleMe_menu"], "")
    self.failUnless(sel.is_element_present(testvars.WebsiteUI["Logout_menuitem"]))
    
