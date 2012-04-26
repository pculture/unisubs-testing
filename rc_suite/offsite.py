"""
offsite.py
    Defines actions that don't take place directly on the universalsubtitles website or widget
"""
from selenium import selenium
import unittest
import time
import urllib
import random
import mslib
import testvars
import widget
import selvars


def TwitterAuth(self,sel,user,passw):
    """
    Description: Perform twitter account sign-in once window
                 has been launced via website or widget.
    Requires: valid username and password
    """
    print "twitter auth: "+ user+":"
    sel.select_pop_up("null")
    if sel.get_eval("window.location") == "http://twitter.com/universalsubs":
        if sel.is_element_present("css=.signin span:contains('Sign in')"):
            sel.click("css=.signin span:contains('Sign in')")
        mslib.wait_for_element_present(self,sel,"css=input[title='username']")
        sel.type("username", user)
        sel.type("password", passw)
        sel.click("signin_submit")
    else:
        time.sleep(2)
        sel.select_pop_up("null")
        mslib.wait_for_element_present(self,sel,"css=input[id=username_or_email]")
        sel.type("username_or_email", user)
        sel.type("session[password]", passw)
        sel.click("allow")
    if sel.is_element_present("css=th:contains('Humaness')"):
        self.fail("caught by the twitter captcha, can not continue")

def OpenIdAuth(self,sel,user,passw):
    """
    Description: Perform open id [from http://myopenid.com ]account sign-in once window
                 has been launced via website or widget.
    Requires: valid username and password
    """
    print "open id auth: "+ user
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"openid_url")
    sel.type("css=.openid", testvars.openiduser)
    sel.click("css=.open-id")
    mslib.wait_for_element_present(self,sel,"signin_button")
    sel.type("password", testvars.passw)
    sel.click("signin_button")
    

def GmailAuth(self,sel,user,passw):
    """
    Description: Perform gmail account sign-in once window
                 has been launced via website or widget.
    Requires: valid username and password
    """
    sel.select_pop_up("null")
    print "gmail auth: "+ user
    mslib.wait_for_element_present(self,sel,"signIn")
    sel.type("Email", user)
    sel.type("Passwd", passw)
    sel.click("signIn")


def handle_warning_popup(self,sel):
    """
    Description: Closes the warning pop-up for offsite widgets

    """
    sel.select_pop_up("null")
    if sel.is_element_present("css=.unisubs-warning"):
        sel.click("link=Continue")
        for i in range(60):
            try:
                if not sel.is_element_present("css=.unisubs-warning"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    sel.select_window("null")

def get_blip_video_url(self,file_type="flv"):
    

    if file_type == "ogv":
        blipURL = "http://blip.tv/file/get/Pycon-PyCon2011PythonTheSecretSauceInTheOpenCloud878.ogv"     
    elif file_type == "mp4":
        blipURL = "http://blip.tv/file/get/Wildcaster-ElephantCalfStrugglesToSwim947.mp4"
    else:
        blipURL = "http://blip.tv/file/get/JonHammond-LouisvilleKentuckyOneNightOnlyJonHammondQuartet855.flv"
    return blipURL


def get_vimeo_video_url(self):

    if "firefox" not in selvars.set_browser():
        vimeoURL = "http://vimeo.com/25378567"
    else:
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("vimeo"," get video url"), "http://vimeo.com/"))
        self.selenium.start()
        vsel= self.selenium
        try:
            vsel.set_timeout(testvars.MSTestVariables["TimeOut"])
            vsel.open("groups/all/sort:recent")
            vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
            vsel.click("css=.detail_format a.thumbnail")
            mslib.wait_for_element_present(self,vsel,"css=div.tabmain a:contains('Videos')")
            vsel.click("css=div.tabmain a:contains('Videos')")
            mslib.wait_for_element_present(self,vsel,"css=div#vimeo_dropdown_2")
            vsel.click_at("css=div#vimeo_dropdown_2", "")
            vsel.click_at("css=li#detail", "")
            mslib.wait_for_element_present(self,vsel,"css=.thumbnail_box a.thumbnail")
            vsel.click("css=.thumbnail_box a.thumbnail")
            mslib.wait_for_element_present(self, vsel,"css=input#clip_id")
            urlid = vsel.get_value("css=input#clip_id")
            vimeoURL = "http://vimeo.com/"+urlid
            print vimeoURL
        finally:
            vsel.stop()
    return vimeoURL

        
def get_youtube_video_url(self,vid_format="embed"):
    if "firefox" not in selvars.set_browser():
        youtubeURL = "http://www.youtube.com/watch?v=lVJVRywgmYM"
    else:
        cat_num = random.randint(1,26)
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("youtube"," get video url"), "http://youtube.com/"))
        self.selenium.start()
        vsel= self.selenium
        vsel.set_timeout(testvars.timeout)
        try:       
            if vid_format == "webm":
                vsel.open("results?uploaded=w&search_query=crazy&search_duration=short&webm=1&search_type=videos&uni=3&search_sort=video_date_uploaded")
            else:
                vsel.open("videos?s=mr&c="+str(cat_num))
            vsel.wait_for_page_to_load(testvars.timeout)

            for x in range(0,5):
                time.sleep(2)
#                if vsel.is_element_present("css=div.video-title"): break
                if vsel.is_element_present("css=div.browse-item-content"): break
                cat_num = random.randint(1,26)
                vsel.open("videos?s=mr&c="+str(cat_num))
                vsel.wait_for_page_to_load(testvars.timeout)
                if x == 4:
                    self.fail("can't get youtube video url")
#            vsel.click("css=div.video-title a")         
            vsel.click("css=div.browse-item-content h3 a")         
            vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
            youtubeURL = vsel.get_eval("window.location")
            print youtubeURL      

        finally:
            vsel.stop()
    return youtubeURL

def get_dailymotion_video_url(self):
    if "firefox" not in selvars.set_browser():
        dailymotionURL = "http://www.dailymotion.com/video/xjhmjf_souviens-toi-tafit-mag-seance-studio-d-enregistrement-ade-mougins_music"
    else:
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("dailymotion"," get video url"), "http://dailymotion.com/"))
        self.selenium.start()
        vsel= self.selenium
        try:
            vsel.set_timeout(testvars.MSTestVariables["TimeOut"])
            # open most recent cc licensed videos
            vsel.open("/en/creative/1")
            vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
            vsel.click("css=h3 a.dmco_simplelink")
            vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
            dailymotionURL = vsel.get_eval("window.location")
            print dailymotionURL      

        finally:
            vsel.stop()
    return dailymotionURL
