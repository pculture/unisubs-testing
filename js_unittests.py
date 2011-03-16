import unittest
import time
import js_runvars
import mslib

from selenium import selenium

class js_unittest(unittest.TestCase):
    """
    run the js unittests
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        print "in setup"
        self.verificationErrors = []
        self.selenium = selenium(js_runvars.set_localhost(), js_runvars.set_port(), js_runvars.set_browser(), js_runvars.set_site())
        self.selenium.start()
        self.selenium.set_timeout(30000)
   
# The test cases of the subgroup.


    def test_videourlparse(self):
        print "running the test"
        sel = self.selenium
        if js_runvars.set_sauce() == True:
            print "running on sauce"
            browser_list = ("firefox", "iexplore", "safari", "opera")
            for x in browser_list:
                print x
                self.selenium = selenium(js_runvars.set_localhost(), js_runvars.set_port(), js_runvars.set_browser(x), js_runvars.set_site())
                self.selenium.start()
                ssel = self.selenium
                run_jsunittests(self,ssel)
        else:
            run_jsunittests(self,sel)



# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """       
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


def run_jsunittests(self,sel):
    sel.open("/en/jstest/alltests/")
    sel.click("parallel")
    sel.click("css=button:contains('Start')")
    time.sleep(15)
    for x in range(0,20):
        status = sel.get_text("css=.goog-testrunner-progress-summary")
        statlist = status.split()
        if int(statlist[0]) == int(statlist[2]): break
        time.sleep(1)
    print status
    if sel.is_text_present("FAILED"):
        error_text = status
        self.verificationErrors.append(error_text)
        


if __name__ == "__main__":
    unittest.main()

  


 
