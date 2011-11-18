#X-browser test run on sauce

from subprocess import Popen


processes = []
browsers = ("firefox","safari")

for browser in browsers:
    
    testrun = ['python', 'test_withHTMLoutput.py', '--sauce','--browser', browser]
    print testrun
    processes.append(Popen(testrun))

for process in processes:
    process.wait()

    

    
