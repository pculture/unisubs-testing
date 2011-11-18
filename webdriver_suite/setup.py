#!/usr/bin/env python
from selenium import webdriver
from urlparse import urlsplit

try:
    import settings as c
except:
    import run_suite as c

BASE_URL = c.testsite
u = urlsplit(BASE_URL)
if len(u.netloc.split('.')) < 3:
    raise Exception("Please enter a complete url")



base_url = BASE_URL
admin_user = "sub_writer"
admin_pass = "sub.writer"
timeout = 60000

if c.testbrowser == "firefox":
    browser = webdriver.Firefox()
elif c.testbrowser == "chrome":
    browser = webdriver.Chrome()
elif c.testbrowser == "iexplore":
    browser = webdriver.Ie()
else:
    raise Exception("option not availble: %s" % testsetup.browser)


