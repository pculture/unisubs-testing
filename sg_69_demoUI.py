# Litmus Subgroup 65 - Login / Logout Tests
# 1. 389 How-to video continue
# 2. 395 How-to video skip
# 3. 

from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, offsite, testvars

## ----------------------------------------------------------------------


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
        website.start_sub_widget(self,sel,skip=True)
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
        website.start_sub_widget(self,sel,skip=True)
        widget.transcribe_video(self,sel,subtextfile)
        # verify subs present on next screen                    
        
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
