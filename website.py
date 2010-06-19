# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars


#Login as a user

def LogIn(self,sel,user,passw):
    sel.set_timeout(testvars.MSTestVariables["TimeOut"])
    sel.open(testvars.MSTestVariables["Site"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.window_maximize()
    sel.click("link=Login")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("id_username", user)
    sel.type("id_password", passw)
    sel.click("//button[@value='login']")
    mslib.wait_for_element_present(self,sel,"link="+user)
    if sel.is_element_present("link=sub_writer"):
        print "logged in as: " + user
    else:
        mslib.AppendErrorMessage(self,sel,"login failed")

def start_new_video_sub(self,sel,url):
    sel.click(testvars.WebsiteUI["Subtitle_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    sel.type("video_url", url)
    sel.click(testvars.WebsiteUI["Video_Submit_Button"])
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    if sel.is_element_present("link=Restart this Step"):
        sel.click("link=Restart this Step")
        self.failUnless(re.search(r"^Are you sure you want to start over[\s\S] All subtitles will be deleted\.$", sel.get_confirmation()))
    sel.select_frame("relative=top")

