from selenium import selenium
import unittest
import time
import os
import logging
import mslib
import website
import widget
import offsite
import testvars
import selvars
import litmusresult


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
        self.selenium = selenium(selvars.set_localhost(), selvars.set_port(), selvars.set_browser(self.id(),self.shortDescription()), selvars.set_site())
        self.selenium.start()
        self.session = self.selenium.sessionId
        if os.path.isfile("curr_test.log"):
            os.remove("curr_test.log")
        LOG_FILENAME = "curr_test.log"
        logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
        if selvars.set_sauce() == True:
            logging.info("sauce job result: http://saucelabs.com/jobs/"+str(self.session))
        else:
            logging.info("starting: " +self.id() +"-"+self.shortDescription())
        
        
    # The tests in the subgroup
    def test_378(self):
        """Site login using site account.

        http://litmus.pculture.org/show_test.cgi?id=378.      
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # verify
        website.verify_login(self,sel,testvars.siteuser)
        # logout
        sel.open("logout/")


    def test_379(self):
        """Site login using twitter account.

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
        """Site login from open id account.
        
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
        website.verify_login(self,sel,testvars.openid-username) #cheat for bug #13688
        # logout
        website.SiteLogout(self,sel)



    def test_381(self):
        """Site login using gmail account.

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
        """Login from widget using gmail account.

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
        """Login from widget using twitter account

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
        """Login from widget using site account.
        
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
        """Login from widget using openid account.
        
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
        website.verify_login(self,sel,testvars.openid-username)
        # logout
        website.SiteLogout(self,sel)

      
        
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
