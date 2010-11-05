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


class subgroup_78(unittest.TestCase):
    """
    Litmus Subgroup 64 - offsite subwidget:
        Tests designed to exercise the subtitle widget embedded
        in sites external to universalsubtitles.org (live, dev or staging)  
    """
    
# Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = (selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), "http://pculture.org/"))
        self.selenium.start()
   
# The test cases of the subgroup.


    def test_369(self):
        """Subtitle Youtube video in offsite embed.
        
        http://litmus.pculture.org/show_test.cgi?id=369
        """
        print "starting 369 youtube widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_widget_null_page())
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,6,8)
        # Review
        widget.edit_text(self,sel,subtextfile)

      

    def test_370(self):
        """Subtitle ogg video in offsite embed.
       
        http://litmus.pculture.org/show_test.cgi?id=370
        """
        print "starting 370 - ogg widget test"
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        sel.open(selvars.set_widget_null_page())
        mslib.wait_for_element_present(self,sel,"css=.left_column span.mirosubs-tabTextchoose")
        website.start_sub_widget(self,sel,"css=.left_column span.mirosubs-tabTextchoose")

        # Transcribe
        widget.transcribe_video(self,sel,subtextfile)
        # Sync
        widget.sync_video(self,sel,subtextfile,5,5)
        # Review
        widget.edit_text(self,sel,subtextfile)




# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        # check for Site Error notification and submit
        website.handle_error_page(self,self.selenium,self.id())
        #Close the browser
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
      


if __name__ == "__main__":
    unittest.main()

 
