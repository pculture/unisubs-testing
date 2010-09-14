from selenium import selenium
import unittest
import os
import time
import re
import sys
import codecs
import selvars
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class subgroup_69(unittest.TestCase):
    """
    Litmus Subgroup 69 - Demo Wiget UI tests
    389 How-to video continue
    395 How-to video skip
    373 Step 1 Typing the subs
    397 Step 1 Beginner mode
    470 Step 1 Advanced mode
    398 Step 1 Expert mode
    399 Step 1 Play-Pause tab + button
    403 Step 2 Play-Pause tab + button
    404 Step 3 Play-Pause tab + button
    400 Step 1 Skip back (button only)
    409 Step 2 Skip back (button only)
    410 Step 3 Skip back (button only)
    406 Step 1 Restart typing
    401 Step 1 Login
    405 Step 2 Login
    416 Step 3 Login
    411 Step 2 Sync
    388 Step 2 Edit sub text (caps,smalls, non-ascii)
    415 Step 3 Edit sub text (caps, smalls, non-ascii)
    408 Step 2 back to typing
    402 Step 3 Down to Sync
    413 Step 3 Drag sub bubbles
    414 Step 3 Text time arrows
    412 Step 3 Hold down to delay sub start
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(), selvars.set_site() )
        self.selenium.start()

# The test cases of the subgroup



    def test_389(self):
        """
        Tests How to video display and Continue
        http://litmus.pculture.org/show_test.cgi?id=389
        """
        print "starting testcase 389"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel,skip=False)
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Next_step"])
        sel.click(testvars.WidgetUI["Next_step"])
        widget.close_howto_video(self,sel,skip=False)
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Next_step"])
        sel.click(testvars.WidgetUI["Next_step"])
        widget.close_howto_video(self,sel,skip=False)



    def test_395(self):
        """
        Tests How to video display and skip setting
        http://litmus.pculture.org/show_test.cgi?id=395
        """
        print "starting testcase 395"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        # start sub widget and click the skip checkbox
        website.start_sub_widget(self,sel,skip=True)
        # pass through the edit steps 1-3 and verify no more video
        
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Next_step"])
        sel.click(testvars.WidgetUI["Next_step"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Next_step"])
        sel.click(testvars.WidgetUI["Next_step"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Next_step"])                     
        


    def test_373(self):
        """
        Tests Step 1 typing the subtitles
        http://litmus.pculture.org/show_test.cgi?id=373
        """
        print "starting testcase 373"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        # verify subs present on next screen                    
        


    def test_397(self):
        """
        Tests Beginner mode setting in Step 1 Typing.
        http://litmus.pculture.org/show_test.cgi?id=397
        """
        print "starting testcase 397"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #Type sub-text in the video, then wait stay on Step-1 screen
        widget.transcribe_video(self,sel,subtextfile,mode="Beginner", step="Stop", buffer="yes")
        # wait for play button to indicate playback was paused, then start playback and see if it auto-stops
        for x in range(0,2):
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
            start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            sel.click(testvars.WidgetUI["Video_play_button"])
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(stop_time) - int(start_time)
            if not  7 < diff_time < 10:
                mslib.AppendErrorMessage(self,sel,"didn't stop after 8 seconds")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time       
        # verify subs present on next screen
        widget.verify_sub_text(self,sel,subtextfile)
        


    def test_470(self):
        """
        Tests Advanced (Recommended) setting Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=470
        """
        print "starting testcase 470"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #Type sub-text in the video, then wait stay on Step-1 screen
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
        mode_label = sel.get_text("css=.mirosubs-speedmode option:contains('Recommended')")
        sel.select("//select", "label=" +mode_label)
        mslib.wait_for_video_to_buffer(self,sel)
        sel.click(testvars.WidgetUI["Play_pause"])
        # keep typing while in playback mode until button changes to play button (indicating paused)
        sel.click("//div/input")
        for x in range(0,6):
            while sel.is_element_present(testvars.WidgetUI["Video_pause_button"]):
                time.sleep(.20)
                sel.type_keys("//div/input","Hi ")
            # stop typing and wait for playback to resume (pause button present)
            print "playback stopped at: "+sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            sel.type_keys("//div/input", "I'm Asa Dotzler")
            sel.key_press("//div/input", "\\13")
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
            print "playback resumed at: "+sel.get_text(testvars.WidgetUI["Video_elapsed_time"])




    def test_398(self):
        """
        Tests Expert setting in Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=398
        """
        print "starting testcase 398"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #Type sub-text in the video, then wait stay on Step-1 screen
        widget.transcribe_video(self, sel, subtextfile, step="Stop",buffer="yes")
        #verify that playback continues to the end
        while int(sel.get_element_width("css=.mirosubs-played")) != 250:
            self.failIf(sel.is_element_present(testvars.WidgetUI["Video_play_button"]))
            time.sleep(2)




    def test_399(self):
        """
        Tests Play - Pause functionality in Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=399
        """
        print "starting testcase 399"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        # wait for video to load
        mslib.wait_for_video_to_buffer(self,sel)
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        #play-pause with screen button
        print "play-pause with screen button"
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with unicode tab char
        print "play-pause with keyboard"
        sel.type_keys("//div/input",'\t')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.type_keys("//div/input",'\t')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with Video play-pause button
        print "play-pause with on-video button"
        sel.click(testvars.WidgetUI["Video_play_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Video_pause_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
          
                         
        

    def test_403(self):
        """
        Tests Play - Pause functionality in Step 2 Syncing
        http://litmus.pculture.org/show_test.cgi?id=403
        """
        print "starting testcase 403"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)

        #on Step 2 test play-pause button
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        #play-pause with screen button
        print "play-pause with screen button"
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with unicode tab char
        print "play-pause with keyboard"
        sel.type_keys("css=.mirosubs-play",u'\u0009')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.type_keys("css=.mirosubs-play",u'\u0009')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with Video play-pause button
        print "play-pause with on-video button"
        sel.click(testvars.WidgetUI["Video_play_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Video_pause_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        


    def test_404(self):
        """
        Tests Play - Pause functionality in Step 3 Review
        http://litmus.pculture.org/show_test.cgi?id=404
        """
        print "starting testcase 404"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)

        #on Step 3 test play-pause button
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        #play-pause with screen button
        print "play-pause with screen button"
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with unicode tab char
        print "play-pause with keyboard"
        sel.type_keys("css=.mirosubs-play",u'\u0009')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.type_keys("css=.mirosubs-play",u'\u0009')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with Video play-pause button
        print "play-pause with on-video button"
        sel.click(testvars.WidgetUI["Video_play_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Video_pause_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])        
                         
        

    def test_400(self):
        """
        Tests Skip Back (ctrl) functionality in Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=400
        """
        print "starting testcase 400 - shift-tab to skip back on step 1"
        print "known bug: http://bugzilla.pculture.org/show_bug.cgi?id=14292"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #set mode to expert and wait for video to load
        mode_label = sel.get_text("css=.mirosubs-speedmode option:contains('Expert')")
        sel.select("//select", "label=" +mode_label)
        mslib.wait_for_video_to_buffer(self,sel)
        # start playback
        sel.click(testvars.WidgetUI["Play_pause"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        # wait for play to advance and test with screen button
        time.sleep(7)
        for x in range(0,3):  
            # get the time, skip back and get the time again
            start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            sel.click_at(testvars.WidgetUI["Skip_back"],"")
            time.sleep(.50)
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(start_time) - int(stop_time)
            if diff_time < 6:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
            time.sleep(10)
        # wait for play to advance and test with keyboard key
        # get the time, skip back and get the time again
        start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
        sel.shift_key_down()
        sel.type_keys("//div/input",'\t')
        sel.shift_key_up()
        time.sleep(.20)
        stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
        diff_time = int(start_time) - int(stop_time)
        if diff_time < 6:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
        



    def test_409(self):
        """
        Tests Skip Back (ctrl) functionality in Step 2 Sync
        http://litmus.pculture.org/show_test.cgi?id=409
        """
        print "starting testcase 409 shift-tab to sktip back step 2"
        print "known bug: http://bugzilla.pculture.org/show_bug.cgi?id=14292"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #step 1 type the subs
        widget.transcribe_video(self, sel, subtextfile,buffer="yes")
        # on step 2 test skip back
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
        sel.click(testvars.WidgetUI["Play_pause"])
        # wait for play to advance and test with screen button
        time.sleep(9)
        for x in range(0,3):  
            # get the time, skip back and get the time again
            start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            sel.click_at(testvars.WidgetUI["Skip_back"],"")
            time.sleep(.50)
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(start_time) - int(stop_time)
            if diff_time < 6:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
            time.sleep(10)
        # wait for play to advance and test with keyboard key
        # get the time, skip back and get the time again
        start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
        sel.shift_key_down()
        sel.type_keys("css=.mirosubs-right",'\t')
        sel.shift_key_up()
        time.sleep(.20)
        stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
        diff_time = int(start_time) - int(stop_time)
        if diff_time < 6:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time



    def test_410(self):
        """
        Tests Skip Back (ctrl) functionality in Step 3 Review
        http://litmus.pculture.org/show_test.cgi?id=410
        """
        print "starting testcase 410"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        #start sub widget
        website.start_sub_widget(self,sel)
        #complete step 1 typing
        widget.transcribe_video(self, sel, subtextfile, buffer="yes")
        #complete step 2 syncing
        widget.sync_video(self,sel,subtextfile,step="Stop")
        #on step 3 test ctrl to skip back        
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Play_pause"])
        sel.click(testvars.WidgetUI["Play_pause"])
        # wait for play to advance and test with screen button
        time.sleep(7)
        for x in range(0,3):  
            # get the time, skip back and get the time again
            start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            sel.click_at(testvars.WidgetUI["Skip_back"],"")
            time.sleep(.50)
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(start_time) - int(stop_time)
            if diff_time < 6:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
            time.sleep(10)
        # wait for play to advance and test with keyboard key
        # get the time, skip back and get the time again
        start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
        sel.shift_key_down()
        sel.type_keys("css=.mirosubs-right",'\t')
        sel.shift_key_up()
        time.sleep(.20)
        stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
        diff_time = int(start_time) - int(stop_time)
        if diff_time < 6:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time


    def test_406(self):
        """
        Tests Restart Typing link in Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=406
        """
        print "starting testcase 406"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile, step="Stop")
        widget.restart_step(self,sel)
        self.failIf(sel.is_element_present("css=.mirosubs-title-notime"))
                

       
    def test_401(self):
        """
        Tests Login link functionality in Step 1 Typing
        http://litmus.pculture.org/show_test.cgi?id=400
        """
        print "starting testcase 401"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile, step="Stop")
        widget.site_login_from_widget_link(self,sel)
        #verify subs still present
        print "verifying subtitles are still present"
        sel.select_window("null")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
        widget.verify_sub_text(self,sel,subtextfile)


    def test_405(self):
        """ 
	Tests Login Link functionality in Step 2 Sync 
        http://litmus.pculture.org/show_test.cgi?id=405
        """
        print "starting testcase 405"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self, sel, subtextfile, step="Stop")
        widget.site_login_from_widget_link(self,sel)
        #verify subs still present
        print "verifying subtitles are still present"
        sel.select_window("null")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
        widget.verify_sub_text(self,sel,subtextfile)



    def test_416(self):
        """
        Tests Login Link functionality in Step 3 Sync
        http://litmus.pculture.org/show_test.cgi?id=416
        """
        print "starting testcase 416"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self, sel, subtextfile)
        widget.site_login_from_widget_link(self,sel)
        #verify subs still present
        print "verifying subtitles are still present"
        sel.select_window("null")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
        widget.verify_sub_text(self,sel,subtextfile)


    def test_411(self):
        """
        Tests Subtitle Syncing in Step 2 Sync
        http://litmus.pculture.org/show_test.cgi?id=411
        """
        print "starting testcase 411"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,step="Stop")                
            
                

    def test_388(self):
        """
        Tests Edit Subtitles text in Step 2 Sync
        Tests smalls, caps, spaces, and non-ascii chars
        http://litmus.pculture.org/show_test.cgi?id=388
        """
        print "starting testcase 388"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,step="Stop")
                       
        #edit subtitles
        print "verifying subtitles are still present"
        widget.edit_text(self,sel,subtextfile)
        # make it french
        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_fr)
        #make it japanese
        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_jp)



    def test_415(self):
        """
        Tests Edit Subtitles in Step 3 Review
        http://litmus.pculture.org/show_test.cgi?id=415
        """
        print "starting testcase 415"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)                
        #edit subtitles
        print "editing subtitles"
        widget.edit_text(self,sel,subtextfile)
        # make it french
        print "french"
        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_fr)
        #make it japanese
        print "japanese"
        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_jp)



    def test_408(self):
        """
        Tests Back To Typing link in Step 2 Sync
        http://litmus.pculture.org/show_test.cgi?id=408
        """
        print "starting testcase 408"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        # start demo and proceed to step 2 and sync subs
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,step="Stop")
        # go back to typing step
        widget.back_step(self,sel)
        # verify step 1 display and subs
        widget.steps_display(self,sel,1)
        widget.verify_sub_text(self,sel,subtextfile)     


        
    def test_402(self):
        """
        Tests Down Arrow to  resync in Step 3 Review
        http://litmus.pculture.org/show_test.cgi?id=402
        """
        print "starting testcase 402"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)
        #on Step 3 resync video times
        widget.resync_video(self,sel,subtextfile)       


##    FIX ME - issues w/ the drag n drop part, commenting out for now.
        
##    def test_413(self):
##        """
##        Tests modifying times by dragging the timeline bubbles
##        http://litmus.pculture.org/show_test.cgi?id=413
##        """
##        print "starting testcase 413"
##        sel = self.selenium
##        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
##        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
##        # be sure logged out
##        website.SiteLogout(self,sel)
##        website.start_demo(self,sel)
##        website.start_sub_widget(self,sel)
##        widget.transcribe_video(self, sel, subtextfile)
##        widget.sync_video(self,sel,subtextfile,start_delay=1, sub_int=1)
##        #on Step 3 resync video times
##        widget.drag_time_bubbles(self,sel,subtextfile)       
                         
        

    def test_414(self):
        """
        Tests modifying times by click the arrows that appear on
        mouseover on Step 3 Review
        http://litmus.pculture.org/show_test.cgi?id=414
        """
        print "starting testcase 414"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)
        #on Step 3 resync video times
        widget.click_time_shift_arrows(self,sel,subtextfile)       


##    
##    def test_412(self):
##        """
##        Tests modifying times by holding down then releasing down arrow
##        on Step 3 Review
##        http://litmus.pculture.org/show_test.cgi?id=412
##        """
##        print "starting testcase 412"
##        sel = self.selenium
##        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
##        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"switch-to-firefox.txt")
##        # be sure logged out
##        website.SiteLogout(self,sel)
##        website.start_demo(self,sel)
##        website.start_sub_widget(self,sel)
##        widget.transcribe_video(self, sel, subtextfile,buffer="yes")
##        widget.sync_video(self,sel,subtextfile,start_delay=5, sub_int=2)
##        #on Step 3 resync video times
##        widget.hold_down_delay_sub(self,sel,subtextfile)       
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
