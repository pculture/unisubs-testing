import unittest
import time
import subprocess

import selenium

class JavascriptUnitTests(unittest.TestCase):
    """
    run the js unittests
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
       
        self.verificationErrors = []
        self.selenium = selenium("localhost",4444,"firefox","http://dev.universalsubtitles.org")
        self.selenium.start()
        self.selenium.set_timeout(10000)
   
# The test cases of the subgroup.


    def test_parallel_js_tests(self):
        sel = self.selenium
        run_jsunittests(self, sel)

# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """       
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


def run_jsunittests(self, sel):
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

  


 
