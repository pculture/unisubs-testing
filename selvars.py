
"""
Sets up the runtime varsf or browser, sauce (True / False) and  Port.
testvars uses these values if they exist, they get set at the commandline
by test_withHTMLoutput.py

"""
import test_withHTMLoutput as controller
import sauce_auth
import json

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
    sets the value of port if specified at the cmdline
    """   
    if controller.testsite:
        site = "http://"+controller.testsite+".universalsubtitles.org"
    else:
        site = "http://staging.universalsubtitles.org"
    return site

def set_widget_null_page():
    """
    sets the dev-null test page to use for testing (staging or dev), if not set, defaults to dev
    """   
    if controller.testsite:
        page = "mirosubs_tests/"+controller.testsite+"-widget-null.html"
    else:
        page = "mirosubs_tests/dev-widget-null.html"
    return page

def set_subtesting_wordpress_page():
    """
    sets the wordpress page to use for testing, if not set, defaults to dev
    """   
    if controller.testsite == "staging":
        page = "/2010/10/16/script-linking-to-stagin/"
    else:
        page = "/2010/04/20/script-linking-to-dev/"
    return page


def set_browser(testid="none",testdesc="none"):
    """ Sets up the browser to either the *browser name or the correct
    json string if the tests are to be run with sauce on-demand
    """
    # if using sauce - create the correctly formated json string
    # - assume windows 2003
    # otherwise use *browser name
    if controller.testsauce==True:
        if controller.testbrowser == "googlechrome":
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "googlechrome",\
                        "browser-version": "", \
                        "max-duration": 600, \
                        "idle-timeout": 120, \
                        "job-name": testid +': '+ testdesc \
                    }
                               
        elif controller.testbrowser == "iexplore":
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "iexplore",\
                        "browser-version": "8" , \
                        "max-duration": 600, \
                        "idle-timeout": 120, \
                        "job-name": testid +': '+ testdesc \
                    }
        elif controller.testbrowser == "opera":
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "opera",\
                        "browser-version": "10" , \
                        "max-duration": 600, \
                        "idle-timeout": 120, \
                        "job-name": testid +': '+ testdesc \
                    }
        elif controller.testbrowser == "safari":
            sbrowser = {\
                        "username": sauce_auth.sauce_user,\
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "safariproxy",\
                        "browser-version": "5", \
                        "max-duration": 600, \
                        "idle-timeout": 120, \
                        "job-name": testid +': '+ testdesc \
                    }
        else:
            sbrowser= { \
                        "username": sauce_auth.sauce_user,
                        "access-key": sauce_auth.sauce_key,\
                        "os": "Windows 2003",\
                        "browser": "firefox",\
                        "browser-version": "3.6", \
                        "max-duration": 600, \
                        "idle-timeout": 120, \
                        "job-name": testid +': '+ testdesc \
                    }
        browser = json.dumps(sbrowser, indent=4)
    else:
        #use default browser
        browser = "*"+controller.testbrowser

    return browser

    

