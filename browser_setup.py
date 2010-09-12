# set up the runtine setting

import test_cmdargs

print test_cmdargs.testbrowser


if test_cmdargs.testbrowser:
    mybrowser = "*"+test_cmdargs.testbrowser
    print "browser setup is using browser: " + mybrowser        
else:
    mybrowser = "*firefox"
    print "browser setup is using default browser: "+ mybrowser
