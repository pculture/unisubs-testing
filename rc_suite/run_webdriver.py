"""
Entrey point for webdriver tests in universal subtitles selenium tests cases.
Tests should leave in wd_tests

"""
import unittest2 as unittest
import time
import os
import shutil
import StringIO
import logging

from selenium import webdriver

import sys

from optparse import OptionParser


import webdriver_conf

FIREFOX_CONF = {
    "osx": "/Applications/Firefox.app/Contents/MacOS/firefox-bin"
    }

ENV_URL_MAPPING = {
    "dev": "http://dev.universalsubtitles.org/",
    "local": "http://unisubs.example.com:8000/",
    "staging": "http://staging.universalsubtitles.org/",
    }

def parse_options():
    parser = OptionParser()
    parser.add_option("-s", "--sauce", action="store_true", dest="sauce", default=False,
                      help='Runs the test on saucelabs.com using specified browser')

    parser.add_option("-e", "--environment", action="store",
                      choices=('local', 'dev', 'staging'),type="choice",
                      dest="site", default='dev',
                      help="""dev for: http://dev.universalsubtitles.org,
                            staging for: http://staging.universalsubtitles.org
                            local for http://unisubs.example.com:8000/""")

    parser.add_option("-p", "--port", action="store", type="int", dest="port", default=4444)

    parser.add_option("-b", "--browser", action="store",type="string",
                      dest="browser_name", default='chrome',
                      help="Which browser(s) to run (depends on local env capabilities )")

    parser.add_option("-v", "--verbosity", action="store",type="int",
                      dest="verbosity", default='0',
                      help="How much output do we want?")    
    (options, args) =  parser.parse_args()
    args_cleaned = [x for x in args if x.startswith("-") is False]    

    return options, args

def _get_firefox(bin_path=None, profile_name=None):
    import selenium.webdriver.firefox.webdriver as fwb
    profile_path = os.path.join(os.path.split(__file__)[0], profile_name or "selenium-firefox-profile")
    if not os.path.exists(profile_path):
        os.makedirs(profile_path)
    ff_profile = fwb.FirefoxProfile(profile_path)
    ff_path = bin_path or FIREFOX_CONF["osx"]
    ff_bin = fwb.FirefoxBinary(firefox_path=ff_path)
    driver = fwb.WebDriver(firefox_profile=ff_profile, firefox_binary=ff_bin)
    return driver

def _get_chrome():
    try:
        return  webdriver.Chrome()
    except:
        logger.error("Make sure you ohave the chromedriver at http://code.google.com/p/chromium/downloads/list")
        raise
        
def get_driver(browser_name, *args, **kwargs):
    
    return {
          "firefox": _get_firefox,
          "chrome": _get_chrome,
        }[browser_name](*args, **kwargs)
                                

def _create_env(options):
    """
    Store 'global' options on webdriver_conf module, for easy
    sharing between test files
    """
    webdriver_conf.URL_BASE = ENV_URL_MAPPING[options.site]
    webdriver_conf.driver = get_driver(options.browser_name)
    # FIZME: monkey path to allow for base_url, does webdriver do that?
    old_func  = webdriver_conf.driver.get
    def absolute_get( url):
        if url.startswith("http"):
            furl = url
        else:
            furl = webdriver_conf.URL_BASE + url
        return old_func(furl)
    webdriver_conf.driver.get = absolute_get

if __name__ == "__main__":
    (options, test_names) = parse_options()
    # TODO: make webdriver open per test so we can parellilize them better
    _create_env(options)
    try:
        loader = unittest.TestLoader()
        # TODO make hook here (patterns=args[1]) for loading specific tests
        suite = loader.discover(os.path.join(os.path.dirname(__file__),  "webdriver_suite"), pattern="*.py")
        runner = unittest.TextTestRunner(verbosity=options.verbosity)
        runner.run(suite)
    except:
        raise
    finally:
        webdriver_conf.driver.quit()

        
    
