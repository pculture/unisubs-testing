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
    if sel.is_element_present("css=.mirosubs-warning"):
        sel.click("link=Continue")
        for i in range(60):
            try:
                if not sel.is_element_present("css=.mirosubs-warning"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
    sel.select_window("null")

def get_blip_video_url(self,file_type="flv"):
    try:
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("blip"," get video url"), "http://blip.tv/"))
        self.selenium.start()
        bsel= self.selenium
        bsel.set_timeout(testvars.MSTestVariables["TimeOut"])
        random_url = "posts?sort=random&file_type="+file_type+"&page=1&view=list"
        bsel.open(random_url)
        print "opening: "+random_url
        mslib.wait_for_element_present(self,bsel,"css=.EpisodeListThumb img")
        bsel.click("css=.EpisodeListThumb img")
        time.sleep(5)
        blipURL = bsel.get_eval("window.location")
    except:
        print "error getting video, type:" +file_type
    finally:
        bsel.close()
        bsel.stop()
    print blipURL
    return blipURL


def get_vimeo_video_url(self):
    try:
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("vimeo"," get video url"), "http://vimeo.com/"))
        self.selenium.start()
        vsel= self.selenium
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
        vsel.close()
        vsel.stop()
    return vimeoURL

        
def get_youtube_video_url(self,vid_format="embed"):
    cat_num = random.randint(1,26)
    try:
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("youtube"," get video url"), "http://youtube.com/"))
        self.selenium.start()
        vsel= self.selenium
        vsel.set_timeout(testvars.MSTestVariables["TimeOut"])
        if vid_format == "webm":
            vsel.open("results?uploaded=w&search_query=crazy&search_duration=short&webm=1&search_type=videos&uni=3&search_sort=video_date_uploaded")
        else:
            vsel.open("videos?s=mr&c="+str(cat_num))
            #vsel.open("results?uploaded=w&search_query=crazy&search_duration=short&search_type=videos&uni=3&search_sort=video_date_uploaded")
        vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
#        vsel.click("css=h3 a[id^='video-long-title']")
        vsel.click("css=div.video-entry a[id^=video-thumb]")             
        vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        youtubeURL = vsel.get_eval("window.location")
        print youtubeURL      

    finally:
        vsel.close()
        vsel.stop()
    return youtubeURL

def get_dailymotion_video_url(self):
    try:
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser("dailymotion"," get video url"), "http://dailymotion.com/"))
        self.selenium.start()
        vsel= self.selenium
        vsel.set_timeout(testvars.MSTestVariables["TimeOut"])
        # open most recent cc licensed videos
        vsel.open("/en/creative/1")
        vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        vsel.click("css=h3 a.dmco_simplelink")
        vsel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        dailymotionURL = vsel.get_eval("window.location")
        print dailymotionURL      

    finally:
        vsel.close()
        vsel.stop()
    return dailymotionURL
