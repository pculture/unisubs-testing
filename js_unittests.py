import unittest
import time
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
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://dev.universalsubtitles.org")
        self.selenium.start()
        self.selenium.set_timeout(30000)
   
# The test cases of the subgroup.


    def test_videourlparse(self):

        sel = self.selenium
        sel.open("jstest/videourlparse_test/")
        for i in range(20):
            try:
                if sel.is_text_present("Done"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failIf(sel.is_text_present("FAILED"))


# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """       
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

  


 
