#!/usr/bin/env python

timeout = 60000
base_url = "http://selenium:selenium4970@staging.universalsubtitles.org/"
admin_user = "sub_writer"
admin_pass = "sub.writer"

try:
    from testsetup_local import *
except ImportError:
    pass

