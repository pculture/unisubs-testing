#set browser for javascript tests

import js_testrunner as controller
import json
import sauce_auth



def set_sauce():
    if controller.testsauce==True:
        sauce = True
        return sauce
   


def set_localhost():
    """ localhost should default to 'localhost'.

    If we are runnign tests on sauce on-demand, then it
    needs to be the sauce url.
    """
    if controller.testsauce==True:
        localhost = "saucelabs.com"
    else:
        localhost = "localhost"
    return localhost

def set_port():
    """
    sets the value of port if specified at the cmdline
    """   
    if controller.testport:
        port = controller.testport    
    else:
        port = 4444
    return port

def set_site():
    """
    sets the value of test site if specified at the cmdline
    """   
    if controller.testsite:
        site = "http://"+controller.testsite+".universalsubtitles.org"
    else:
        site = "http://staging.universalsubtitles.org"
    return site


def set_browser(browser="firefox"):
    """Sets the browser for the test setup. If using sauce, need the correct sauce json string for the browser.

    """
    print "set_browser"
    if controller.testsauce == False:
        testbrowser = "*firefox"
        
    else:
        
        SAUCE_BROWSER = {
            "username": sauce_auth.sauce_user, \
            "access-key": sauce_auth.sauce_key,\
            "max-duration": 120, \
            "idle-timeout": 60, \
            "public": "true", \
            }

        if browser == "firefox":
            BR = {"os": "Windows 2003",\
                  "browser": "firefox",\
                  "browser-version": "3.6", \
           }

        elif browser == "opera":
            BR = {"os": "Windows 2003",\
             "browser": "opera",\
             "browser-version": "10" , \
             }


        elif browser == "safari":
            BR = {"os": "Windows 2003",\
                "browser": "safariproxy",\
                "browser-version": "5", \
                }

        elif browser == "iexplore":
            BR = {"os": "Windows 2003",\
                 "browser": "iexplore",\
                 "browser-version": "8" , \
                 }

    
        for k,v in BR.iteritems():
            SAUCE_BROWSER[k]=v

        testbrowser = json.dumps(SAUCE_BROWSER)
    return testbrowser
