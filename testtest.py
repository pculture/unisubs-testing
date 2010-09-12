from selenium import selenium
import unittest
import os
import time
import re
import sys
import codecs
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class testtest(unittest.TestCase):
    """
    
    412 Step 3 Hold down to delay sub start
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()

    def test_376(self):
        """Test demo widget not logged in
        http://litmus.pculture.org/show_test.cgi?id=376
        """
        print "starting 376 demo forced login"
        
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)        
        # Check message in transcribe step
        widget.verify_login_message(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        
        # Check message in sync step
        widget.verify_login_message(self,sel)
        widget.sync_video(self,sel,subtextfile,2,2)

        # Check message in review step and click done
        widget.verify_login_message(self,sel)
        sel.click(testvars.WidgetUI["Next_step"])
        self.failUnless(sel.is_element_present("css=.mirosubs-modal-login"))
        sel.click("css=.mirosubs-log")
        #Login
        widget.site_login_auth(self,sel)
        sel.select_window("null")
        self.failUnless(sel.is_element_present(testvars.WidgetUI["Next_step"]))
        sel.click(testvars.WidgetUI["Next_step"])
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        self.failUnless(sel.is_text_present("Subtitles saved!"))
        self.failUnless(sel.is_element_present("css=div#languages-tab"))
        #Finish up by logging out
        print "logging out from site"
        website.SiteLogout(self,sel)
       
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
  #      self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
