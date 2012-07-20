"""
mslib.py
Help Modules specific to universal subtitles project
"""

import re
import os
import time
import datetime
import testvars
import timeit
##import selvars

def AppendErrorMessage(self,sel,msg):
    """
    Formats an error message to append to output log.
    """
    self.verificationErrors.append(msg)
    print "**** Error ****   "+msg


def wait_for_element_present(self,sel,input_field):
    """
    Description: Waits 60 seconds for element to present itself.
    Requires: valid element identifier, can be css, xpath
    """
    
    for i in range(30):
        
        try:
            if sel.is_element_present(input_field): break
        except: pass
        time.sleep(1)
    else:
        self.fail("time out waiting 30s for element " +input_field)
  


def wait_for_element_not_present(self,sel,input_field):
    """
    Description: Waits 60 seconds for element to present itself.
    Requires: valid element identifier, can be css, xpath
    """
    for i in range(30):
        
        try:
            if sel.is_element_present(input_field) == False: break
        except: pass
        time.sleep(1)
    else:
        self.fail("time out waiting 30s for element " +input_field)

    

def wait_for_text_present(self,sel,ttext):
    """
    Description: Waits 60 seconds for element to present itself.
    Requires: text expected
    """
    for i in range(30):
        try:
            if sel.is_text_present(ttext): break
        except: pass
        time.sleep(1)
    else:
        self.fail("time out waiting 30s for text " +ttext)



def wait_for_text_not_present(self,sel,ttext):
    """
    Description: Waits 60 seconds for element to present itself.
    Requires: valid element identifier, can be css, xpath
    """
    for i in range(30):
        try:
            if sel.is_text_present(ttext) == False: break
        except: pass
        time.sleep(1)
    else:
        self.fail("time out waiting 30s for text " +ttext)

def wait_for_video_to_buffer(self,sel):
    """
    Description: Waits for the video in the frame to buffer to 30%.
                 This is always called by widget.transcribe_video
    """
    # on some browsers, need to start playback for browser to start to buffer
    #start play, then pause to wait for buffer
#    if selvars.set_browser() == "*firefox":
    time.sleep(2)
    try:
        if sel.is_element_present(testvars.WidgetUI["Video_pause_button"]):
            print "autoplaying"
            sel.focus(testvars.WidgetUI["Play_pause"])
            sel.click_at(testvars.WidgetUI["Play_pause"],"")
            time.sleep(5)
        if sel.is_element_present("css=.unisubs-buffered"):
            print " - waiting for video to buffer " +time.strftime("%M:%S", time.gmtime())
            for i in range(30):
                try:
                    if int(sel.get_element_width("css=.unisubs-buffered")) >= 125:
                        print " - video buffered to 50% " +time.strftime("%M:%S", time.gmtime())
                        break
                except: pass
                time.sleep(1)
        
    finally:
        print " - done loading video"

def calc_time_diff(time1,time2):
    print float(time2)
    print float(time1)
    diff = float(time2) - float(time1)
    return diff


def set_test_id(test_id):
    
    s = str(test_id).strip(">,<,[,]")
    L = s.split('_')
    testid = L.pop()
    return testid

def take_screenshot(self,sel):
    current_page_url = sel.get_location()
    #print current_page_url
    url_stripped_of_protocol = current_page_url.split("://")[1]
    #print url_stripped_of_protocol
    trimmed_page_url = url_stripped_of_protocol.replace("/","_")
    #print trimmed_page_url
    results_path = os.path.join(os.getcwd(), "Results")
    filename = os.path.join(
        results_path, 
        trimmed_page_url+"_"+time.strftime("%Y%m%d_%H%M", time.gmtime())+".png")
    print "Saving the screenshot to "+filename    
    sel.capture_entire_page_screenshot(filename,"")
    
