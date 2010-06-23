# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars


#Login as a user

def TwitterAuth(self,sel,user,passw):
    print "twitter auth: "+ user+":"
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"username_or_email")
    sel.type("username_or_email", user)
    sel.type("session[password]", passw)
    sel.click("allow")
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

    
   

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
   
    
