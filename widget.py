# widget.py

from selenium import selenium

import unittest, time, re, codecs
import mslib, testvars


# transcribe video contents, takes input from a text file

def Login(self,sel,auth_type):
    #auth_type can be "log" (for site), "twitter","openid","gmail"
    print "logging in using "+auth_type+ " account"
    mslib.wait_for_element_present(self,sel, testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click_at(testvars.WebsiteUI["SubtitleMe_menu"], "")
    sel.click_at(testvars.WebsiteUI["Login_menuitem"], "")
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-"+auth_type)
    sel.click("css=.mirosubs-"+auth_type)
    
        
def close_howto_video(self,sel,skip=True):
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-modal-widget-content")
    if sel.is_element_present("css=.mirosubs-howtopanel"):
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-done:contains('Continue')")
        mslib.wait_for_element_present(self,sel,"css=.goog-checkbox-unchecked")
        if skip==True:
            sel.click("css=.goog-checkbox-unchecked")
        sel.click("css=.mirosubs-done:contains('Continue')")


def transcribe_video(self,sel,sub_file,mode="Expert",step="Continue"):
    print "starting to transcribe video"
    # giving the video a chance to load.
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    mode_label = sel.get_text("css=.mirosubs-speedmode option:contains("+mode+")")
    sel.select("//select", "label=" +mode_label)
    mslib.wait_for_video_to_buffer(self,sel)
        
    sel.click(testvars.WidgetUI["Play_pause"])

    for line in codecs.open(sub_file,encoding='utf-8'):
        sel.click("//div/input")
        sel.type("//div/input", line)
        sel.type_keys("//div/input"," ")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Transcribe_current_sub"])
        current_sub = sel.get_text(testvars.WidgetUI["Transcribe_current_sub"])
        if line.rstrip() != current_sub.rstrip():
            mslib.AppendErrorMessage(self,sel,"sub text mismatch")
            print "found: " + current_sub.rstrip()
            print "expected: " +line
        sel.key_press("//div/input", "\\13")
        time.sleep(2)
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])


def restart_typing(self,sel):
    if sel.is_element_present("css=.mirosubs-restart"):
    # If it loads the widget automatically
        sel.click("css=.mirosubs-restart")
        self.failUnless(re.search(r"^Are you sure you want to start over[\s\S] All subtitles will be deleted\.$", sel.get_confirmation()))

def back_step(self,sel):
    while sel.is_text_present("Back to") or sel.is_text_present("Return to"):
        sel.click("css=.mirosubs-backTo")
        time.sleep(3)
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-steps")

def sync_video(self,sel,sub_file,start_delay=5,sub_int=4):
    print "starting video / sub syncing"
    sel.select_frame("relative=top")
    #give video a chance to load
    time.sleep(5)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    print "clicking video play button to start playback"
    sel.click(testvars.WidgetUI["Video_playPause"])
       
    time.sleep(start_delay)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    for line in open(sub_file):
        sel.focus(testvars.WidgetUI["Sync_sub"])
        sel.click_at(testvars.WidgetUI["Sync_sub"],"")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Active_subtime"])
        print sel.get_text(testvars.WidgetUI["Active_subtime"]) +": "+ sel.get_text(testvars.WidgetUI["Active_subtext"])
        time.sleep(sub_int)
    sel.click(testvars.WidgetUI["Next_step"])
                  
def review_edit_text(self,sel,sub_file):
    print "editing text"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    li = 1
    #sel.click(testvars.WidgetUI["Sync_Review_play_pause"])
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

    
def review_time_shift_sync_hold(self,sel,sub_file,delay_time, sync_time):
    print "down key time shift"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    sel.click(testvars.WidgetUI["Video_playPause"])
    time.sleep(delay_time)
    li = 1
    time_stamp_el = "//li["+str(li)+"]/span[1]/span/span[1]"
    for line in open(sub_file):
        old_time = sel.get_text(time_stamp_el)
        sel.click(testvars.WidgetUI["Skip_back"])
        # 40 is the native key code for down arrow key
        sel.key_down_native("40")
        time.sleep(sync_time)
        sel.key_up_native("40")
        new_time = sel.get_text(time_stamp_el)
        print old_time + " ==> " + new_time
        if old_time == new_time:
            mslib.AppendErrorMessage(self,sel,"time's not shifted")
        time.sleep(delay_time)
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

def verify_login_message(self,sel):
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])
    self.failUnless(sel.get_text(testvars.WidgetUI['Must_Login'] +":contains('To save your subtitling work')")
    

                                     
