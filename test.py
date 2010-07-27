# test sandbox

from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, offsite, testvars

#----------------------------------------------------------------------


class tc_406(unittest.TestCase):
    
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
