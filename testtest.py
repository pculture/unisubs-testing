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


class subgroup_test(unittest.TestCase):
    """Subgroup 69: Widget functionality tests using the site demo.

    Litmus Subgroup 69 - Demo Wiget UI tests
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        testid = self.id()
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://staging.universalsubtitles.org" )
        self.selenium.start()

# The test cases of the subgroup
    def test_409(self):
        """Widget Step 2, skip-back functionality.
        
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
            diff_time = float(start_time) - float(stop_time)
            self.failUnless(diff_time > 5,"screen button: jump back not ~8 seconds)
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
        self.failUnless(diff_time > 5,"screen button: jump back not ~8 seconds)
        

       


          
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
#        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
