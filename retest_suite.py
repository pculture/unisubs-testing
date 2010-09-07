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

    def test_main(self):
        # Run HTMLTestRunner.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_413')
            
            ])

        # Invoke TestRunner
        buf = StringIO.StringIO()
        runner = unittest.TextTestRunner(buf) #DEBUG: this is the unittest baseline
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()

##############################################################################
# Executing this module from the command line
##############################################################################

import unittest
if __name__ == "__main__":
    unittest.main()
