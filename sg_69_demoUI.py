# Litmus Subgroup 65 - Login / Logout Tests
#389 How-to video continue
#395 How-to video skip
#373 Step 1 Typing the subs
#397 Step 1 Beginner mode
#470 Step 1 Advanced mode
#398 Step 1 Expert mode
#399 Step 1 Play-Pause tab + button
#403 Step 2 Play-Pause tab + button
#404 Step 3 Play-Pause tab + button
#400 Step 1 Skip back (button only)
#409 Step 2 Skip back (button only)
#410 Step 3 Skip back (button only)
#406 Step 1 Restart typing
#401 Step 1 Login
#405 Step 2 Login
#416 Step 3 Login
#411 Step 2 Sync
#388 Step 2 Edit sub text (caps,smalls, non-ascii)
#415 Step 3 Edit sub text (caps, smalls, non-ascii)
#408 Step 2 back to typing
#402 Step 3 Down to Sync
#413 Step 3 Drag sub bubbles
#414 Step 3 Text time arrows
#412 Step 3 Hold down to delay sub start


from selenium import selenium
import unittest, time, re, sys, codecs
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class tc_389(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_how_to_video_continue(self):
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
                                       
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_395(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_how_to_video_skip(self):
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
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



class tc_373(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_typing_subs(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        # verify subs present on next screen                    
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_397(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_beginner_mode(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
            if not  7 < diff_time < 9:
                mslib.AppendErrorMessage(self,sel,"didn't stop after 8 seconds")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
        
        
        # verify subs present on next screen
        widget.verify_sub_text(self,sel,subtextfile)
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



class tc_470(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_advanced_mode(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
            time.sleep(.5)    
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_398(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_expert_mode(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        #Type sub-text in the video, then wait stay on Step-1 screen
        widget.transcribe_video(self, sel, subtextfile, step="Stop",buffer="yes")
        #verify that playback continues to the end
        while int(sel.get_element_width("css=.mirosubs-played")) != 250:
            self.failIf(sel.is_element_present(testvars.WidgetUI["Video_play_button"]))
            
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_399(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_tab_playpause(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
        sel.type_keys("//div/input",u'\u0009')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.type_keys("//div/input",u'\u0009')
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
        time.sleep(3)
        #play-pause with Video play-pause button
        print "play-pause with on-video button"
        sel.click(testvars.WidgetUI["Video_play_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
        time.sleep(3)
        sel.click(testvars.WidgetUI["Video_pause_button"])
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
          
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_403(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_tab_playpause(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_404(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_tab_playpause(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_400(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_skip_back(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
            time.sleep(.20)
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(start_time) - int(stop_time)
            if diff_time < 7:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
            time.sleep(10)
## Commented out keyboard control b/c ctrl key not working in selenium
##        # wait for play to advance and test with keyboard key
##        time.sleep(14)
##        # get the time, skip back and get the time again
##        start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
##        sel.control_key_down()
##        sel.control_key_up()
##        time.sleep(.20)
##        stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
##        diff_time = int(start_time) - int(stop_time)
##        if diff_time < 7:
##            mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
##            print "started at: " +start_time+ "stopped at: " +stop_time
##            print diff_time
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_409(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_skip_back(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
            time.sleep(.20)
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(start_time) - int(stop_time)
            if diff_time < 7:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
            time.sleep(10)
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_410(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_skip_back(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
            time.sleep(.20)
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(start_time) - int(stop_time)
            if diff_time < 7:
                mslib.AppendErrorMessage(self,sel,"didn't jump back quickly")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
            time.sleep(10)
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)




class tc_406(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step1_restart_typing(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile, step="Stop")
        widget.restart_typing(self,sel)
        self.failIf(sel.is_element_present("css=.mirosubs-title-notime"))
                
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_401(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario

       
    def test_step1_login(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)




class tc_405(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_login(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_416(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_login(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_411(unittest.TestCase):
    
# Open the desired browser and set up the test
 # Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost,4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_sync(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile,step="Stop")                
            
                
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)
            
                
class tc_388(unittest.TestCase):
    
# Open the desired browser and set up the test
 # Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost,4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_edit_subs(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
        sel.capture_screenshot(testvars.MSTestVariables["ResultOutputDirectory"]+"tc_388_eels_fr.png")
        #make it japanese
        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_jp)
        sel.capture_screenshot(testvars.MSTestVariables["ResultOutputDirectory"]+"tc_388_eels_jp.png")
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



class tc_415(unittest.TestCase):
    
# Open the desired browser and set up the test
 # Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost,4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_edit_subs(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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
        sel.capture_screenshot(testvars.MSTestVariables["ResultOutputDirectory"]+"tc_415_eels_fr.png")
        #make it japanese
        print "japanese"
        widget.edit_text(self,sel,subtextfile,new_text=testvars.eels_jp)
        sel.capture_screenshot(testvars.MSTestVariables["ResultOutputDirectory"]+"tc_415_eels_jp.png")
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



class tc_408(unittest.TestCase):
    
# Open the desired browser and set up the test
 # Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost,4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step2_back_to_typing(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
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

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


        

class tc_402(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_down_resync(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)

        #on Step 3 resync video times
        widget.resync_video(self,sel,subtextfile)       
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)      



class tc_413(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_drag_time_bubbles(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)

        #on Step 3 resync video times
        widget.drag_time_bubbles(self,sel,subtextfile)       
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)




class tc_414(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_text_time_arrows(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile)
        widget.sync_video(self,sel,subtextfile)

        #on Step 3 resync video times
        widget.click_time_shift_arrows(self,sel,subtextfile)       
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_412(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_step3_hold_down_delay_start(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        subtextfile = testvars.MSTestVariables["DataDirectory"]+"switch-to-firefox.txt"
        # be sure logged out
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)
        widget.transcribe_video(self, sel, subtextfile,buffer="yes")
        widget.sync_video(self,sel,subtextfile,start_delay=6, sub_int=3)
        #on Step 3 resync video times
        widget.hold_down_delay_sub(self,sel,subtextfile)       
                         
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
