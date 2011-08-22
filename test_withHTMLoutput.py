# -*- coding: utf-8 -*-
from selenium import selenium
#import system modules
import unittest, time, re
import shutil
import os
import StringIO
import sys
from threading import Thread
from Queue import Queue

import HTMLTestRunner
import litmusresult
import sg_64_submit
import sg_65_login 
import sg_69_demoUI
import sg_70_revisions
import sg_78_widget_offsite
import sg_78_widget_pagedemo
import sg_78_widget_playback
import sg_80_comments
import sg_81_ul_dl
import sg_88_teams


from optparse import OptionParser
parser = OptionParser()
parser.add_option(
    "-s", "--sauce", action="store_true", dest="sauce", default=False,
    help='Runs the test on saucelabs.com using specified browser')

parser.add_option(
    "-m", "--minimal", action="store_true", dest="minimal", default=False,
    help='Runs the minimal pagedemo tests')

parser.add_option(
    "-j", "--jenkins", action="store_true", dest="jenkins", default=False,
    help='limited test suite for jenkins ci testing')

parser.add_option(
    "-b", "--browser", action="store",
    choices=('firefox','chrome','opera', 'safari', 'iexplore', 'googlechrome', 
             'lin_ff','firefox4','iexplore9'),
    type="choice",
    dest="browser", default="firefox",
    help='Possible browser choices: firefox,chrome,opera, safari, iexplore, googlechrome, lin_ff, firefox4, iexplore9)')

parser.add_option(
    "-f", "--fast", action="store_true", dest="fast", default=False,
    help='run threaded - no responsibility for what this does to your machine - no limits')

parser.add_option(
    "-p", "--port", action="store", type="int", dest="port", default=4444)

parser.add_option("-u", "--siteurl", action="store",
                  choices=('dev', 'staging'),type="choice",
                  dest="site", default='dev',
                  help="""dev for: http://dev.universalsubtitles.org,
                        staging for: http://staging.universalsubtitles.org""")

parser.add_option("-l", "--litmus",action="store_true",dest="litmus",default=False,
                  help='Sends test output directly to litmus.pculture.org')

parser.add_option("-i", "--buildid", action="store", dest="buildid",
                  default=time.strftime("%Y%m%d", time.gmtime()) + "99",
                  help="specify the build id of the litmus testrun results to display there")

(options, args) = parser.parse_args()
testbrowser = options.browser
testport = options.port
testsauce = options.sauce
testfast = options.fast
testsite = options.site
testbuildid = options.buildid
testlitmus = options.litmus
minimal = options.minimal
jenkins = options.jenkins

class Test_HTMLTestRunner(unittest.TestCase):
    SAUCE_MINIMAL_PAGEDEMOS = [
##        'sg_78_widget_offsite.subgroup_78_unisubs_mc.test_623',
##        'sg_78_widget_playback.subgroup_78_playback.test_684',
##        'sg_78_widget_playback.subgroup_78_playback.test_688',
##        'sg_78_widget_playback.subgroup_78_playback.test_685',
##        'sg_78_widget_playback.subgroup_78_playback.test_686',
##        'sg_78_widget_playback.subgroup_78_playback.test_687',
##        'sg_78_widget_playback.subgroup_78_playback.test_701',
        'sg_78_widget_playback.subgroup_78_playback.test_702',                
#        'sg_78_widget_pagedemo.subgroup_78_pagedemo.test_689',
#        'sg_78_widget_pagedemo.subgroup_78_pagedemo.test_690',
#        'sg_78_widget_pagedemo.subgroup_78_pagedemo.test_691'
        ]

    SAUCE_TESTS = [
        'sg_69_demoUI.subgroup_69.test_373',
##        'sg_69_demoUI.subgroup_69.test_414',
##        'sg_64_submit.subgroup_64.test_538',
##        'sg_64_submit.subgroup_64.test_534',
##        'sg_64_submit.subgroup_64.test_533',
##        ## 'sg_78_widget_offsite.subgroup_78_subtesting.test_601',
##        ## 'sg_78_widget_offsite.subgroup_78_subtesting.test_622',
##        ## 'sg_78_widget_playback.subgroup_78_subtesting_playback.test_696',
##        'sg_80_comments.subgroup_80.test_536',
##        'sg_88_teams.subgroup_88.test_613',
##        'sg_88_teams.subgroup_88.test_693',
##        'sg_65_login.subgroup_65.test_379',
##        'sg_65_login.subgroup_65.test_378'
        ]

    SAUCE_TESTS.extend(SAUCE_MINIMAL_PAGEDEMOS)


    JENKINS_TESTS = [
        'sg_64_submit.subgroup_64.test_533',
        'sg_69_demoUI.subgroup_69.test_414'
        ]
    
    ALL_TESTS = [
        'sg_64_submit.subgroup_64',
        'sg_81_ul_dl.subgroup_81',
        'sg_69_demoUI.subgroup_69',
        'sg_80_comments.subgroup_80',
        'sg_65_login.subgroup_65',
        'sg_78_widget_offsite.subgroup_78_unisubs_mc',
        'sg_78_widget_offsite.subgroup_78_pculture',
##        ## 'sg_78_widget_offsite.subgroup_78_subtesting',
        'sg_78_widget_pagedemo.subgroup_78_pagedemo',
        'sg_70_revisions.subgroup_70',
        'sg_78_widget_playback.subgroup_78_playback',
        'sg_88_teams.subgroup_88'
        ]

    def _set_test_id(self, test_id):
        s = str(test_id).strip(">,<,[,]")
        L = s.split('_')
        testid = L.pop()
        return testid

    def _runtests(self,q):
        while True:
            mytest = q.get()
            tid = self._set_test_id(str(mytest))
            tname = "Thread_"+tid+"_"+time.strftime("%M%S", time.gmtime())+".log"
            res = open(tname,"w")
            runner = unittest.TextTestRunner(stream=res)
            runner.run(mytest)
            res.close()

            # get the result and send it to litmus
            logs = file(tname,"r")
            byte_output = logs.read()
            id_string = str(mytest)
            stat = byte_output[0]
            logs.close()
            litmusresult.write_log(id_string,stat,testbuildid,byte_output)
            os.remove(tname)
            q.task_done()

    def _add_smaller_group_for_sauce(self):
        tests = self.SAUCE_MINIMAL_PAGEDEMOS if minimal else self.SAUCE_TESTS
        self.suite.addTests([
                unittest.defaultTestLoader.loadTestsFromName(t) 
                for t in tests])

    def _add_jenkins_tests(self):
        tests = self.JENKINS_TESTS
        self.suite.addTests([
                unittest.defaultTestLoader.loadTestsFromName(t) 
                for t in tests])
        

    def _add_all_tests(self):
        suite_list = [[t, unittest.getTestCaseNames(eval(t), 'test')] 
                      for t in self.ALL_TESTS]
        for sg in suite_list:
            for tc in sg[1]:
                self.suite.addTests([
                        unittest.defaultTestLoader.loadTestsFromName(sg[0]+"."+tc)])

    def _post_output_to_litmus(self):
        if testsauce == True:
            num_worker_threads = 5
        elif testfast == True:
            num_worker_threads = 3
        else:
            num_worker_threads = 1

        q = Queue()
        for i in range(num_worker_threads):  
            t = Thread(target=lambda: self._runtests(q))
            t.daemon = True
            t.start()    
        for x in self.suite:
            q.put(x)
        q.join()

    def _post_results_to_html_page(self):
        buf = StringIO.StringIO()
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='Univeral Subtitles Testing',
            description='Results')
        runner.run(self.suite)

        # check out the output
        byte_output = buf.getvalue()
        # output the main test results
        results_path = os.path.join(os.getcwd(), "Results")
        filename = os.path.join(
            results_path, 
            'unisubs_{0}_{1}_{2}_GMT.html'.format(
                str(testsite),
                str(testbrowser), 
                time.strftime("%Y%m%d_%H%M", time.gmtime())))
        f = open(filename, 'w')
        f.write(byte_output)
        f.close()
        # copy the results to a file called last_run.html
        
        lastrun = os.path.join(results_path, testsite+'_lastrun.html')
        shutil.copyfile(filename,lastrun)

    def test_main(self):                
        """ Run HTMLTestRunner. """

        self.suite = unittest.TestSuite()

        if testsauce:
            self._add_smaller_group_for_sauce()
        elif jenkins:
            self._add_jenkins_tests()
        else: # pcf server or local
            self._add_all_tests()           

        # Invoke TestRunner

        if testlitmus:
            self._post_output_to_litmus()
        else:
            self._post_results_to_html_page()


##############################################################################
# Executing this module from the command line
##############################################################################

import unittest
if __name__ == "__main__":
    argv=['test_HTMLTestRunner.py', 'Test_HTMLTestRunner']
    theme=1
    unittest.main(argv=argv)
    #HTMLTestRunner.main(argv=argv)
