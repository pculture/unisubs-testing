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

    def test_470(self):
        """Widget Step 1, advanced (recommended) mode setting.
        
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
        for x in range(0,4):
            while sel.is_element_present(testvars.WidgetUI["Video_pause_button"]):
                time.sleep(.2)
                sel.type_keys("//div/input","Hi ")
            # stop typing and wait for playback to resume (pause button present)
            stop_time = sel.get_text(testvars.WidgetUI['Video_elapsed_time'])
            sel.type_keys("//div/input", "I'm Asa Dotzler")
            widget.transcribe_enter_text(self,sel)
            mslib.wait_for_element_present(self,sel,testvars.WidgetUI["Video_pause_button"])
            resume_time = sel.get_text(testvars.WidgetUI['Video_elapsed_time'])
            self.assertNotAlmostEqual(float(stop_time),float(resume_time),"restarted at same position, no jump back")
        

       


          
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
