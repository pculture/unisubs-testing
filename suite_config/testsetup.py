#!/usr/bin/env python

from selenium import webdriver

timeout = 60000
browser = webdriver.Firefox()

base_url = "http://dev.universalsubtitles.org/"
admin_user = "sub_writer"
admin_pass = "sub.writer"

try:
    from testsetup_local import *
except ImportError:
    pass

