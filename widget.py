# website.py

from selenium import selenium

import unittest, time, re
import mslib, testvars


# transcribe video contents, takes input from a text file

def Login(self,sel,auth_type):
    #auth_type can be "log" (for site), "twitter","openid","gmail"
    print "logging in using "+auth_type+ " account"
    sel.click_at(testvars.WidgetUI["SubtitleMe_menu"], "")
    sel.click_at(testvars.WidgetUI["Login_menuitem"], "")
    sel.select_frame("relative=top")
    sel.click("css=.mirosubs-"+auth_type)
    sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])

def verifyLogIn(self,sel,user):
    sel.select_frame("relative=top")
    if sel.get_text("css=.mirosubs-loggedIn") != "You are logged in as "+user:
        mslib.AppendErrorMessage(self,sel,"not logged in")
        print sel.get_text("css=.mirosubs-loggedIn")
    else:
        print "logged in as: " +user


def transcribe_video(self,sel,sub_file):
    print "starting to transcribe video"
    sel.select_frame("relative=top")
    # giving the video a chance to load.
    time.sleep(20)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Transcribe_play_pause"])
    if sel.get_text("css=.mirosubs-timeElapsed") == "null":
        sel.click(testvars.WidgetUI["Transcribe_play_pause"])
    for line in open(sub_file):
        sel.click("//div/input")
        sel.type("//div/input", line)
        sel.type_keys("//div/input"," ")
        time.sleep(2)
        current_sub = sel.get_text(testvars.WidgetUI["Transcribe_current_sub"])
        if line.rstrip() != current_sub.rstrip():
            mslib.AppendErrorMessage(self,sel,"sub text mismatch")
            print "found: " + current_sub.rstrip()
            print "expected: " +line
        sel.key_press("//div/input", "\\13")
        time.sleep(3)
    sel.click(testvars.WidgetUI["Next_step"])


def sync_video(self, sel, sub_file,start_time):
    print "starting video / sub syncing"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_Review_play_pause"])
    sel.key_press_native("40")
    #Using down key to start playback for now
#    sel.focus(testvars.WidgetUI["Sync_sub"])
 #   sel.click(testvars.WidgetUI["Sync_sub"])
     #use key press to start playback, 32 is for spacebar.
 #   sel.key_down_native("32")
 #   sel.key_up_native("32")
     

    time.sleep(start_time)
    for line in open(sub_file):
        # 40 is the native key code for down arrow
        sel.key_press_native("40")
        time.sleep(5)
        print sel.get_text(testvars.WidgetUI["Active_subtime"]) +": "+ sel.get_text(testvars.WidgetUI["Active_subtext"])
        
    sel.click(testvars.WidgetUI["Next_step"])
                  
def review_edit_text(self,sel,sub_file):
    print "editing text"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_Review_play_pause"])
    li = 1
    #sel.click(testvars.WidgetUI["Sync_Review_play_pause"])
    # use key_press_native 32 for spacebar
    sel.key_press_native("32")
    time.sleep(5)
    for line in open(sub_file):
        text_el = "//li[" +str(li) + "]/span[2]"
        time_stamp_el = "//li["+str(li)+"]/span[1]/span/span[1]"
        
        # 1. edit the text contents to be all upper case.
        sel.click(text_el)
        sel.type("css=.mirosubs-title textarea", line.upper())
        sel.click(time_stamp_el)
        mslib.wait_for_element_present(self,sel,text_el)
        if line.rstrip().upper() != sel.get_text(text_el).rstrip():
            mslib.AppendErrorMessage(self,sel,"sub text mismatch")
            print "found: " + sel.get_text(text_el).rstrip()
            print "expected: " +line.rstrip().upper()
        # Put it back
        sel.click(text_el)
        sel.type("css=.mirosubs-title textarea", line)
        sel.click(time_stamp_el)
        mslib.wait_for_element_present(self,sel,text_el)
        time.sleep(3)
        li = li+1
    

        
def review_drag_bubbles(self,sel,sub_file):
        start_time = sel.get_text(time_stamp_el)
        print start_time
        drag_bubble(self,sel,line.upper(),"left","-60")
        stop_time = sel.get_text(time_stamp_el)
        print start_time +": "+stop_time
        # 2. drag the left side of the bubble -pixels  and verify time change
        
        # 3. drag the left side of the bubble + pixels and verify time change

        # 4. drag the right side of the bubble -pixels  and verify time change

        # 5. drag the right side of the bubble + pixels and verify time change
        

def review_time_shift_arrows(self,sel,sub_file):
    left_arrow_el = "//li["+str(li)+"]/span[1]/span/span[2]/a[2]"
    right_arrow_el = "//li["+str(li)+"]/span[1]/span/span[2]/a[1]"
    # 6. Click text-arrow left and verify time jump

    # 7. Click text-arrow right and verify time jump

    
def review_time_shift_sync_hold(self,sel,sub_file):
    print "spacebar time shift"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_Review_play_pause"])
    sel.focus(testvars.WidgetUI["Sync_Review_play_pause"])
    sel.click(testvars.WidgetUI["Sync_Review_play_pause"])
    time.sleep(8)
    li = 1
    time_stamp_el = "//li["+str(li)+"]/span[1]/span/span[1]"
    for line in open(sub_file):
        old_time = sel.get_text(time_stamp_el)
        sel.click(testvars.WidgetUI["Skip_back"])
        # 40 is the native key code for down arrow key
        sel.key_down_native("40")
        time.sleep(4)
        sel.key_up_native("40")
        new_time = sel.get_text(time_stamp_el)
        time.sleep(6)
        print old_time + " ==> " + new_time
        if old_time == new_time:
            mslib.AppendErrorMessage(self,sel,"time's not shifted")
        li = li + 1        

    

def drag_bubble(self,sel,sub_text,side,move_pixels):
    li = 1
    for line in open(sub_file):
        text_el = "//li[" +str(li) + "]/span[2]"
        time_stamp_el = "//span["+str(li)+"]/span/span[1]"
        if "left" in side:
            sel.drag_and_drop("css=.mirosubs-subtext:contains(" + sub_text + ") + span", move_pixels+",0")
        if "right" in side:
                sel.drag_and_drop("css=.mirosubs-subtext:contains(" + sub_text + ") +span + span", move_pixels+",0")




