import unittest
import time
import os
import shutil
import StringIO
import HTMLTestRunner
import js_unittests

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--sauce", action="store_true", dest="sauce", default=False,
                  help='Runs the test on saucelabs.com using specified browser')

parser.add_option("-u", "--siteurl", action="store",
                  choices=('dev', 'staging'),type="choice",
                  dest="site", default='dev',
                  help="""dev for: http://dev.universalsubtitles.org,
                        staging for: http://staging.universalsubtitles.org""")

parser.add_option("-p", "--port", action="store", type="int", dest="port", default=4444)

(options, args) = parser.parse_args()
testsauce = options.sauce
print "js_testrunner test sauce"
testsite = options.site
testport = options.port




        


class Test_HTMLTestRunner(unittest.TestCase):



# Open the desired browser and set up the test

    def test_main(self):
        # Run HTMLTestRunner.

        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromName('js_unittests.js_unittest.test_videourlparse'),
            ])


   
 # Run tests and post results to HTML page.
        buf = StringIO.StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=buf,
                    title='Univeral Subtitles JS Unittests',
                    description='Results'
                    )
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()
        # output the main test results
        results_path = os.path.join(os.getcwd(), "Results")
        filename = os.path.join(results_path, 'unisubs_' + testsite +'_'+time.strftime("%Y%m%d_%H%M", time.gmtime())+'_GMT.html')
        f = open(filename, 'w')
        f.write(byte_output)
        f.close()
        #copy the results to a file called last_run.html
        lastrun = os.path.join(results_path, 'js_last_run.html')
        shutil.copyfile(filename,lastrun)

##############################################################################
# Executing this module from the command line
##############################################################################

import unittest
if __name__ == "__main__":
    argv=['js_testrunner.py', 'Test_HTMLTestRunner']
    theme=1
    unittest.main(argv=argv)
    #HTMLTestRunner.main(argv=argv)
