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
        self.session = self.selenium.sessionId


    def test_close(self):
        
        """Widget Step 3, click time arrows to modify time.
        
        http://litmus.pculture.org/show_test.cgi?id=414
        """
        print "starting testcase 414"
        sel = self.selenium
        sel.set_timeout(180000)
        # be sure logged out
        sel.open("/videos/teams")
        vid_url = offsite.get_youtube_video_url(self)
        
  
          
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
        self.selenium.sessionId = self.session
        print self.selenium.sessionId
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors) 


if __name__ == "__main__":
    unittest.main()
