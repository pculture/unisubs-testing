#!/usr/bin/env python

from selenium import webdriver

base_url = "http://staging.universalsubtitles.org"
browser = webdriver.Firefox()
timeout = 60000

admin_user = "sub_writer"
admin_pass = "sub.writer"
