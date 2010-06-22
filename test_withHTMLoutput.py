# -*- coding: utf-8 -*-
from selenium import selenium
#import system modules
import unittest, time, re
import StringIO
import sys
import HTMLTestRunner
# import MC Test Suite modules
import testvars
import sg_65_login, sg_64_subwidget

# ------------------------------------------------------------------------
# This is the main test

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
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_378),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_379),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_380),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_381),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_382),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_383),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_384),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.tc_385),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_64_subwidget.tc_369),
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_64_subwidget.tc_370),
            
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        #runner = unittest.TextTestRunner(buf) #DEBUG: this is the unittest baseline
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='Miro Community Test Suite',
                    description='Results of test run'
                    )
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()
        # output the main test results
        filename=testvars.MSTestVariables["ResultOutputDirectory"]+'MS_test_results_'+time.strftime("%d-%m-%Y_%H-%M", time.gmtime())+'_GMT.html'
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
