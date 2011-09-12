from selenium import selenium
import unittest
import sys
import os
import time
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
        self.session = self.selenium.sessionId
   
# The test cases of the subgroup.


    def test_508(self):
        """Must login to upload subs
        
        http://litmus.pculture.org/show_test.cgi?id=508
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #get a video and open page
        test_video_url = website.submit_random_youtube(self,sel)
        print test_video_url
        vid = test_video_url.split("/")[-2]
        sel.open("en/logout/?next=/") #verify logged out.
        sel.open(test_video_url)
        #Original is the default tab when video opened.
        sel.click(testvars.video_upload_subtitles)
        mslib.wait_for_element_present(self,sel,"css=div.msg_modal")
        self.assertTrue(sel.is_element_present("css=div.msg_modal a:contains('Login')"))
        sel.click("css=div#upload_subs-div a.close")
  
    def test_507(self):
        """Invalid or unsupported formats
        
        http://litmus.pculture.org/show_test.cgi?id=507
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        try:
            #get a video and open page
            website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
            test_video_url = website.submit_random_youtube(self,sel)
            print test_video_url
            sel.open(test_video_url)
            #Original is the default tab when video opened.
            print "1. invalid ttml"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_fakesub.xml")
            website.upload_subtitles(self,sel,sub_file)
            mslib.wait_for_element_present(self,sel,"css=p.error_list")
            self.assertTrue(sel.is_element_present("css=p.error_list:contains('Can not detect file encoding')"))
            sel.click("css=a.close")
            
            print "2. invalid srt"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_invalid.srt")
            website.upload_subtitles(self,sel,sub_file)
            time.sleep(5)
            mslib.wait_for_element_present(self,sel,"css=p.error_list")
            self.assertTrue(sel.is_element_present("css=p.error_list:contains('Incorrect subtitles format')"))
            sel.click("css=a.close")
            
            print "3. unsupported format"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_text.txt")
            website.upload_subtitles(self,sel,sub_file)
            time.sleep(5)
            mslib.wait_for_element_present(self,sel,"css=p.error_list")
            self.assertTrue(sel.is_element_present("css=p.error_list:contains('Incorrect format.')"))
            sel.click("css=a.close")
            
        finally:
            # check for Site Error notification and submit
            website.handle_error_page(self,sel,self.id())
   
    def test_509(self):
        """Upload subtitle files ssa format.
        
        http://litmus.pculture.org/show_test.cgi?id=509
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        
        #get a video and open page
        try:
            website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
            test_video_url = website.submit_random_youtube(self,sel)
            print test_video_url
            sel.open(test_video_url)
            #Original is the default tab when video opened.
            print "1. english ssa upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.ssa")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.txt")
            website.upload_subtitles(self,sel,sub_file)
            website.verify_sub_upload(self,sel,sub_text)

            print "2. polish ssa upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.ssa")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="pl")
            website.verify_sub_upload(self,sel,sub_text, lang="Polish")

            print "3. arabic ssa upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.ssa")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="ar")
            website.verify_sub_upload(self,sel,sub_text, lang="Arabic")

            print "4. macedonian ssa upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.ssa")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="mk")
        #   website.verify_sub_upload(self,sel,sub_text, lang="Macedonian")
        finally:
            # check for Site Error notification and submit
            website.handle_error_page(self,sel,self.id())


    def test_510(self):
        """Upload subtitle files ttml format.
        
        http://litmus.pculture.org/show_test.cgi?id=510
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        
        #get a video and open page
        try:
            website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
            test_video_url = website.submit_random_youtube(self,sel)
            print test_video_url
            sel.open(test_video_url)
            #Original is the default tab when video opened.
            print "1. english ttml upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.xml")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.txt")
            website.upload_subtitles(self,sel,sub_file)
            website.verify_sub_upload(self,sel,sub_text)

            print "2. polish ttml upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.xml")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="pl")
            website.verify_sub_upload(self,sel,sub_text, lang="Polish")

            print "3. arabic ttml upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.xml")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="ar")
            website.verify_sub_upload(self,sel,sub_text, lang="Arabic")

            print "4. macedonian ttml upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.xml")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="mk")
            website.verify_sub_upload(self,sel,sub_text, lang="Macedonian")
        finally:
            # check for Site Error notification and submit
            website.handle_error_page(self,sel,self.id())


    def test_505(self):
        """Upload subtitle files srt format.
        
        http://litmus.pculture.org/show_test.cgi?id=505
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        
        #get a video and open page
        try:
            website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
            test_video_url = website.submit_random_youtube(self,sel)
            print test_video_url
            sel.open(test_video_url)
            #Original is the default tab when video opened.
        
            print "1. english srt upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.srt")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.txt")
            website.upload_subtitles(self,sel,sub_file)
            website.verify_sub_upload(self,sel,sub_text)

            print "2. polish srt upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.srt")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="pl")
            website.verify_sub_upload(self,sel,sub_text, lang="Polish")

            print "3. arabic srt upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.srt")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="ar")
            website.verify_sub_upload(self,sel,sub_text, lang="Arabic")

            print "4. macedonian srt upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.srt")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="mk")
            website.verify_sub_upload(self,sel,sub_text, lang="Macedonian")
        finally:
            # check for Site Error notification and submit
            website.handle_error_page(self,sel,self.id())

    def test_506(self):
        """Upload subtitle files sbv format.
        
        http://litmus.pculture.org/show_test.cgi?id=506
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        
        #get a video and open page
        try:
            website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
            test_video_url = website.submit_random_youtube(self,sel)
            print test_video_url
            sel.open(test_video_url)
      
            #Original is the default tab when video opened.
            print "1. english sbv upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.sbv")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_en_subs.txt")
            website.upload_subtitles(self,sel,sub_file)
            website.verify_sub_upload(self,sel,sub_text)

            print "2. polish sbv upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.sbv")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_pl_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="pl")
            website.verify_sub_upload(self,sel,sub_text, lang="Polish")

            print "3. arabic sbv upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.sbv")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_ar_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="ar")
            website.verify_sub_upload(self,sel,sub_text, lang="Arabic")

            print "4. macedonian sbv upload"
            sub_file = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.sbv")
            sub_text = os.path.join(testvars.MSTestVariables["DataDirectory"],"sg81_mk_subs.txt")
            website.upload_subtitles(self,sel,sub_file,lang="mk")
            website.verify_sub_upload(self,sel,sub_text, lang="Macedonian")
        finally:
            # check for Site Error notification and submit
            website.handle_error_page(self,sel,self.id())



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

  


 
