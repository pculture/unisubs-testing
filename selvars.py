"""
Sets up the runtime varsf or browser, sauce (True / False) and  Port.
testvars uses these values if they exist, they get set at the commandline
by test_withHTMLoutput.py

"""

import test_withHTMLoutput as controller
import sauce_auth
import json


""" localhost should default to 'localhost' unless using sauce, then it
    needs to be the sauce url
"""



def set_localhost():
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
    sets the value of port if specified at the cmdline
    """   
    if controller.testsite:
        site = "http://"+controller.testsite+".universalsubtitles.org"
    else:
        site = "http://dev.universalsubtitles.org"
    return site

if controller.testbrowser:
    vbrowser = "*"+controller.test_browser
else:
    vbrowser = "*chrome"


def set_browser():
    """ Sets up the browser to either the *browser name or the correct
    json string if the tests are to be run with sauce
    """
    # if using sauce - create the correctly formated json string
    # - assume windows 2003
    # otherwise use *browser name
    if controller.testsauce==True:
        print "running tests with sauce"
        if controller.testbrowser == "googlechrome":
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "googlechrome",\
                        "browser-version": "" \
                    }
                               
        elif controller.testbrowser == ("ie" or "iexplore"):
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "iexplore",\
                        "browser-version": "8" \
                    }
        elif controller.testbrowser == ("opera"):
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "opera",\
                        "browser-version": "10" \
                    }
        elif controller.testbrowser == ("safari"):
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "safariproxy",\
                        "browser-version": "5" \
                    }
        else:
            sbrowser= { \
                        "username": sauce_auth.sauce_user,
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "firefox",\
                        "browser-version": "3.6" \
                    }
        browser = json.dumps(sbrowser, indent=4)
    else:
        print "using *browser, default is ff"
        browser = "*"+controller.testbrowser

    return browser

    

