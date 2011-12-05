import os
import sys
import nose
import nose.config
from lettuce import lettuce_cli

from optparse import OptionParser

parser = OptionParser()
parser.add_option(
    "-s", "--sauce", action="store_true", dest="sauce", default=False,
    help='Runs the test on saucelabs.com using specified browser')

parser.add_option(
    "-b", "--browser", action="store",
    choices=('firefox','chrome','opera', 'safari', 'iexplore', 'googlechrome', 
             'lin_ff','firefox5','iexplore9'),
    type="choice",
    dest="browser", default="firefox",
    help='Possible browser choices: firefox, chrome, opera, safari, iexplore, googlechrome, lin_ff, firefox3, iexplore9)')

parser.add_option(
    "-p", "--port", action="store", type="int", dest="port", default=4444)

parser.add_option("-u", "--siteurl", action="store", dest="siteurl",
                  default='http://dev.universalsubtitles.org',
                  help="""The url to use for testing, default is dev.universalsubtitles.org""")

parser.add_option("-t", "--testsuite", action="store",
                  dest="suite", default='rc_only.cfg',
                  help="""Config file to speicfy which tests should be run, should be located in suite_config directory""")

(options, args) = parser.parse_args()
testsuite = options.suite
testbrowser = options.browser
testport = options.port
testsite = options.siteurl

class Configs():
    """Less than ideal - it's the only way I could think of to claim the commandline args before they get to nose.

    Imports the setup module and opens and closes a browser windows.
    """
    def setup(self):
        sys.path.append(os.path.join(os.getcwd(), 'webdriver_suite'))
        import setup
        b = setup.browser
        b.close()
         
class RunTests():

    def cmd_line_args(self):
        args = sys.argv[1:]
        sys.argv = sys.argv[0:1]

    def run_tests_with_lettuce(self):
        curr_dir = os.getcwd()
        try:
            lettuce_dir = os.path.join(curr_dir, 'tests')
            os.chdir(lettuce_dir)
            lettuce_cli.main('--verbosity=0 --with-xunit')
        finally:
            os.chdir(curr_dir)
    def run_tests_with_nose(self):
        BASE_CONFIG = os.path.join(os.getcwd(), "suite_config", "base_config.cfg")
        TEST_CONFIG = os.path.join(os.getcwd(), "suite_config", testsuite)
          
        cfgs = [BASE_CONFIG, TEST_CONFIG]
        print cfgs
        nose.config.config_files = cfgs
        testrun = nose.config.Config()
        testrun.configure()
        nose.run(testrun)

if __name__ == "__main__":
#    Configs().setup()
    t = RunTests()
    t.cmd_line_args()
    t.run_tests_with_lettuce()
    t.run_tests_with_nose()
