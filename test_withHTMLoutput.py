
# -*- coding: utf-8 -*-
from selenium import selenium
#import system modules
import unittest, time, re
import shutil
import os
import StringIO
import sys
import HTMLTestRunner
import litmusresult
import mslib
import sg_64_submit
import sg_65_login 
import sg_69_demoUI 
import sg_78_widget_offsite
import sg_80_comments
import sg_81_ul_dl



from optparse import OptionParser
parser = OptionParser()
parser.add_option("-s", "--sauce", action="store_true", dest="sauce",
                  help='Runs the test on saucelabs.com using specified browser')
parser.add_option("-b", "--browser", action="store",
                  choices=('firefox','chrome','opera', 'safari', 'iexplore', 'googlechrome'),type="choice",
                  dest="browser", default="firefox",
                  help='Possible browser choices: firefox,chrome,opera, safari, iexplore, googlechrome'
                  )

parser.add_option("-p", "--port", action="store", type="int", dest="port")
parser.add_option("-u", "--siteurl", action="store",
                  choices=('dev', 'staging'),type="choice",
                  dest="site", default='dev',
                  help="""dev for: http://dev.universalsubtitles.org,
                        staging for: http://staging.universalsubtitles.org""")
parser.add_option("-l", "--litmus",action="store_true",dest="litmus",
                  help='Sends test output directly to litmus.pculture.org')
parser.add_option("-i", "--buildid", action="store", dest="buildid",
                  default=time.strftime("%Y%m%d", time.gmtime()) + "99",
                  help="specify the build id of the litmus testrun results to display there")

(options, args) = parser.parse_args()
testbrowser = options.browser
testport = options.port
testsauce = options.sauce
testsite = options.site
testbuildid = options.buildid
testlitmus = options.litmus
                  

          


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

        ## Run a smaller group of tests when using sauce
        if testsauce == True:
            self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_389'),
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_414'),
            unittest.defaultTestLoader.loadTestsFromName('sg_64_submit.subgroup_64.test_534'),
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_408'),
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_406'),
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_414'),
            unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_388'),
            unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_offsite.subgroup_78.test_369'),
            unittest.defaultTestLoader.loadTestsFromName('sg_80_comments.subgroup_80.test_536'),
            unittest.defaultTestLoader.loadTestsFromName('sg_80_comments.subgroup_80.test_537'),
            unittest.defaultTestLoader.loadTestsFromName('sg_65_login.subgroup_65.test_384'),
            unittest.defaultTestLoader.loadTestsFromName('sg_65_login.subgroup_65.test_378')
            
            ])
        ## Running on pcf server or local, run all the tests
        else:
            suite_list = [['sg_64_submit.subgroup_64',unittest.getTestCaseNames(sg_64_submit.subgroup_64,'test')], \
                          ['sg_81_ul_dl.subgroup_81',unittest.getTestCaseNames(sg_81_ul_dl.subgroup_81,'test')], \
                          ['sg_69_demoUI.subgroup_69',unittest.getTestCaseNames(sg_69_demoUI.subgroup_69,'test')], \
                          ['sg_80_comments.subgroup_80',unittest.getTestCaseNames(sg_80_comments.subgroup_80,'test')],  \
                          ['sg_65_login.subgroup_65',unittest.getTestCaseNames(sg_65_login.subgroup_65,'test')], \
                          ['sg_78_widget_offsite.subgroup_78',unittest.getTestCaseNames(sg_78_widget_offsite.subgroup_78,'test')], \
                          ['sg_70_revisions.subgroup_70',unittest.getTestCaseNames(sg_70_revisions.subgroup_70,'test')], \
                           ]

            for sg in suite_list:
                for tc in sg[1]:
                    self.suite.addTests([
                        unittest.defaultTestLoader.loadTestsFromName(sg[0]+"."+tc)                    
                    ])
            

        # Invoke TestRunner

        # Post the output directly to Litmus
        if testlitmus == True:
            buf = StringIO.StringIO()
            runner = unittest.TextTestRunner(stream=buf)
            for x in self.suite:
                runner.run(x)
                # check out the output
                byte_output = buf.getvalue()
                id_string = str(x)
                stat = byte_output[0]
                try:
                    litmusresult.write_log(id_string,stat,testbuildid,byte_output)
                    litmusresult.send_result()
                finally:
                    buf.truncate(0)



        else:   # Post results to HTML page
            buf = StringIO.StringIO()
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
