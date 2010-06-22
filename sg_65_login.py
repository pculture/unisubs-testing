# Litmus Subgroup 65 - Login / Logout Tests
# 1. 378 Website Site Login
# 2. 379 Website Twitter Account
# 3. 380 Website Open ID
# 4. 381 Website Gmail
# 5. 382 Widget Gmail
# 6. 383 Widget Twitter Account
# 7. 384 Widget Site Login
# 8. 385 Widget Open ID



from selenium import selenium
import unittest, time, re, sys
import mslib, website, widget, offsite, testvars

# ----------------------------------------------------------------------


class tc_378(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_site_login(self):
        sel = self.selenium
        #login
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # verify
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.verifyLogIn(self,sel,testvars.siteuser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)



class tc_379(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_twitter_login(self):
        sel = self.selenium
        #login
        website.Login(self,sel,"twitter")
        offsite.TwitterAuth(self,sel,testvars.twitteruser, testvars.passw)
        # verify
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.verifyLogIn(self,sel,testvars.twitteruser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_380(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_openid_login(self):
        sel = self.selenium
        #login
        website.Login(self,sel,"open-id")
        offsite.OpenIdAuth(self,sel,testvars.openiduser,testvars.passw)
        # verify
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.verifyLogIn(self,sel,testvars.openiduser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_381(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_gmail_login(self):
        sel = self.selenium
        #login
        website.Login(self,sel,"gmail")
        offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
        # verify
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.verifyLogIn(self,sel,testvars.gmailuser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_382(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_gmail_widget_login(self):
        sel = self.selenium
        #login
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.Login(self,sel,"gmail")
        offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
        # verify
        widget.verifyLogIn(self,sel,testvars.gmailuser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_383(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_twitter_widget_login(self):
        sel = self.selenium
        #login
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.Login(self,sel,"twitter")
        offsite.GmailAuth(self,sel,testvars.twitteruser,testvars.passw)
        # verify
        widget.verifyLogIn(self,sel,testvars.twitteruser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


class tc_384(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_site_widget_login(self):
        sel = self.selenium
        #login
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.Login(self,sel,"log")
        sel.type("id_username", user)
        sel.type("id_password", passw)
        sel.click("//button[@value='login']")
        sel.wait_for_page_to_load(testvars.MSTestVariables["TimeOut"])
        website.GmailAuth(self,sel,testvars.siteuser,testvars.passw)
        # verify
        widget.verifyLogIn(self,sel,testvars.gmailuser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)

class tc_385(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_openid_widget_login(self):
        sel = self.selenium
        #login
        sel.open(testvars.MSTestVariables["Site"] + "demo/")
        widget.Login(self,sel,"openid")
        offsite.OpenIdAuth(self,sel,testvars.openiduser,testvars.passw)
        # verify
        widget.verifyLogIn(self,sel,testvars.openiduser) 
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
