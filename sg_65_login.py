from selenium import selenium
import unittest
import time
import os
import mslib
import website
import widget
import offsite
import testvars
import selvars


class subgroup_65(unittest.TestCase):
    """
    Litmus Subgroup 65 - Login / Logout Tests
    Tests designed to test the various login / logout options and requirements.
    """
    
    # Open the desired browser and set up the test
    def setUp(self):
        """
        Sets up run envirnment for selenium server
        """
        self.verificationErrors = []
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.shortDescription()), selvars.set_site())
        self.selenium.start()
        
        
    # The tests in the subgroup
    def test_378(self):
        """378: Site login using site account.

        http://litmus.pculture.org/show_test.cgi?id=378.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # verify
        website.verify_login(self,sel,testvars.siteuser)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")


    def test_379(self):
        """379: Site login using twitter account.

        http://litmus.pculture.org/show_test.cgi?id=379
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        website.Login(self,sel,"twitter")
        offsite.TwitterAuth(self,sel,testvars.twitteruser, testvars.passw)
        # verify
        website.verify_login(self,sel,username="PCF Sub-writer")
        # logout
        website.SiteLogout(self,sel)

    

    def test_380(self):
        """380: Site login from open id account.
        
        http://litmus.pculture.org/show_test.cgi?id=380
        """
        print "this test will likely fail until bug #13688 (http://bugzilla.pculture.org/show_bug.cgi?id=13688) gets fixed"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login        
        website.SiteLogout(self,sel)
        website.Login(self,sel,"open-id")
        offsite.OpenIdAuth(self,sel,testvars.openiduser,testvars.passw)
        # verify
        website.verify_login(self,sel,testvars.openiduser)
        # logout
        website.SiteLogout(self,sel)



    def test_381(self):
        """381: Site login using gmail account.

        http://litmus.pculture.org/show_test.cgi?id=381
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        website.Login(self,sel,"google")
        offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
        # verify
        website.verify_login(self,sel,testvars.gmailuser)
        # logout
        website.SiteLogout(self,sel)



    def test_382(self):
        """382: Login from widget using gmail account.

        http://litmus.pculture.org/show_test.cgi?id=382
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        widget.Login(self,sel,"google")
        offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
        # verify
        widget.wait_for_offsite_login(self,sel)
        widget.close_widget(self,sel)
        website.verify_login(self,sel,testvars.gmailuser)
        # logout
        website.SiteLogout(self,sel)


    def test_383(self):
        """383: Login from widget using twitter account

        http://litmus.pculture.org/show_test.cgi?id=383
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        
        website.start_demo(self,sel)
        widget.Login(self,sel,"twitter")
        offsite.TwitterAuth(self,sel,testvars.twitteruser,testvars.passw)
        # verify
        widget.wait_for_offsite_login(self,sel)
        widget.close_widget(self,sel)
        website.verify_login(self,sel,username="PCF Sub-writer")
        # logout
        website.SiteLogout(self,sel)


    def test_384(self):
        """384: Login from widget using site account.
        
        http://litmus.pculture.org/show_test.cgi?id=384
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogIn(self,sel,testvars.siteuser, testvars.passw)
        # verify
        website.verify_login(self,sel,testvars.siteuser)
        # logout
        website.SiteLogout(self,sel)



    def test_385(self):
        """385: Login from widget using openid account.
        
        http://litmus.pculture.org/show_test.cgi?id=385
        """
        print "this test will likely fail until bug #13688 (http://bugzilla.pculture.org/show_bug.cgi?id=13688) gets fixed"
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        widget.Login(self,sel,"openid")
        offsite.OpenIdAuth(self,sel,testvars.openiduser,testvars.passw)
        # verify
        widget.wait_for_offsite_login(self,sel)
        widget.close_widget(self,sel)
        website.verify_login(self,sel,testvars.openiduser)
        # logout
        website.SiteLogout(self,sel)

      
    def test_376(self):
        """376: Widget requires login to submit subtitles.

        http://litmus.pculture.org/show_test.cgi?id=376 .

               
        """
        print "starting" +self.shortDescription()
        
        sel = self.selenium
        subtextfile = os.path.join(testvars.MSTestVariables["DataDirectory"],"OctopusGarden.txt")
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        website.start_sub_widget(self,sel)        
        # Check message in transcribe step
        widget.verify_login_message(self,sel)
        widget.transcribe_video(self,sel,subtextfile)
        
        # Check message in sync step
        widget.verify_login_message(self,sel)
        widget.sync_video(self,sel,subtextfile,2,2)

        # Check message in review step and click done
        widget.verify_login_message(self,sel)
        sel.click(testvars.WidgetUI["Next_step"])
        self.failUnless(sel.is_element_present("css=.mirosubs-modal-login"))
        sel.click("css=.mirosubs-log")
        #Login
        widget.site_login_auth(self,sel)
        sel.select_window("null")
        self.failUnless(sel.is_element_present(testvars.WidgetUI["Next_step"]))
        sel.click(testvars.WidgetUI["Next_step"])
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        mslib.wait_for_element_present(self,sel,testvars.WebsiteUI["SubtitleMe_menu"])
        self.failUnless(sel.is_text_present("Subtitles saved!"))
        self.failUnless(sel.is_element_present("css=div#languages-tab"))
        #Finish up by logging out
        print "logging out from site"
        website.SiteLogout(self,sel)

        
# Close the browser, log errors, perform cleanup
    def tearDown(self):
        """
        Clean up log erros and close the browser
        """
        #Close the browser
        self.selenium.stop()
        # log and errors
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
