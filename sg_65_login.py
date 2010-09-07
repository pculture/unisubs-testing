from selenium import selenium
import unittest
import time
import mslib
import website
import widget
import offsite
import testvars


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
        self.selenium = selenium(testvars.vlocalhost, 4444, testvars.vbrowser, testvars.MSTestVariables["Site"])
        self.selenium.start()
        
    # The tests in the subgroup
    def test_378(self):
        """
        Site_login
        http://litmus.pculture.org/show_test.cgi?id=378
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
        """
        Twitter login from site
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
        """
        Open id login from site
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
        """
        Gmail login from site
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
        """
        Gmail login from widget
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
        time.sleep(10)
        sel.select_window("null")
        sel.refresh()
        website.verify_login(self,sel,testvars.gmailuser)
        # logout
        website.SiteLogout(self,sel)


    def test_383(self):
        """
        Twitter login from widget
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
        time.sleep(10)
        sel.select_window("null")
        sel.refresh()
        website.verify_login(self,sel,username="PCF Sub-writer")
        # logout
        website.SiteLogout(self,sel)


    def test_384(self):
        """
        Site login from site
        http://litmus.pculture.org/show_test.cgi?id=384
        """
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        website.SiteLogout(self,sel)
        website.start_demo(self,sel)
        widget.Login(self,sel,"log")
        sel.select_pop_up("null")
        mslib.wait_for_element_present(self,sel,"id_username")
        sel.type("id_username", testvars.siteuser)
        sel.type("id_password", testvars.passw)
        sel.click("//button[@value='login']")
        # verify
        time.sleep(10)
        sel.select_window("null")
        sel.refresh()
        website.verify_login(self,sel,testvars.siteuser)
        # logout
        website.SiteLogout(self,sel)



    def test_385(self):
        """
        Open id login from widget
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
        
        time.sleep(10)
        sel.select_window("null")
        sel.refresh()
        website.verify_login(self,sel,testvars.openiduser)
        # logout
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
