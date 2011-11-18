from selenium import selenium
import unittest
import time
import sys
import os
import mslib
import website
import widget
import offsite
import testvars
import selvars



class feedback_tab(unittest.TestCase):
    """
    Feedback tab, make sure the site feedback takes us where we need to, tenderapp
    
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """      
        self.verificationErrors = []
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site() )
        self.selenium.start()
        self.session = self.selenium.sessionId
        print "RUNNING"
        if selvars.set_sauce() == True:
            print "sauce job result: http://saucelabs.com/jobs/"+str(self.session)

## The test cases of the subgroup.

    def test_feedback_tab(self):
        """
        Make sure clicking the feedback tab will take us to the tenderapp, with the new tab

        For https://unisubs.sifterapp.com/projects/12298/issues/426162/comments
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open("/")
        
        sel.click(testvars.WebsiteUI["FeedBack_button"])
        last_window = sel.get_all_window_names()[-1]
        sel.select_window(last_window)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        
        loc  = sel.get_location()
        self.assertEqual(loc, "https://universalsubtitles.tenderapp.com/")
        
        
if __name__ == "__main__":
    unittest.main()
