"""
mslib.py
Help Modules specific to universal subtitles project
"""

import re
import time
import datetime
import testvars

def remove_html_tags(data):
    """
    removes html tags from test data
    """
    p = re.compile(r'<.*?>')
    return p.sub('', data)


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
    for i in range(60):
        try:
            if sel.is_element_present(input_field): break
        except: pass
        time.sleep(1)
    else:
        self.fail("time out waiting for element " +input_field)

def wait_for_video_to_buffer(self,sel):
    """
    Description: Waits for the video in the frame to buffer to 75%.
                 This is always called by widget.transcribe_video
    """
    # on some browsers, need to start playback for browser to start to buffer
    #start play, then pause to wait for buffer
    sel.click(testvars.WidgetUI["Play_pause"])
    wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
    sel.click(testvars.WidgetUI["Video_pause_button"])
    wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
    wait_for_element_present(self,sel,"css=.mirosubs-buffered")
    
    print " - waiting for video to buffer " +time.strftime("%M:%S", time.gmtime())
    for i in range(60):
        try:
            if int(sel.get_element_width("css=.mirosubs-buffered")) >= 125: break
        except: pass
        time.sleep(1)
    print " - video buffered to 50% " +time.strftime("%M:%S", time.gmtime())

def calc_time_diff(time1,time2):
    t2 = datetime.datetime.strptime(time2, "%H:%M.%S")
    t1 = datetime.datetime.strptime(time1, "%H:%M.%S")
    diff = t2 - t1
    return diff.seconds
