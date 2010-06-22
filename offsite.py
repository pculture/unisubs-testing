# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars


#Login as a user

def TwitterAuth(self,sel,user,passw):
    sel.select_frame("relative=top")
    sel.type("username_or_email", user)
    sel.type("session[password]", passw)
    sel.click("allow")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

def OpenIdAuth(self,sel,user,passw):
    sel.select_frame("relative=top")
    sel.type("css=.openid", user)
    sel.click("css=.open-id")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])   
    sel.type("password", passw)
    sel.click("signin_button")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])


def GmailAuth(self,sel,user,passw):
    sel.select_frame("relative=top")
    sel.type("Email", "pcf.subwriter")
    sel.type("Passwd", "sub.writer")
    sel.click("signIn")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
    
