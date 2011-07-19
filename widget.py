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
import re






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
    time.sleep(5)  # give the widget a chance to open directly if it's going to.
    select_video_language(self,sel)
    close_howto_video(self,sel)
            
    if sel.is_element_present("css=.mirosubs-modal-widget"):
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])
        sel.click(testvars.WidgetUI["Must_Login"])
        
    else:
        if sel.is_element_present("css=.mirosubs-uniLogo"):
            mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["Login_menuitem"])
            sel.click(testvars.WebsiteUI["Login_menuitem"])

 #   sel.select_frame("relative=top")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-modal-login-content")
    sel.click("css=a.mirosubs-" +auth_type)
    
        

def site_login_from_widget_link(self,sel):
    """
    Description: performs a site login from the Login link on the widget steps.

    Pre-condition: widget is opened and user is not logged in.

    Post-condition: user is returned to starting widget page.
    """
    if sel.is_element_present(testvars.WidgetUI["Must_Login"]):   
        # log in from widget
        sel.click("link=LOGIN")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-modal-login")
        time.sleep(2)
        sel.click("css=.mirosubs-log")
        site_login_auth(self,sel)
    else:
        print "User is already logged into site"

def site_login_auth(self,sel):
    """
    Description: specifically logs in as the site user defined in <a href="testvars.html">testvars</a>

    Pre-condition: Login was clicked from widget

    Post-condition: user logged in and returned to widget page.
    """
    time.sleep(5)
    sel.select_pop_up("null")
    mslib.wait_for_element_present(self,sel,"id_username")
    sel.type("id_username", testvars.siteuser)
    sel.type("id_password", testvars.passw)
    sel.click("//button[@value='login']")
    #wait for the login to complete
    time.sleep(10)

def open_starter_dialog(self,sel):
    sel.click(testvars.WebsiteUI["NewTranslation_menuitem"])        
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Select_language"])
    mslib.wait_for_text_present(self,sel,"This video")
    

def starter_dialog_edit_orig(self,sel):
    """Choose the current lang to edit.
    Return orig_lang

    Gets the videos orig lang to edit the original subs - or sets it to English if none set.

    Post-condition: the widget is launched and you will be on step 1.
    """
    
    #Figure our the original lang or choose your own
    orig_lang = "Original"
    if sel.is_element_present(testvars.WebsiteUI["AddSubtitles_menuitem"]):
        sel.click(testvars.WebsiteUI["AddSubtitles_menuitem"])
    time.sleep(5)
    if sel.is_element_present(testvars.create_lang_unknown): # No lang set, going to use English
        orig_lang = "English"
        select_video_language(self,sel,vid_lang='en',sub_lang='en')
    elif sel.is_element_present(testvars.create_lang_known):        
        ol = sel.get_text(testvars.create_lang_known)
        orig_lang = ol.split("in ")[1]
        print orig_lang
        lc = sel.get_value("css=p select option:contains('"+orig_lang+"')")
        lang_code = re.sub("\d+$","",lc)
        select_video_language(self,sel,vid_lang=lang_code,sub_lang=lang_code)
    else:
        print "video opened directly - no lang select dialogs"
    time.sleep(5)
    close_howto_video(self,sel)
    mslib.wait_for_element_present(self,sel,"css=div.mirosubs-help-heading")
    return orig_lang


def starter_dialog_translate_from_orig(self,sel,to_lang='hr'):
    """Choose the a new translation and translate from original lang
    Return orig_lang

    This assumes you know the original language and want to edit the original subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    #Figure out orig lang fail is there isn't a set lang already
    mslib.wait_for_text_present(self,sel,"This video")
    if sel.is_element_present(testvars.create_lang_unknown):
        self.fail("can't make a new translation when video has no orig lang set - test is invalid")
    else:
        ol = sel.get_text(testvars.create_lang_known)
        orig_lang = ol.split("in ")[1]
        lc = sel.get_value("css=p select option:contains('"+orig_lang+" ')")
        lang_code = re.sub("\d+$","",lc) #gives only the letters of the value field.
        from_code = re.sub("\D","",lc)  #gives only the number - used in from pulldown.
        select_video_language(self,sel,sub_lang=to_lang,from_lang=from_code)
        time.sleep(5)
        close_howto_video(self,sel)
        mslib.wait_for_element_present(self,sel,"css=div.mirosubs-help-heading")
        return orig_lang

def starter_dialog_translate_from_not_orig(self,sel,from_lang,to_lang='hr'):
    """Choose the a new translation and translate from a sub that is not the orig lang.
    Return from_lang

    This assumes you know the original language and want to edit the original subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    #Figure out orig lang fail is there isn't a set lang already
    mslib.wait_for_text_present(self,sel,"This video")
    if sel.is_element_present(testvars.create_lang_unknown):
        self.fail("can't make a new translation when video has no orig lang set - test is invalid")
    else:
        ol = sel.get_text(testvars.create_lang_known)
        orig_lang = ol.split("in ")[1]
        lc = sel.get_value("css=p select option:contains('"+orig_lang+" ')")
        lang_code = re.sub("\d+$","",lc)
    if lang_code == from_lang:
        self.fail("invalid test - from lang "+str(from_lang)+" is the same as the origi lang"+str(orig_lang))
        
    select_video_language(self,sel,sub_lang=to_lang,from_lang=from_lang)
    time.sleep(5)
    close_howto_video(self,sel)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-help-heading")
    return from_lang



def starter_dialog_fork(self,sel,to_lang='hr'):
    """Choose the a new translation and translate from original lang
    Return orig_lang

    This assumes you know the original language and want to edit the original subs.

    Post-condition: the widget is launched and you will be on step 1 or Edit step
    """
    #Figure out orig lang fail is there isn't a set lang already
    mslib.wait_for_text_present(self,sel,"This video")
    if sel.is_element_present(testvars.create_lang_unknown):
        self.fail("can't make a new translation when video has no orig lang set - test is invalid")
    else:
        ol = sel.get_text(testvars.create_lang_known)
        orig_lang = ol.split("in ")[1]
        select_video_language(self,sel,sub_lang=to_lang,from_lang='forkk')
        time.sleep(5)
        close_howto_video(self,sel)
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")
        return orig_lang

def get_lang_cc(self,sel,language):
    """Gives back the lang code for Subtitle Into language.

     Precondition: starter dialog must be open.
     

    """
    lc = sel.get_value("css=p select option:contains('"+language+" ')")
    lang_code = re.sub("\d+$","",lc) #gives only the letters of the value field.
    return lang_code

def select_video_language(self,sel,vid_lang="en",sub_lang="en-gb",from_lang='forkk'):
    time.sleep(5)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Select_language"])
    sel.select_frame("relative=top")
    mslib.wait_for_text_present(self,sel,"Subtitle into")
    
    if sel.is_element_present(testvars.create_lang_unknown): # Don't know the video lang so choose for 1st time subs.
        sel.select(testvars.create_lang_unknown +" + select", "value=regexp:^"+str(vid_lang))
        if sel.is_element_present(testvars.create_subtitle_into):
            sel.select(testvars.create_subtitle_into +" + select", "value=regexp:^"+str(sub_lang))
        print "edit orig subs, orig: "+str(vid_lang)+" to: "+str(sub_lang)
    else:
        mslib.wait_for_element_present(self,sel,testvars.create_lang_known) 
        
        sel.select(testvars.create_subtitle_into +" + select", "value=regexp:^"+str(sub_lang))
        print "subbing into: "+str(sub_lang)
        time.sleep(2)
        if sel.is_element_present(testvars.create_translate_from+" + span select") == True:
            sel.select(testvars.create_translate_from+" + span select", "value=regexp:^"+str(from_lang))
            print "selected video language, from: "+str(from_lang)
    time.sleep(1)
    sel.click("link=Continue")
   

        
def close_howto_video(self,sel,skip=True):
    """
    Description: closes the how-to interstitial help video
    Default is set to "True", to skip the video on proceeding steps.

    Pre-condition: widget has been launched.
    
    Post-condition: help video is closed and returned to previous widget page.
    """
    time.sleep(10)
    sel.select_frame("relative=top")
    if sel.is_element_present("css=.mirosubs-howtopanel"):
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-done:contains('Continue')")
        mslib.wait_for_element_present(self,sel,"css=.goog-checkbox-unchecked")
        if skip==True:
            sel.click("css=.goog-checkbox-unchecked")
        sel.click("css=.mirosubs-done:contains('Continue')")
        time.sleep(3)
        if sel.is_element_present("css=.mirosubs-done:contains('Continue')"):
            sel.click("css=.mirosubs-done:contains('Continue')")
    else:
        print "no how-to video"
            


def transcribe_video(self,sel,sub_file,mode="Expert",step="Continue", buffer="yes"):
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
    print ("Transcribing the video")
    sel.select_window("null")
    restart_step(self,sel)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-speedmode")
    try:
        if mode == "Recommended":
        # Recommended mode
            sel.select("css=.mirosubs-speedmode select", "value=au")
        elif mode == "Beginner":
        # Beginner mode
            sel.select("css=.mirosubs-speedmode select", "value=pl")
        # Expert mode
        elif mode == "Expert":
            sel.select("css=.mirosubs-speedmode select", "value=no")
    except:
        print ("trouble selecting element (safari issue?) - going with default value")
        

    sel.click(testvars.WidgetUI["Play_pause"])
    for i,line in enumerate(codecs.open(sub_file,encoding='utf-8')):
        x=i+1
        sel.focus("css=input[class*=trans]")
        sel.type("css=input[class*=trans]",line)
        sel.type_keys("css=input[class*=trans]",' ')
        time.sleep(1)
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Transcribed_text"])
        current_sub = sel.get_text(testvars.WidgetUI["Transcribed_text"])
        print current_sub
        
        # compare input text
##        self.assertEqual(line.rstrip(),current_sub.rstrip(),\
##        "sub text mismatch - expected: "+line.rstrip()+" found: "+current_sub.rstrip())
##        if "firefox" in selvars.set_browser() or "iexplore" in selvars.set_browser():
##            sel.key_press("css=.trans", "13")
##        else:
        sel.get_eval("this.browserbot.getUserWindow().mirosubs.widget.fireKeySequence(this.browserbot.getUserWindow().document.getElementsByClassName('trans')[0], 13,13);")    
        
    if step == "Continue":
        sel.click_at(testvars.WidgetUI["Next_step"],"")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-done span:contains('Reviewing')")


 


def restart_step(self,sel):
    """
    Description: Clicks the 'Restart this Step' link, and handle the confirmation dialog.
    """
    if sel.is_element_present("css=.mirosubs-restart"):
        sel.click("link=Restart this Step")
        if sel.is_element_present("css=.mirosubs-activestep:contains('2')"):
            try:
                self.assertTrue(re.search(r"^Are you sure you want to start over[\s\S] All timestamps will be deleted\.$", sel.get_confirmation()))
            except:
                if "5." in (sel.get_eval("navigator.appVersion")):
                    sel.key_press("css=div", "13") #workaround for FF 4 selenium confirmation bug
                
        if sel.is_element_present("css=.mirosubs-activestep:contains('1')"):
            try:
                self.assertTrue("Are you sure you want to start over? All subtitles will be deleted.", sel.get_confirmation())
            except:
                if "5." in (sel.get_eval("navigator.appVersion")):
                    sel.key_press("css=div", "13") #workaround for FF 4 selenium confirmation bug

def back_step(self,sel):
    """
    Description: Clicks the 'Back to' link to go back 1 step.
    """
    while sel.is_text_present("Back to Typing"):
        sel.click("link=Back to Typing")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep")

def sync_video(self,sel,sub_file,start_delay=3,sub_int=2,step="Continue"):
    """
    Description: Use the defined sync button to sync the subtitles.  Waits for
    text present on the video and prints the subtime.

    Options:
        sub_file - path to file or text lines to enter
        start_delay - time to wait before 1st sync (default = 4 secs)
        sub_int - time to wait before next sub (default = 2 secs
        step - {'Continue' (default) | 'Stop} move on to next step when done.

    Pre-condition - can use this to sync on Step 2, Step 3 or Edit.
    """
    print ("Syncing the subs")
    sel.select_window("null")
    mslib.wait_for_video_to_buffer(self,sel)
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
    #start playback
#    sel.type_keys("css=.mirosubs-play",u'\u0009')
    if sel.is_element_present(testvars.WidgetUI["Video_pause_button"]):
        print "video is playing"
    else:
        sel.focus(testvars.WidgetUI["Play_pause"])
        sel.click_at(testvars.WidgetUI["Play_pause"],"")
    time.sleep(start_delay)
    #start syncing   
    
    for i,line in enumerate(open(sub_file)):
        x=i+1
        sel.focus(testvars.WidgetUI["Sync_sub"])
        sel.click_at(testvars.WidgetUI["Sync_sub"],"")
        time.sleep(.5)
        sub_cell_start_time = "css=li:nth-child("+str(x)+") > span.mirosubs-timestamp span span.mirosubs-timestamp-time"
        sub_cell_text = "css=li:nth-child("+str(x)+") > span.mirosubs-title span"
        start_time=sel.get_text(sub_cell_start_time)
        print start_time
        print sel.get_text(sub_cell_text)
        time.sleep(sub_int)
    # finish sync of the last sub
    sel.focus(testvars.WidgetUI["Sync_sub"])
    sel.click_at(testvars.WidgetUI["Sync_sub"],"")
    if step == "Continue":
        sel.click(testvars.WidgetUI["Next_step"])
    
                  


def edit_text(self,sel,subtextfile,new_text=""):
    """
    Description: Input the same text used in transcribe_video and for each line,
    edit the text with new_text.  Verifies text has been updated.

    Options:
        new_text - text string

    Pre-condition - can use this on Step 2, Step 3.
    """
    print ("Editing the sub text in the widget")
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=ul.mirosubs-titlesList")
    sel.click("css=.mirosubs-activestep") #reset the list to the top of the page
    mslib.wait_for_video_to_buffer(self,sel)
   
    for i,line in enumerate(open(subtextfile)):
        x = i+1
        sub_cell = "css=ul.mirosubs-titlesList li:nth-child("+str(x)+")"       
        if sel.is_element_present(sub_cell) == False:
            break
        textspan = sub_cell +" > .mirosubs-title span"
        thetextarea = "css=.mirosubs-subedit"     
        
        if new_text == "":
            ed_text = str(line).rstrip().upper()
        else:
            ed_text = new_text
        sel.click(textspan)
        time.sleep(.5)
        print ed_text
        sel.type(thetextarea, ed_text)
        sel.get_eval("this.browserbot.getUserWindow().mirosubs.widget.fireKeySequence(this.browserbot.getUserWindow().document.getElementsByClassName('mirosubs-subedit')[0], 13,13);")   
      
        time.sleep(1)
#        self.assertTrue(sel.is_element_present(textspan))
        sub_cell_text=sel.get_text(textspan)
        print sub_cell_text
        self.assertEqual(sub_cell_text.rstrip(),ed_text.rstrip())
        time.sleep(.5)
        


def edit_translation(self,sel,subtextfile,new_text=""):
    """
    Description: Update the translation text with either the orig text or text provided in a file.

    Options:
        new_text - text string

    Pre-condition - Editing Translation Widget opened
    """
    print ("Editing the translation")
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
    for i,line in enumerate(codecs.open(subtextfile)):
        x = i+1
        sub_cell = "css=.mirosubs-titlesList li:nth-child("+str(x)+")"
        if sel.is_element_present(sub_cell) == False:
            break
        thetextarea = "css=textarea"
        if new_text == "":
            ed_text = str(line).upper()
        else:
            ed_text = new_text
        sel.click(sub_cell)
        sel.type(thetextarea, u'ed_text')
        sel.get_eval("this.browserbot.getUserWindow().mirosubs.widget.fireKeySequence(this.browserbot.getUserWindow().document.getElementsByClassName('mirosubs-subedit')[0], 13,13);") 
        time.sleep(1)
    sel.click(testvars.WidgetUI["Next_step"])
        
def drag_time_bubbles(self,sel,subtextfile):
    """
    Description: Grab
    the left and right sides of the timeline bubbles and edit the time.
    Verifies the time stamp has been modified.
    
    Options:
        new_text - text string

    Pre-condition - use must be on Step 3 or Review with known text data.
    """
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep:contains('3')")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
           
    sub_cell_start_time = "css=li:nth-child(1) > .mirosubs-timestamp span span.mirosubs-timestamp-time"
    # drag bubble to the left and verify time change
    start_time = sel.get_text(sub_cell_start_time)
    print "sub start time: " '%.2f' % float(start_time)
    drag_it(self,sel,"left","60")
    time.sleep(1)
    new_start_time = sel.get_text(sub_cell_start_time)
    print " - new sub time: " '%.2f' % float(new_start_time)
    self.failUnless(float(start_time) < float(new_start_time))

  
def drag_it(self,sel,side,move_pixels):
    """
    Description: actually grabs the timeline bubbles and moves them

    Options:
        sub_text - text used to locate correct bubble
        side - {'left' | 'right'}
        move_pixels - number of pixels to move bubble { + | - }
    """
    if side == "left":
        sel.focus("css=.mirosubs-timeline-sub .mirosubs-grabber.mirosubs-leftGrabber")
        sel.drag_and_drop("css=.mirosubs-timeline-sub .mirosubs-grabber.mirosubs-leftGrabber", move_pixels+",0")


    if side == "right":
        sel.focus("css=.mirosubs-timeline-sub .mirosubs-grabber.mirosubs-rightGrabber")
        sel.drag_and_drop("css=.mirosubs-timeline-sub .mirosubs-grabber.mirosubs-rightGrabber", move_pixels+",0")


def click_time_shift_arrows(self,sel,subtextfile):
    """
    Description: clicks the left and right arrows on subtitle text box.
    Verifies that the time has been changed by .05 seconds.

    Options:
        subtextfile - text used in transcribe step.
        
    """
    sub_li = 1
    sel.select_window("null")
    mslib.wait_for_element_present(self,sel,"css=.mirosubs-activestep:contains('3')")
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
    sub_cell_start_time = "css=li:nth-child("+str(sub_li)+") > .mirosubs-timestamp span span.mirosubs-timestamp-time"
    up_arrow = "css=li:nth-child("+str(sub_li)+") > .mirosubs-timestamp span .mirosubs-changeTime .mirosubs-up"
    down_arrow = "css=li:nth-child("+str(sub_li)+") > .mirosubs-timestamp span .mirosubs-changeTime .mirosubs-down"
    for x in range(0,3):  
        #Click up (right) and verify time jump of .05 seconds
        start_time = sel.get_text(sub_cell_start_time)
        sel.focus(up_arrow)
        sel.click_at(up_arrow,"")
        new_start_time = sel.get_text(sub_cell_start_time)
        self.assertAlmostEqual(mslib.calc_time_diff(start_time,new_start_time),float(.05),3)
        #maybe verify the pixel change on the timeline
    for x in range(0,3):
        #Click text-arrow right and verify time jump
        start_time = sel.get_text(sub_cell_start_time)
        sel.click_at(down_arrow,"")
        new_start_time = sel.get_text(sub_cell_start_time)
        self.assertAlmostEqual(mslib.calc_time_diff(new_start_time,start_time),float(.05),3)
        #maybe verify the pixel change on the timeline

    
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
    sel.click(testvars.WidgetUI["Play_pause"])
    time.sleep(delay_time)
  
    sub_li = 1
    for line in open(sub_file):
        sub_cell_start_time = "css=li:nth-child("+str(sub_li)+") > .mirosubs-timestamp span span.mirosubs-timestamp-time"
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

    if sel.is_element_present("css=.mirosubs-activestep:contains('1')"):
        goto_step(self,sel,"2")
    mslib.wait_for_video_to_buffer(self,sel)
    sel.click(testvars.WidgetUI["Video_playPause"])
       
    time.sleep(start_delay)
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Sync_sub"])
       
    for i,line in enumerate(codecs.open(subtextfile,encoding='utf-8')):
        x = i+1
        sub_cell_start_time = "css=li:nth-child("+str(x)+") > .mirosubs-timestamp span span.mirosubs-timestamp-time"
        start_time=sel.get_text(sub_cell_start_time)
        sel.focus(testvars.WidgetUI["Sync_sub"])
        sel.click_at(testvars.WidgetUI["Sync_sub"],"")
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Active_subtime"])
        new_start_time = sel.get_text(testvars.WidgetUI["Active_subtime"])
        self.assertNotEqual(float(start_time),float(new_start_time), \
                        '%.2f' % float(start_time) +" = " +'%.2f' % float(new_start_time))
        time.sleep(sub_int)
        
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
        sub_cell_text = "css=li:nth-child("+str(sub_li)+") > .mirosubs-title"
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

def set_subs_complete(self,sel,done=True):
    time.sleep(5)
    sel.select_frame("relative=top")
    if sel.is_text_present("Entire video completed?") == True:
        if done==True:
            if sel.is_element_present("css=.goog-checkbox-unchecked"):
                sel.click("css=.goog-checkbox-unchecked")
        elif done==False:
            if sel.is_element_present("css=.goog-checkbox-checked"):
                sel.click("css=.goog-checkbox-checked")
        sel.click("css=.mirosubs-green-button.mirosubs-big")
        time.sleep(3)

        
def submit_sub_edits(self,sel,offsite=False):
    print " * Submit subtitles"
    sel.select_window("null")
    #give video a chance to load
    mslib.wait_for_element_present(self,sel,testvars.widget_steps)
    #Go to step 3 before submit
    if not sel.get_text("css=li a.mirosubs-activestep") == "3":
        sel.click("css=.mirosubs-help-heading li a:contains('3')")
    sel.click(testvars.WidgetUI["Next_step"])
    set_subs_complete(self,sel,done=True)
    if offsite==False:
        mslib.wait_for_element_present(self,sel,testvars.video_video_info)
    time.sleep(10)
    

def goto_step(self,sel,step="3"):
    
    mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Next_step"])
    sel.click("css=.mirosubs-help-heading li a:contains('"+step+"')")
    self.assertTrue(sel.get_text("css=li a.mirosubs-activestep:contains('"+step+"')"))


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
