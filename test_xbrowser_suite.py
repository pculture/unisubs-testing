# -*- coding: utf-8 -*-
from selenium import selenium
#import system modules
import unittest, time, re
import StringIO
import sys
import HTMLTestRunner
# import MS Test Suite modules
import testvars
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
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_373'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_389'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_398'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_401'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_403'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_404'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_405'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_406'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_410'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_411'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_412'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_414'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_415'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_416'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_470'),
            unittest.defaultTestLoader.loadTestsFromName('sg_64_subwidget.subgroup_64.test_369'),
##            unittest.defaultTestLoader.loadTestsFromName('sg_64_subwidget.subgroup_64.test_370'),
            unittest.defaultTestLoader.loadTestsFromName('sg_64_subwidget.subgroup_64.test_376')
            
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf) #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='Univeral Subtitles Testing',
                    description='Cross browser regression testing'
                    )
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()
        # output the main test results
        filename=testvars.MSTestVariables["ResultOutputDirectory"]+ "MS_xbrowser_"+ testvars.vbrowser+"_"+time.strftime("%d-%m-%Y_%H-%M", time.gmtime())+'_GMT.html'
        f = open(filename, 'w')
        f.write(byte_output)
        f.close()

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
