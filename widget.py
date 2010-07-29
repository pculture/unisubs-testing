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

def site_login_from_widget_link(self,sel):
    auth_type = "log"
    #auth_type can be "log" (for site), "twitter","openid","gmail"
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])        
    print "loggin in from widget"
    sel.click("link=LOGIN")
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-"+auth_type)
    sel.click("css=.mirosubs-"+auth_type)
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"id_username")
    sel.type("id_username", testvars.siteuser)
    sel.type("id_password", testvars.passw)
    sel.click("//button[@value='login']")
    #wait for the login to complete
    time.sleep(10)
    
        
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

def sync_video(self,sel,sub_file,start_delay=2,sub_int=2,step="Continue"):
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
    sel.focus(testvars.WidgetUI["Sync_sub"])
    sel.click_at(testvars.WidgetUI["Sync_sub"],"")
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])
    
                  
def review_edit_text(self,sel,sub_file):
    print "editing text"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    li = 1

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

def edit_text(self,sel,subtextfile,new_text="my hovercraft is full of eels"):
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
    sub_li=1
    for line in open(subtextfile):
        sub_cell = "//li["+str(sub_li)+"]/span[2]"
        sel.focus(sub_cell)
        sel.click(sub_cell)
        sel.type("css=textarea", new_text)
        sel.key_press("css=textarea", "\\13")
        sub_cell_text=sel.get_text(sub_cell)
        if sub_cell_text.rstrip() != new_text.rstrip():
            mslib.AppendErrorMessage(self,sel,"text not edited correctly")
            print "expected: " +new_text+ "found: "+ sub_cell_text.rstrip
        sub_li = sub_li + 1
        
def drag_time_bubbles(self,sel,sub_file):

    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li = 1
    for line in open(subtextfile):
        #Fix Me - find correct xpath or css for the sub bubble elements and start time
        sub_cell_start_time = "//span["+str(li)+"]/span/span[1]"
        sub_cell_end_time = "//span["+str(li)+"]/span/span[2]"
    
        # drag start time to the left and verify time change
        start_time = sel.get_text(sub_cell_start_time)
        print start_time
        drag_it(self,sel,line.upper(),"left","-60")
        new_start_time = sel.get_text(sub_cell_start_time)
        self.failUnless(int(start_time) > int(new_start_time))

        # drag start time to the right and verify time change
        start_time = sel.get_text(sub_cell_start_time)
        print start_time
        drag_it(self,sel,line.upper(),"left","+60")
        new_start_time = sel.get_text(sub_cell_start_time)
        self.failUnless(int(start_time) < int(new_start_time))
           
        # drag end time to the left and verify time change
        end_time = sel.get_text(sub_cell_end_time)
        print end_time
        drag_it(self,sel,line.upper(),"right","-60")
        new_end_time = sel.get_text(sub_cell_end_time)
        self.failUnless(int(end_time) > int(new_end_time))

        # drag end time to the right and verify time change
        end_time = sel.get_text(sub_cell_end_time)
        print end_time
        drag_it(self,sel,line.upper(),"right","+60")
        new_end_time = sel.get_text(sub_cell_end_time)
        self.failUnless(int(end_time) < int(new_end_time))

  
def drag_it(self,sel,sub_text,side,move_pixels):
        if "left" in side:
            sel.drag_and_drop("css=.mirosubs-subtext:contains(" + sub_text + ") + span", move_pixels+",0")
        if "right" in side:
                sel.drag_and_drop("css=.mirosubs-subtext:contains(" + sub_text + ") +span + span", move_pixels+",0")


                

def click_time_shift_arrows(self,sel,subtextfile):
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li = 1
    for line in open(subtextfile):
        sub_cell_start_time = "//span["+str(li)+"]/span/span[1]"
        sub_cell_end_time = "//span["+str(li)+"]/span/span[2]"
        
    #Fix Me - find correct xpath or css for the sub bubble elements and start time
        left_arrow = "//li["+str(li)+"]/span[1]/span/span[2]/a[2]"
        right_arrow = "//li["+str(li)+"]/span[1]/span/span[2]/a[1]"
        for x in range(0,5):  
            #Click text-arrow left and verify time jump of .02 seconds
            start_time = sel.get_text(sub_cell_start_time)
            print start_time
            sel.click(left_arrow)
            new_start_time = sel.get_text(sub_cell_start_time)
            self.failUnless(int(start_time) - int(new_start_time)) == .02
            #maybe verify the pixel change on the timeline
        for x in range(0,5):
            #Click text-arrow right and verify time jump
            end_time = sel.get_text(sub_cell_start_time)
            print start_time
            sel.click(right_arrow)
            new_end_time = sel.get_text(sub_cell_end_time)
            self.failUnless(int(new_end_time) - int(end_time)) == .02
            #maybe verify the pixel change on the timeline

    
def hold_down_delay_sub(self,sel,sub_file,delay_time=4,hold_time=2, sync_time=2):
    print "down key time shift"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    sel.click(testvars.WidgetUI["Video_playPause"])
    time.sleep(delay_time)
    sel.click(testvars.WidgetUI["Skip_back"])
    li = 1
    sub_cell_start_time = "//li["+str(li)+"]/span[1]/span/span[1]"
    for line in open(sub_file):
        old_time = sel.get_text(sub_cell_start_time)
        # 40 is the native key code for down arrow key
        sel.key_down_native("40")
        time.sleep(hold_time)
        sel.key_up_native("40")
        new_time = sel.get_text(time_stamp_el)
        print old_time + " ==> " + new_time
        if old_time == new_time:
            mslib.AppendErrorMessage(self,sel,"time's not shifted")
        time.sleep(sync_time)
        li = li + 1

def resync_videos (self,sel,subtextfile,start_delay=1,sub_int=.5, step="Stop"):
    print "starting sub resync"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    sel.click(testvars.WidgetUI["Video_playPause"])
       
    time.sleep(start_delay)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li = 1
    for line in open(subtextfile):
        #Fix Me - find correct xpath for the sub start time in a cell
        sub_cell_start_time = "//span["+str(li)+"]/span/span[1]"
        start_time=sel.get_text(sub_cell_start_time)
        sel.focus(testvars.WidgetUI["Sync_sub"])
        sel.click_at(testvars.WidgetUI["Sync_sub"],"")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Active_subtime"])
        new_start_time = sel.get_text(testvars.WidgetUI["Active_subtime"])
        self.failUnless(int(start_time) < int(new_start_time))
        time.sleep(sub_int)
    sel.focus(testvars.WidgetUI["Sync_sub"])
    sel.click_at(testvars.WidgetUI["Sync_sub"],"")
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])


def verify_login_message(self,sel):
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])
    self.failUnless(sel.get_text(testvars.WidgetUI['Must_Login'] +":contains('To save your subtitling work')"))

def steps_display(self,sel,step_num):
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")
    self.failUnless("Typing" == sel.get_text("css=h2"))
    self.failUnless(str(step_num) == sel.get_text("css=.mirosubs-activestep"))
    self.failUnless("tab" == sel.get_text("css=.mirosubs-tab"))
    self.assertEqual("Play next 8 seconds", sel.get_text("css=.mirosubs-tab + span"))
    self.assertEqual("ctrl", sel.get_text("css=.mirosubs-control"))
    self.assertEqual("Re-play last 8 seconds", sel.get_text("css=.mirosubs-control + span"))
    self.assertEqual("Speed Mode", sel.get_text("css=.mirosubs-speedmode h4"))

def verify_sub_text(self,sel,subtextfile):
    print "verifying sub text"
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
    sub_li=1
    for line in codecs.open(subtextfile,encoding='utf-8'):
        sub_cell_text = "//li["+str(sub_li)+"]/span[2]"
        print sel.get_text(sub_cell_text)
        self.assertEqual(line.rstrip(), sel.get_text(sub_cell_text).rstrip())
        sub_li = sub_li + 1
        
