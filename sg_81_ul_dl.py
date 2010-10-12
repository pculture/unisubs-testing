from selenium import selenium
import unittest
import sys
import os
import mslib
import website
import widget
import testvars
import selvars





class subgroup_81(unittest.TestCase):
    """
    Litmus Subgroup 81 - upload / download subtitles:
        Tests designed verify the upload of subtitle formats
        previously downloaded from the subs website.
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        print "starting testcase "+self.id()+": "+self.shortDescription()
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site()))
        self.selenium.start()
   
# The test cases of the subgroup.


    def test_508(self):
        """Upload subtitle files as the original language.
        
        http://litmus.pculture.org/show_test.cgi?id=508
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        
        #get a video and open page
        sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.ssa")
        sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.txt")
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        test_video_url = website.get_video_no_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        #Open the Original is the default tab when  video opened.
        website.upload_subtitles(self,sel,sub_file)
        website.verify_sub_upload(self,sel,sub_text)

   



# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        # check for Site Error notification and submit
        website.handle_error_page(self,self.selenium,self.id())
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
  #      self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":

    unittest.main()

  


 
