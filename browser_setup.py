# set up the runtine setting

import test_withHTMLoutput as controller

if controller.testbrowser:
    mybrowser = "*"+controller.testbrowser
    print "browser setup is using browser: " + mybrowser        
else:
    mybrowser = "*firefox"
    print "browser setup is using default browser: "+ mybrowser
