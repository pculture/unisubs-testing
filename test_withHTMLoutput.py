
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
parser.add_option("-s", "--sauce", action="store_true", dest="sauce", default=False,
                  help='Runs the test on saucelabs.com using specified browser')

parser.add_option("-b", "--browser", action="store",
                  choices=('firefox','chrome','opera', 'safari', 'iexplore', 'googlechrome', 'lin_ff','firefox4','iexplore9'),
                  type="choice",
                  dest="browser", default="firefox",
                  help='Possible browser choices: firefox,chrome,opera, safari, iexplore, googlechrome, lin_ff, firefox4, iexplore9)'
                  )

parser.add_option("-f", "--fast", action="store_true", dest="fast", default=False,
                  help='run threaded - no responsibility for what this does to your machine - no limits'
                  )

parser.add_option("-p", "--port", action="store", type="int", dest="port", default=4444)

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
      

class Test_HTMLTestRunner(unittest.TestCase):



# Open the desired browser and set up the test

##    def test0(self):
##        self.suite = unittest.TestSuite()
##        buf = StringIO.StringIO()
##        runner = HTMLTestRunner.HTMLTestRunner(buf)
##        runner.run(self.suite)
##        # didn't blow up? ok.
##        self.assert_('</html>' in buf.getvalue())

    def test_main(self):

        def runtests():
            while True:
                mytest = q.get()
                tid = set_test_id(str(mytest))
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
                
                

        def set_test_id(test_id):
            
            s = str(test_id).strip(">,<,[,]")
            L = s.split('_')
            testid = L.pop()
            return testid
        
        # Run HTMLTestRunner.

        # suite of TestCases
        self.suite = unittest.TestSuite()

        ## Run a smaller group of tests when using sauce
        if testsauce == True:
            self.suite.addTests([
##                unittest.defaultTestLoader.loadTestsFromName('sg_69_demoUI.subgroup_69.test_414'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_64_submit.subgroup_64.test_538'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_64_submit.subgroup_64.test_534'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_64_submit.subgroup_64.test_533'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_offsite.subgroup_78_subtesting.test_601'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_offsite.subgroup_78_subtesting.test_622'),
                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_offsite.subgroup_78_unisubs_mc.test_623'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_playback.subgroup_78_playback.test_684'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_playback.subgroup_78_playback.test_688'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_playback.subgroup_78_playback.test_685'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_playback.subgroup_78_playback.test_686'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_playback.subgroup_78_playback.test_687'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_playback.subgroup_78_subtesting_playback.test_696'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_pagedemo.subgroup_78_pagedemo.test_689'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_pagedemo.subgroup_78_pagedemo.test_690'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_78_widget_pagedemo.subgroup_78_pagedemo.test_691'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_80_comments.subgroup_80.test_536'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_88_teams.subgroup_88.test_603'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_65_login.subgroup_65.test_379'),
##                unittest.defaultTestLoader.loadTestsFromName('sg_65_login.subgroup_65.test_378')
            ])
            
        ## Running on pcf server or local, run all the tests
        else:
            suite_list = [
                ['sg_64_submit.subgroup_64',unittest.getTestCaseNames(sg_64_submit.subgroup_64,'test')], \
                ['sg_81_ul_dl.subgroup_81',unittest.getTestCaseNames(sg_81_ul_dl.subgroup_81,'test')], \
                ['sg_69_demoUI.subgroup_69',unittest.getTestCaseNames(sg_69_demoUI.subgroup_69,'test')], \
                ['sg_80_comments.subgroup_80',unittest.getTestCaseNames(sg_80_comments.subgroup_80,'test')],  \
                ['sg_65_login.subgroup_65',unittest.getTestCaseNames(sg_65_login.subgroup_65,'test')], \
                ['sg_78_widget_offsite.subgroup_78_unisubs_mc',unittest.getTestCaseNames(sg_78_widget_offsite.subgroup_78_unisubs_mc,'test')], \
                ['sg_78_widget_offsite.subgroup_78_pculture',unittest.getTestCaseNames(sg_78_widget_offsite.subgroup_78_pculture,'test')], \
                ['sg_78_widget_offsite.subgroup_78_subtesting',unittest.getTestCaseNames(sg_78_widget_offsite.subgroup_78_subtesting,'test')], \
                ['sg_78_widget_pagedemo.subgroup_78_pagedemo',unittest.getTestCaseNames(sg_78_widget_pagedemo.subgroup_78_pagedemo,'test')],
                ['sg_70_revisions.subgroup_70',unittest.getTestCaseNames(sg_70_revisions.subgroup_70,'test')], \
                ['sg_88_teams.subgroup_88',unittest.getTestCaseNames(sg_88_teams.subgroup_88,'test')], \
                           ]

            for sg in suite_list:
                for tc in sg[1]:
                    self.suite.addTests([
                        unittest.defaultTestLoader.loadTestsFromName(sg[0]+"."+tc)                    
                    ])
            

        # Invoke TestRunner

        # Post the output directly to Litmus
        if testlitmus == True:
            if testsauce == True:
                num_worker_threads = 5
            elif testfast == True:
                num_worker_threads = 3
            else:
                num_worker_threads = 1
            
            q = Queue()
            for i in range(num_worker_threads):  
                t = Thread(target=runtests)
                t.daemon = True
                t.start()    
            for x in self.suite:
                q.put(x)
            q.join()

           


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
