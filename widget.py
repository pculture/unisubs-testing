"""
widget.py
Description: handles actions that are performed within the widget.
"""

from selenium import selenium

import unittest
import time
import re
import codecs
import mslib
import testvars
import selvars


def Login(self,sel,auth_type):
    """
    Description: Initiates login sequence using the Subtitle Me menu that's attached to
    an embedded video, either onsite or offsite.

    auth_type can be 'log' (for site), 'twitter','openid','google'
    Requires valid accounts for chosen login type

    Pre-condition: Subtitle me widget menu should be present on page.

    Post-condition: either site or external login authorization pages are opened.
    For offsite login options see <a href="offsite.html">offsite</a>
    """
    print "logging in using "+auth_type+ " account"
    mslib.wait_for_element_present(self,sel, testvars.WebsiteUI["SubtitleMe_menu"])
    sel.click(testvars.WebsiteUI["SubtitleMe_menu"])
    time.sleep(3)  # give the widget a chance to open directly if it's going to.
    select_video_language(self,sel)
            
    if sel.is_element_present("css=.mirosubs-modal-widget"):
        close_howto_video(self,sel)
        time.sleep(3)
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])
        sel.click(testvars.WidgetUI["Must_Login"])
        
    else:
        if sel.is_element_present("css=.mirosubs-uniLogo"):
            mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_menuitem"])
            sel.click(testvars.WebsiteUI["Login_menuitem"])

 #   sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-modal-login")
    sel.click("css=.mirosubs-" +auth_type)
    
        

def site_login_from_widget_link(self,sel):
    """
    Description: performs a site login from the Login link on the widget steps.

    Pre-condition: widget is opened and user is not logged in.

    Post-condition: user is returned to starting widget page.
    """

    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])        
    # log in from widget
    sel.click("link=LOGIN")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-modal-login")
    sel.click("css=.mirosubs-log")
    site_login_auth(self,sel)

def site_login_auth(self,sel):
    """
    Description: specifically logs in as the site user defined in <a href="testvars.html">testvars</a>

    Pre-condition: Login was clicked from widget

    Post-condition: user logged in and returned to widget page.
    """
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"id_username")
    sel.type("id_username", testvars.siteuser)
    sel.type("id_password", testvars.passw)
    sel.click("//button[@value='login']")
    #wait for the login to complete
    time.sleep(10)


def select_video_language(self,sel,vid_lang="English",sub_lang="English"):
    time.sleep(3)
    if sel.is_element_present(testvars.WidgetUI["Select_language"]):
        sel.select_frame("relative=top")
        vid_label = sel.get_text("css=p:nth-child(1) > select option:contains("+vid_lang+")")
        sel.select("//select", "label=" +vid_label)
        sub_label = sel.get_text("css=p:nth-child(2) > select option:contains("+sub_lang+")")
        sel.select("//select", "label=" +sub_label)
        sel.click("link=Continue")
    else:
        print "no language selection box"
        
def close_howto_video(self,sel,skip="True"):
    """
    Description: closes the how-to interstitial help video
    Default is set to "True", to skip the video on proceeding steps.

    Pre-condition: widget has been launched.
    
    Post-condition: help video is closed and returned to previous widget page.
    """
    time.sleep(3)
    if sel.is_element_present("css=.mirosubs-howtopanel"):
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-done:contains('Continue')")
        mslib.wait_for_element_present(self,sel,"css=.goog-checkbox-unchecked")
        if skip=="True":
            sel.click("css=.goog-checkbox-unchecked")
        sel.click("css=.mirosubs-done:contains('Continue')")


def transcribe_video(self,sel,sub_file,mode="Expert",step="Continue", buffer="no"):
    """
    Description: On widget Step 1, reads in lines of subtitle text and types it.

    Options: 
        sub_file - the full path to the text to enter
        mode - sets typing mode {'Beginner' | 'Recommended' | 'Expert (default)'}
        step - {'Stop' | 'Continue' (default)} Continue on to next step.
        buffer {'yes' | 'no' (default) } will buffer the video to 75% before
        proceeding. see wait_for_video_to_buffer

        returns line_count - the number of text lines input for the translation
    """
    print " * Transcribe video"
    # giving the video a chance to load.
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    mode_label = sel.get_text("css=.mirosubs-speedmode option:contains("+mode+")")
    sel.select("//select", "label=" +mode_label)
    # For html5 video, wait for the video to buffer
    if sel.is_element_present("css=.mirosubs-videoDiv video") or buffer != "no":
        mslib.wait_for_video_to_buffer(self,sel)
    else: time.sleep(10)
    sel.type_keys("css=.mirosubs-play",u'\u0009')
    
    line_count = 0
    for line in codecs.open(sub_file,encoding='utf-8'):
        sel.focus("css=input[class*=trans]")
        sel.type("css=input[class*=trans]",line)
        sel.type_keys("css=input[class*=trans]",' ')    
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Current_playing_sub"])
        current_sub = sel.get_text(testvars.WidgetUI["Current_playing_sub"])
        # compare input text
        self.assertEqual(line.rstrip(),current_sub.rstrip(),\
                         "sub text mismatch - expected: "+line.rstrip()+" found: "+current_sub.rstrip())
        
        transcribe_enter_text(self,sel)
        time.sleep(1)
        line_count = line_count+1
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])
    return line_count


def transcribe_enter_text(self,sel):
    """ Handle the text entry in Step 1 typing for all browsers

    """
    if (selvars.vbrowser == "*firefox") or (selvars.vbrowser == "*chrome"):
        sel.key_press("css=.trans", "13")
    else:
        sel.key_press_native('10')    


def restart_step(self,sel):
    """
    Description: Clicks the 'Restart this Step' link, and handle the confirmation dialog.
    """
    if sel.is_element_present("css=.mirosubs-restart"):
        sel.click("link=Restart this Step")
        if sel.is_element_present("css=.mirosubs-activestep:contains('2')"):
            self.assertTrue(re.search(r"^Are you sure you want to start over[\s\S] All timestamps will be deleted\.$", sel.get_confirmation()), \
                            "missing or incorrect confirmation dialog")

def back_step(self,sel):
    """
    Description: Clicks the 'Back to' link to go back 1 step.
    """
    while sel.is_text_present("Back to Typing"):
        sel.click("link=Back to Typing")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")

def sync_video(self,sel,sub_file,start_delay=4,sub_int=3,step="Continue"):
    """
    Description: Use the defined sync button to sync the subtitles.  Waits for
    text present on the video and prints the subtime.

    Options:
        sub_file - path to file or text lines to enter
        start_delay - time to wait before 1st sync (default = 2 secs)
        sub_int - time to wait before next sub (default = 2 secs
        step - {'Continue' (default) | 'Stop} move on to next step when done.

    Pre-condition - can use this to sync on Step 2, Step 3 or Edit.
    """
    print " * Sub syncing"
    sel.select_frame("relative=top")
    #give video a chance to load
    time.sleep(10)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])

    sel.focus(testvars.WidgetUI["Sync_sub"])
    sel.click_at(testvars.WidgetUI["Sync_sub"],"")   
       
    time.sleep(start_delay)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li=1
    for line in open(sub_file):
        sel.focus(testvars.WidgetUI["Sync_sub"])
        sel.click_at(testvars.WidgetUI["Sync_sub"],"")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Current_playing_sub"])
        sub_cell_start_time = "//li["+str(sub_li)+"]/span[1]/span/span[1]"
        start_time=sel.get_text(sub_cell_start_time)
#        print " - sub time: " '%.2f' % float(start_time) + " - sub text: "+ sel.get_text(testvars.WidgetUI["Current_playing_sub"])
        time.sleep(sub_int)
        sub_li = sub_li + 1
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])
    
                  


def edit_text(self,sel,subtextfile,new_text="my hovercraft is full of eels"):
    """
    Description: Input the same text used in transcribe_video and for each line,
    edit the text with new_text.  Verifies text has been updated.

    Options:
        new_text - text string

    Pre-condition - can use this to sync on Step 2, Step 3 or Edit.
    """
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
    sub_li=1
    for line in open(subtextfile):
        sub_cell = "//li["+str(sub_li)+"]/span[2]"
        sel.focus(sub_cell)
        sel.click(sub_cell)
        mslib.wait_for_element_present(self,sel,"css=textarea")
        sel.type("css=textarea", new_text)
        sel.key_press("css=textarea", "\\13")
        sub_cell_text=sel.get_text(sub_cell)
        self.assertEqual(sub_cell_text.rstrip(),new_text.rstrip())
        sub_li = sub_li + 1
        
def drag_time_bubbles(self,sel,subtextfile):
    """
    Description: For each line, initially used in transcribe_video, grab
    the left and right sides of the timeline bubbles and edit the time.
    Verifies the time stamp has been modified.
    
    Options:
        new_text - text string

    Pre-condition - use must be on Step 3 or Review with known text data.
    """
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep:contains('3')")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li = 1
    for line in open(subtextfile):
        
        sub_cell_start_time = "//li["+str(sub_li)+"]/span[1]/span/span[1]"
        sub_cell_end_time = "//span["+str(sub_li)+"]/span/span[2]"

        #start playback - wait for sub to appear on screen then pause playback
        sub_line = line.split(',')
        first_phrase = sub_line[0]
        print first_phrase
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
        sel.click(testvars.WidgetUI["Video_playPause"])
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-captionDiv:contains('" + first_phrase + "')")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        sel.click(testvars.WidgetUI["Video_playPause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        # drag start time to the left and verify time change
        start_time = sel.get_text(sub_cell_start_time)
        print start_time
##        drag_it(self,sel,first_phrase,"left","-60")
##        new_start_time = sel.get_text(sub_cell_start_time)
##        self.failUnless(int(start_time) > int(new_start_time))
##
        # drag start time to the right and verify time change
        start_time = sel.get_text(sub_cell_start_time)
        print " - sub time: " '%.2f' % float(start_time)
        drag_it(self,sel,"left","+60")
        time.sleep(10)
        new_start_time = sel.get_text(sub_cell_start_time)
        print " - new sub time: " '%.2f' % float(new_start_time)
        self.failUnless(float(start_time) < float(new_start_time))
##           
##        # drag end time to the left and verify time change
##        end_time = sel.get_text(sub_cell_end_time)
##        print end_time
##        drag_it(self,sel,first_word,"right","-60")
##        new_end_time = sel.get_text(sub_cell_end_time)
##        self.failUnless(int(end_time) > int(new_end_time))
##
        # drag end time to the right and verify time change
        end_time = sel.get_text(sub_cell_end_time)
        print " - sub end time: " '%.2f' % float(end_time)
        drag_it(self,sel,"right","+60")
        time.sleep(10)
        new_end_time = sel.get_text(sub_cell_end_time)
        print " - sub end time: " '%.2f' % float(new_end_time)
        self.failUnless(float(end_time) < float(new_end_time))

  
def drag_it(self,sel,side,move_pixels):
    """
    Description: actually grabs the timeline bubbles and moves them

    Options:
        sub_text - text used to locate correct bubble
        side - {'left' | 'right'}
        move_pixels - number of pixels to move bubble { + | - }
    """
    if side == "left":
        sel.focus("css=.mirosubs-grabber.mirosubs-leftGrabber")
        sel.drag_and_drop("css=.mirosubs-grabber.mirosubs-leftGrabber", "'"+move_pixels+",0'")

    if side == "right":
        sel.focus("css=.mirosubs-grabber.mirosubs-rightGrabber")
        sel.drag_and_drop("css=.mirosubs-grabber.mirosubs-rightGrabber", "'"+move_pixels+",0'")                

def click_time_shift_arrows(self,sel,subtextfile):
    """
    Description: clicks the left and right arrows on subtitle text box.
    Verifies that the time has been changed by .05 seconds.

    Options:
        subtextfile - text used in transcribe step.
        
    """
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep:contains('3')")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li = 1
    for line in open(subtextfile):
        sub_cell_start_time = "//li["+str(sub_li)+"]/span[1]/span/span[1]"
        up_arrow = "//li["+str(sub_li)+"]/span[1]/span/span[2]/a[1]"
        down_arrow = "//li["+str(sub_li)+"]/span[1]/span/span[2]/a[2]"
        for x in range(0,5):  
            #Click up (right) and verify time jump of .05 seconds
            start_time = sel.get_text(sub_cell_start_time)
            sel.focus(up_arrow)
            sel.click_at(up_arrow,"")
            new_start_time = sel.get_text(sub_cell_start_time)
            self.assertEqual(mslib.calc_time_diff(start_time,new_start_time),float(.05))
            #maybe verify the pixel change on the timeline
        for x in range(0,5):
            #Click text-arrow right and verify time jump
            start_time = sel.get_text(sub_cell_start_time)
            sel.click_at(down_arrow,"")
            new_start_time = sel.get_text(sub_cell_start_time)
            self.assertEqual(mslib.calc_time_diff(start_time,new_start_time),float(.05))
            #maybe verify the pixel change on the timeline
        sub_li = sub_li + 1

    
def hold_down_delay_sub(self,sel,sub_file,delay_time=2,hold_time=.75, sync_time=1):
    """
    Description: tests the time shift of subs when holding then releasing the down key.
    Verifies that the time has been shifted.

    Options:
        delay_time - amount of time to wait before jumping back with ctrl key (default=4)
        hold_time - amount of time to hold down the key (default=2) 
        sync_time - amount of time wait before starting next subtitle (default=2)

    Pre-conditions: must coordinate this with the times used in sync_video or the time shift
    comparision may fail.

    Post-condition - still on same step in widget, with new times.
    """
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep:contains('3')")
    print " * Resync subs: hold down key"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    sel.click(testvars.WidgetUI["Video_playPause"])
    time.sleep(delay_time)
  
    sub_li = 1
    for line in open(sub_file):
        sub_cell_start_time = "//li["+str(sub_li)+"]/span[1]/span/span[1]"
        old_time = sel.get_text(sub_cell_start_time)
        # 40 is the key code for down arrow key
        sel.focus("css=.mirosubs-down")
        sel.key_down("css=.mirosubs-down","\\40")
        time.sleep(hold_time)
        sel.key_up("css=.mirosubs-down","\\40")
        new_time = sel.get_text(sub_cell_start_time)
        self.assertNotEqual(float(new_time),float(old_time), \
                        "no time change: "+'%.2f' % float(new_time) +"="+ '%.2f' % float(old_time))
        time.sleep(sync_time)
        sub_li = sub_li + 1

def resync_video (self,sel,subtextfile,start_delay=1,sub_int=1, step="Stop"):
    """
    Description: tests the time shift of subs when using down key to resyncronize.
    Verifies time stamp has changed.

    Options:
        start_delay - amount of time to wait before jumping back with ctrl key (default=4)
        sub_int - amount of before next sub sync
        step - {'Stop' (default) | 'Continue'}

    Pre-conditions: must coordinate this with the times used in sync_video or the time shift
    comparision may fail.
    """
    print " * Resync subs - shorter interval"
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
    sel.click(testvars.WidgetUI["Video_playPause"])
       
    time.sleep(start_delay)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_li = 1
    
    for line in codecs.open(subtextfile,encoding='utf-8'):
        sub_cell_start_time = "//li["+str(sub_li)+"]/span[1]/span/span[1]"
        start_time=sel.get_text(sub_cell_start_time)
        sel.focus(testvars.WidgetUI["Sync_sub"])
        sel.click_at(testvars.WidgetUI["Sync_sub"],"")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Active_subtime"])
        new_start_time = sel.get_text(testvars.WidgetUI["Active_subtime"])
        self.assertNotEqual(float(start_time),float(new_start_time), \
                        '%.2f' % float(start_time) +" = " +'%.2f' % float(new_start_time))
        time.sleep(sub_int)
        sub_li = sub_li + 1
        
    sel.focus(testvars.WidgetUI["Sync_sub"])
    sel.click_at(testvars.WidgetUI["Sync_sub"],"")
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])


def verify_login_message(self,sel):
    """
    Description: verifies the widget must login message is displayed when a user is not logged in.
    """
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])
    self.assertTrue(sel.get_text(testvars.WidgetUI['Must_Login'] +":contains('LOGIN')"),"Login message missing on widget")

def steps_display(self,sel,step_num):
    """
    Description: verifies text contents of Steps.  
    """
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep:contains('"+str(step_num)+"')")
    self.assertTrue(str(step_num) == sel.get_text("css=.mirosubs-activestep"),"active step is not: "+str(step_num))
    self.assertTrue("tab" == sel.get_text("css=.mirosubs-tab"),"tab not in help text")
    if step_num == "1":
        self.assertTrue("Typing" == sel.get_text("css=h2"), "heading is not Typing")
        self.assertEqual("Play next 8 seconds", sel.get_text("css=.mirosubs-tab + span"))
    else:
        self.assertEqual("Play/Pause", sel.get_text("css=.mirosubs-tab + span"))
    self.assertEqual("shift\n+\ntab", sel.get_text("css=.mirosubs-control"))
    self.assertEqual("Skip Back 8 Seconds", sel.get_text("css=.mirosubs-control + span"))
    self.assertEqual("Speed Mode", sel.get_text("css=.mirosubs-speedmode h4"))

def verify_sub_text(self,sel,subtextfile):
    """
    Description: Compares the current text in the text box with the text in the input subtextfile.

    Pre-condition: User in widget, steps 1,2,3 or Edit.

    """
    print "verifying sub text"
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
    sub_li=1
    for line in codecs.open(subtextfile,encoding='utf-8'):
        sub_cell_text = "//li["+str(sub_li)+"]/span[2]"
        self.assertEqual(line.rstrip(), sel.get_text(sub_cell_text).rstrip())
        sub_li = sub_li + 1
        
def wait_for_offsite_login(self,sel):
    time.sleep(2)
    for i in range(90):
        try:
            sel.select_window("null")
            print "wait for spinner to stop and login complete."
            if sel.is_element_present("css=.mirosubs-widget"):
                if not sel.is_element_present("css=.big_spinner"):break
                
        except: pass
        time.sleep(1)


def close_widget(self,sel,submit="Discard"):
    """
    Description: uses the red close x to close out the widget.

    Options: "Submit" or "Discard" {default} subtitles.

    Pre-Condition: Widget is opened on page.
    
    Post Conditions: Returned to originating site.
    """
    sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Close_widget"])
    self.assertTrue(sel.is_element_present(testvars.WidgetUI["Close_widget"]),"no close button found")
    time.sleep(3)
    sel.click(testvars.WidgetUI["Close_widget"])
    time.sleep(3)
    # if it doesn't close - just open the page again.
    if sel.is_element_present(testvars.WidgetUI["Close_widget"]):
        print "widget didn't close the way I want it too"
        sel.open()
