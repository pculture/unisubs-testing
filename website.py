# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars


#Login as a user

def SiteLogIn(self,sel,user,passw):
    sel.set_timeout(testvars.MSTestVariables["TimeOut"])
    sel.open(testvars.MSTestVariables["Site"]+"/auth/login/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.window_maximize()
    sel.type("id_username", user)
    sel.type("id_password", passw)
    sel.click("//button[@value='login']")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
   # taking out verification as no longer displayed on page  
   # mslib.wait_for_element_present(self,sel,"link="+user)
   # if sel.is_element_present("link=sub_writer"):
   #     print "logged in as: " + user
   # else:
   #     mslib.AppendErrorMessage(self,sel,"login failed")

def TwitterLogIn(self,sel,user,passw):
    sel.set_timeout(testvars.MSTestVariables["TimeOut"])
    sel.open(testvars.MSTestVariables["Site"]+"/auth/login/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.window_maximize()
    sel.click("css=.twitter")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("username_or_email", user)
    sel.type("session[password]", passw)
    sel.click("allow")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

def OpenIdLogIn(self,sel,user,passw):
    sel.set_timeout(testvars.MSTestVariables["TimeOut"])
    sel.open(testvars.MSTestVariables["Site"]+"/auth/login/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.window_maximize()
    sel.click("css=.open-id")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("css=.openid", user)
    sel.click("css=.open-id")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])   
    sel.type("password", passw)
    sel.click("signin_button")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])


def GmailLogIn(self,sel,user,passw):
    sel.set_timeout(testvars.MSTestVariables["TimeOut"])
    sel.open(testvars.MSTestVariables["Site"]+"/auth/login/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.window_maximize()
    sel.click("css=.gmail")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("Email", "pcf.subwriter")
    sel.type("Passwd", "sub.writer")
    sel.click("signIn")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    

def verifyLogIn(self,sel,user):
    sel.open(testvars.MSTestVariables["Site"] + "/demo/")
    sel.select_frame("relative=top")
    if sel.get_text("css=.mirosubs-loggedIn") != "You are logged in as "+user:
        mslib.AppendErrorMessage(self,sel,"not logged in")
        print sel.get_text("css=mirosubs-loggedIn")
    else:
        print "logged in as: " +user
  

def start_new_video_sub(self,sel,url):
    sel.open(testvars.MSTestVariables["Site"]+"/videos/create/")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if sel.is_element_present("link=Restart this Step"):
        sel.click("link=Restart this Step")
        self.failUnless(re.search(r"^Are you sure you want to start over[\s\S] All subtitles will be deleted\.$", sel.get_confirmation()))
    sel.select_frame("relative=top")

