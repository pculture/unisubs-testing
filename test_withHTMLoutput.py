
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



from optparse import OptionParser
parser = OptionParser()
parser.add_option("-s", "--sauce", action="store_true", dest="sauce")
parser.add_option("-b", "--browser", action="store", type="string", dest="browser", default="firefox")
parser.add_option("-p", "--port", action="store", type="int", dest="port")
parser.add_option("-u", "--siteurl", action="store", type="string", dest="site")

(options, args) = parser.parse_args()
testbrowser = options.browser
testport = options.port
testsauce = options.sauce
testsite = options.site

import mslib
import sg_64_submit
import sg_65_login
import sg_69_demoUI
import sg_78_widget_offsite               


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
            unittest.defaultTestLoader.loadTestsFromTestCase(sg_64_submit.subgroup_64),
#            unittest.defaultTestLoader.loadTestsFromTestCase(sg_78_widget_offsite.subgroup_78),
#            unittest.defaultTestLoader.loadTestsFromTestCase(sg_69_demoUI.subgroup_69),
#            unittest.defaultTestLoader.loadTestsFromTestCase(sg_65_login.subgroup_65)        
                        
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
        results_path = os.path.join(os.getcwd(), "Results")
        filename = os.path.join(results_path, 'unisubs_' + str(testbrowser) +'_'+time.strftime("%Y%m%d_%H%M", time.gmtime())+'_GMT.html')
        f = open(filename, 'w')
        f.write(byte_output)
        f.close()
        #copy the results to a file called last_run.html
        lastrun = os.path.join(results_path, 'last_run.html')
        shutil.copyfile(filename,lastrun)

##############################################################################
# Executing this module from the command line
##############################################################################

import unittest
if __name__ == "__main__":
    argv=['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']
    theme=1
    unittest.main(argv=argv)
    #HTMLTestRunner.main(argv=argv)
