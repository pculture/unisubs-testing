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
    sel.open("/logout/?next=/")
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
    sel.open("/logout/?next=/")
    mslib.wait_for_element_present(self,sel,"css=.login_link")
    if sel.is_element_present(testvars.WebsiteUI["Logout_Button"]):
        sel.click(testvars.WebsiteUI["Logout_Button"])
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
    sel.open("/demo/")
#    mslib.wait_for_element_present(self,sel,"css=.try_link")
#    sel.click("css=.try_link span:contains('Demo')")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

def submit_video(self,sel,url):
    """
    Description: Submit a video using the site button

    Pre-condition: site page is opened

    Post-condition: the widget is launched immediately.
    You'll need to deal with the help video, see widget.close_howto_video
    """
    sel.open("/")
    sel.click(testvars.WebsiteUI["Subtitle_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    

def start_sub_widget(self,sel,skip="True"):
    """
    Description: Start the Subtitle Widget using the Subtitle Me menu.
    skip is set to true by default and gets passed to widget.close_howto_video
    to prevent further how-to video displays.

    Pre-condition: On a page where Subtitle Me menu is present.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    # Click Subtitle Me (Continue Subtitling -> Add Subtitles)
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(5)
    if sel.is_element_present("css=.mirosubs-modal-widget"):
        print "widget opened directly - no menu displayed."
    elif sel.is_element_present("css=.mirosubs-uniLogo"):
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["AddSubtitles_menuitem"])
        sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])
    else:
        print "not sure what's going on here, no widget, not menu"
    widget.close_howto_video(self,sel,skip)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")
    sel.select_frame("relative=top")

def verify_login(self,sel,username="sub_writer"):
    """
    Description: Verifies user is logged in by finding the logout button on the
    website and then starting the demo and looking for logout menu item on the
    Subtitle Me button.

    Pre-Condition: must be logged into site.

    Post-Condition: will be on the /demo page
    """
    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Logout_Button"])
    self.failUnless(sel.is_element_present("css=.user_panel"))
    print "logged in as: " + sel.get_text("css=.user_panel")
    self.failUnless(sel.is_element_present("css=.user_panel:contains("+username+")"))
    #not starting demo to check logged in status anymore
##    start_demo(self,sel)
##    mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
##    sel.click_at(testvars.WebsiteUI["SubtitleMe_menu"], "")
##    self.failUnless(sel.is_element_present(testvars.WebsiteUI["Logout_menuitem"]))


def verify_submitted_video(self,sel,vid_url,embed_type="html5"):
    """
    Description: Verifies the contents of the main video page of a submitted video.
    Require's the original url and expected type of embed.  Assumes html5 video if not specified.

    embed_type one of 'youtube', 'flow' 'html5' (default)

    Returns: url of the video on the universalsubtitles site.
    """
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv")
    if embed_type == "flow":
        print "verifying video embedded with flowplayer"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv object")
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv object[data*=\"flowplayer\"]"))
    elif embed_type == "youtube":
        print "verifying video embedded with youtube"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-videoDiv object")
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv object[data*=\"youtube.com\"]"))
    else:
        print "verifying video is html5"                        
        self.failUnless(sel.is_element_present("css=.mirosubs-videoDiv video"))
    print "verifying embedded video url is same as original"    
    self.failUnless(sel.is_element_present("css=.mirosubs-embed:contains("+vid_url+")"))
    unisubs_link = sel.get_text("css=.mirosubs-permalink[href]")
    return unisubs_link
