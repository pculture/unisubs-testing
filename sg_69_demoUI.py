# Litmus Subgroup 65 - Login / Logout Tests
#389 How-to video continue
#395 How-to video skip
#373 Step 1 Typing the subs
#397 Step 1 Beginner mode
#470 Step 1 Advanced mode
#398 Step 1 Expert mode
#399 Step 1 Play-Pause tab + button
#400 Step 1 Skip back (button only)
#406 Step 1 Restart typing
#401 Step 1 Login
#
#
#
#
#


from selenium import selenium
import unittest, time, re, sys, codecs
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class tc_389(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        widget.transcribe_video(self,sel,subtextfile,mode="Beginner", step="Stop")
        # wait for play button to indicate playback was paused, then start playback and see if it auto-stops
        for x in range(0,2):
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
            start_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            sel.click(testvars.WidgetUI["Video_play_button"])
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_play_button"])
            stop_time = sel.get_text(testvars.WidgetUI["Video_elapsed_time"])
            diff_time = int(stop_time) - int(start_time)
            if diff_time != 8:
                mslib.AppendErrorMessage(self,sel,"didn't stop after 8 seconds")
                print "started at: " +start_time+ "stopped at: " +stop_time
                print diff_time
        
        
        # verify subs present on next screen                    
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



class tc_470(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
            
        
        # verify subs present on next screen                    
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_398(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        widget.transcribe_video(self, sel, subtextfile, step="Stop")
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
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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


class tc_400(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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


class tc_406(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        self.failIf(sel.is_element_present("css=.mirosubs-titlesList li"))
                
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_401(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
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
        mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Must_Login"])
                
        print "loggin in from widget"
        sel.click("link=LOGIN")
        sel.select_frame("relative=top")
        auth_type = "log"
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-"+auth_type)
        sel.click("css=.mirosubs-"+auth_type)
        sel.select_pop_up("null")
        mslib.wait_for_element_present(self,sel,"id_username")
        sel.type("id_username", testvars.siteuser)
        sel.type("id_password", testvars.passw)
        sel.click("//button[@value='login']")
        #wait for the login to complete
        time.sleep(10)

        
        #verify subs still present
        print "verifying subtitles are still present"
        sel.select_window("null")
        mslib.wait_for_element_present(self,sel,"css=.mirosubs-titlesList")
        sub_index=1
        for line in open(subtextfile):
            current_sub = sel.get_text("css=.mirosubs-titlesList li:nth-child("+str(sub_index)+")")
            if line.rstrip() != current_sub.rstrip():
                mslib.AppendErrorMessage(self,sel,"sub text mismatch")
                print "found: " + current_sub.rstrip()
                print "expected: " +line
            sub_index = sub_index + 1
            
                
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()
