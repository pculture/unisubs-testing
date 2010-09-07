
# -*- coding: utf-8 -*-
from selenium import selenium
#import system modules
import unittest, time, re
import shutil
import os
import StringIO
import sys
import HTMLTestRunner
# import MS Test Suite modules
import testvars
import mslib
import sg_65_login
import sg_64_subwidget
import sg_69_demoUI

class Test_HTMLTestRunner(unittest.TestCase):

# Open the desired browser and set up the test

    def test0(self):
        self.suite = unittest.TestSuite()
        buf = StringIO.StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(buf)
        runner.run(self.suite)
        # didn't blow up? ok.
        self.assert_('</html>' in buf.getvalue())

    def test_main(self):
        # Run HTMLTestRunner.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_69_demoUI.subgroup_69),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_64_subwidget.subgroup_64),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.subgroup_65)
            
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf) #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='Univeral Subtitles Testing',
                    description='Results'
                    )
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()
        # output the main test results
        
        filename = os.path.join(testvars.MSTestVariables["ResultOutputDirectory"], 'unisubs_' + testvars.vbrowser +'_'+time.strftime("%Y%m%d_%H%M", time.gmtime())+'_GMT.html')
        f = open(filename, 'w')
        f.write(byte_output)
        f.close()
        #if running on pcf-mcdev, copy the results to the public directory
        lastrun = testvars.MSTestVariables["ResultOutputDirectory"] + 'last_run.html'
        shutil.copyfile(filename,lastrun)

##############################################################################
# Executing this module from the command line
##############################################################################

import unittest
if __name__ == "__main__":
    if len(sys.argv) > 1:
        argv = sys.argv
    else:
        argv=['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']
    theme=1
    unittest.main(argv=argv)
    #HTMLTestRunner.main(argv=argv)
