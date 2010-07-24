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

## ----------------------------------------------------------------------


class tc_378(unittest.TestCase):
    
# Open the desired browser and set up the test
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, testvars.MSTestVariables["Browser"], testvars.MSTestVariables["Site"])
        self.selenium.start()

# The user actions executed in the test scenario
    def test_site_login(self):
        sel = self.selenium
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.SiteLogIn(self,sel,testvars.siteuser,testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.Login(self,sel,"twitter")
        offsite.TwitterAuth(self,sel,testvars.twitteruser, testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login        
        sel.open(testvars.MSTestVariables["Site"])
        website.Login(self,sel,"open-id")
        offsite.OpenIdAuth(self,sel,testvars.openiduser,testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.Login(self,sel,"google")
        offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.start_demo(self,sel)
        widget.Login(self,sel,"google")
        offsite.GmailAuth(self,sel,testvars.gmailuser,testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.start_demo(self,sel)
        widget.Login(self,sel,"twitter")
        offsite.TwitterAuth(self,sel,testvars.twitteruser,testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.start_demo(self,sel)
        widget.Login(self,sel,"log")
        sel.select_pop_up("null")
        mslib.wait_for_element_present(self,sel,"id_username")
        sel.type("id_username", testvars.siteuser)
        sel.type("id_password", testvars.passw)
        sel.click("//button[@value='login']")
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
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
        sel.set_timeout(testvars.MSTestVariables["TimeOut"])
        #login
        sel.open(testvars.MSTestVariables["Site"])
        website.start_demo(self,sel)
        widget.Login(self,sel,"openid")
        offsite.OpenIdAuth(self,sel,testvars.openiduser,testvars.passw)
        # verify
        website.verify_login(self,sel)
        # logout
        sel.open(testvars.MSTestVariables["Site"] +"logout/")
# Close the browser, log errors, perform cleanup 
    def tearDown(self):
        self.selenium.stop()
# the command on the previous line should close the browser
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
