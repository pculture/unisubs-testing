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

class subgroup_95(unittest.TestCase):
    """
    Litmus Subgroup 95 - watch page, videos/watch.
        Tests designed to watch page on the site
    """

    
    ##Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """      
        
        self.verificationErrors = []
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site() )
        self.selenium.start()
        self.session = self.selenium.sessionId

    ## The test cases of the subgroup.



    def test_729(self):
       """Feature a video.

        http://litmus.pculture.org/show_test.cgi?id=729
        """
       sel = self.selenium
       sel.set_timeout(testvars.MSTestVariables["TimeOut"])
       sel.open("/")

       print "submitting a youtube video"
       vid_url = offsite.get_youtube_video_url(self)
       # Submit Video
       print ("logging in and submitting video")
       valid_url = website.submit_video(self,sel,vid_url)
       if valid_url == False:
           print 'random vid submit failed, trying known good url'
           vid_url = 'http://www.youtube.com/watch?v=lVJVRywgmYM'
           website.submit_video(self,sel,vid_url)
       # Verify embed and player
       print ("verifying embed")
       website.verify_submitted_video(self,sel,vid_url,embed_type="youtube")
       mslib.wait_for_element_present(self,sel,"css=h2.main-title span.title-container")
       title = sel.get_text("css=h2.main-title span.title-container")
       website.feature_video(self,sel,action='Feature')
       sel.open("/videos/watch/featured")
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       mslib.wait_for_element_present(self,sel,"css=div.watch-page-content ul.video_list li a")
       self.failUnless(sel.is_text_present(title))
        #Unfeature it
       sel.open(test_vid_url)
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       sel.click(testvars.video_video_info)
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       website.feature_video(self,sel,action='Unfeature')
       time.sleep(5)
       print "Verifying unfeatured"
       sel.open("/videos/watch/featured")
       mslib.wait_for_element_present(self,sel,"css=div.watch-page-content ul.video_list li a")
       self.failIf(sel.is_text_present(title))
        
        


    def test_740(self):
       """Unfeature a video.
       
        http://litmus.pculture.org/show_test.cgi?id=740
        """



       sel = self.selenium
       sel.set_timeout(testvars.MSTestVariables["TimeOut"])

       #get a video and open page    
       website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
       test_vid_url = website.get_video_with_translations(self,sel)
       print test_vid_url
       #Feature it
       sel.open(test_vid_url)
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       sel.click(testvars.video_video_info)
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       title = sel.get_text("css=h2.main-title span.title-container")
       website.feature_video(self,sel,action='Feature')
       print "Verifying featured"
       sel.open("/videos/watch/featured/")
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       mslib.wait_for_element_present(self,sel,"css=div.watch-page-content ul.video_list li a")
       self.failUnless(sel.is_text_present(title))


       #Unfeature it
       sel.open(test_vid_url)
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       sel.click(testvars.video_video_info)
       sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
       website.feature_video(self,sel,action='Unfeature')
       time.sleep(5)
       print "Verifying unfeatured"
       sel.open("/videos/watch/featured")
       mslib.wait_for_element_present(self,sel,"css=div.watch-page-content ul.video_list li a")
       self.failIf(sel.is_text_present(title))


         
# Close the browser, log errors, perform cleanup
    def tearDown(self):
        """
        Closes the browser test window and logs errors
        """
        
        #give it back the session id in case it's lost it
        self.selenium.sessionId = self.session
        #Check for an error page, then close the browser
        try:
            website.handle_error_page(self,self.selenium,self.id())
        finally:
            self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)
      


if __name__ == "__main__":
    unittest.main()





 
