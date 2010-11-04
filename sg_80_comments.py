from selenium import selenium
import unittest
import sys
import mslib
import website
import widget
import testvars
import selvars
import comments_text

class subgroup_80(unittest.TestCase):
    """Comments tests.
    
        Tests designed to verify adding comments to original lang
        and translated lang of videos
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


    def test_487(self):
        """Add comments on original language
        
        http://litmus.pculture.org/show_test.cgi?id=487
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])

        #get a video and open page    
        website.SiteLogout(self,sel)
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        #Open the Original is the default tab when  video opened.
        sel.click(testvars.comments_tab)
        #Not logged in, enter a comment
        print "1. trying to enter a comment when not logged in"
        ctext = "this comment should never post"
        website.enter_comment_text(self,sel,ctext)
        website.verify_comment_text(self,sel,ctext, result="login")
        #Login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        sel.open(test_video_url)
        sel.click(testvars.comments_tab)
        #Enter a 1-char comment
        print "2. entering a 1-char comment on original"
        website.enter_comment_text(self,sel,"d")
        website.verify_comment_text(self,sel,"d")
        #Enter a normal comment
        print "3. entering a normal comment on original"
        website.enter_comment_text(self,sel,comments_text.normal_comment_text)
        website.verify_comment_text(self,sel,comments_text.normal_comment_text)
        print "4. entering a too-long comment on original"
        #Enter a too long comment
        website.enter_comment_text(self,sel,comments_text.normal_comment_text * 10)
        website.verify_comment_text(self,sel,comments_text.normal_comment_text, result="too long")

    def test_536(self):
        """Add comments on Video Info tab
        
        http://litmus.pculture.org/show_test.cgi?id=536
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #get a video and open page    
        website.SiteLogout(self,sel)
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        sel.click(testvars.video_video_info)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        sel.click(testvars.comments_tab)
        #Open the Original tab / then comments tab
        self.assertTrue(sel.get_text("css=li.active:contains('Video Info')"),"Video Info is not the active tab")
        #Not logged in, enter a comment
        print "1. trying to enter a comment when not logged in"
        ctext = "this comment should never post"
        website.enter_comment_text(self,sel,ctext)
        website.verify_comment_text(self,sel,ctext, result="login")
        #Login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        sel.open(test_video_url)
        sel.click(testvars.video_video_info)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        sel.click(testvars.comments_tab)
        #Enter a 1-char comment
        print "2. entering a 1-char comment on Video Info"
        website.enter_comment_text(self,sel,"d")
        website.verify_comment_text(self,sel,"d")
        #Enter a normal comment
        print "3. entering a normal comment on Video Info"
        website.enter_comment_text(self,sel,comments_text.normal_comment_text)
        website.verify_comment_text(self,sel,comments_text.normal_comment_text)
        print "4. entering a too-long comment on Video Info"
        #Enter a too long comment
        website.enter_comment_text(self,sel,comments_text.normal_comment_text * 10)
        website.verify_comment_text(self,sel,comments_text.normal_comment_text, result="too long")



    def test_488(self):
        """Add comments on a translation
        
        http://litmus.pculture.org/show_test.cgi?id=488
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #get a video and open page      
        website.SiteLogout(self,sel)
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        language = website.get_translated_lang(self,sel)
        
        #Open the Language tab / then the comments
        sel.click("link="+language)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        self.failUnless(sel.is_element_present("css=h4.inline:contains("+language+")"))
        sel.click(testvars.comments_tab) 

        #Not logged in, enter a comment
        print "1. trying to enter a comment when not logged in"
        ctext = "this comment should never post"
        website.enter_comment_text(self,sel,ctext)
        website.verify_comment_text(self,sel,ctext, result="login")
        #Login and go to language comments page
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        sel.open(test_video_url)
        sel.click("link="+language)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        self.failUnless(sel.is_element_present("css=h4.inline:contains("+language+")"))
        sel.click(testvars.comments_tab) 

        #Enter a 1-char comment
        print "2. entering a 1-char comment on Video Info"
        website.enter_comment_text(self,sel,"d")
        website.verify_comment_text(self,sel,"d")
        #Enter a normal comment
        print "3. entering a normal comment on Video Info"
        website.enter_comment_text(self,sel,comments_text.normal_comment_text)
        website.verify_comment_text(self,sel,comments_text.normal_comment_text)
        print "4. entering a too-long comment on Video Info"
        #Enter a too long comment
        website.enter_comment_text(self,sel,comments_text.normal_comment_text * 10)
        website.verify_comment_text(self,sel,comments_text.normal_comment_text, result="too long")


    def test_537(self):
        """Add comments on a translation using non-ascii characters
        
        http://litmus.pculture.org/show_test.cgi?id=537
        """
        
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #get a video and open page      
        website.SiteLogout(self,sel)
        test_video_url = website.get_video_with_translations(self,sel)
        print test_video_url
        sel.open(test_video_url)
        language = website.get_translated_lang(self,sel)
        
        
        #Login and go to language comments page
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        sel.open(test_video_url)
        sel.click("link="+language)
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        self.assertTrue(sel.is_element_present("css=h4.inline:contains("+language+")"))
        sel.click(testvars.comments_tab) 

        #Enter some non-ascii comments
        print "1. entering croatian comment text"
        website.enter_comment_text(self,sel,comments_text.hr_comment_text)
        website.verify_comment_text(self,sel,comments_text.hr_comment_text)
        print "2. entering japanese comment text"
        website.enter_comment_text(self,sel,comments_text.jp_comment_text)
        website.verify_comment_text(self,sel,comments_text.jp_comment_text)
        print "3. entering russian comment text"
        website.enter_comment_text(self,sel,comments_text.ru_comment_text)
        website.verify_comment_text(self,sel,comments_text.ru_comment_text)



# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        # check for Site Error notification and submit
        website.handle_error_page(self,self.selenium,self.id())
        """
        Closes the browser test window and logs errors
        """
        #Close the browser
        self.selenium.close()
        self.selenium.stop()
        #Log any errors
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":

    unittest.main()

  


 
