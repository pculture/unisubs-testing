#Submit test results to litmus automatically

import sys
import os
import httplib
import urllib
import time
import selvars
import xml.dom.minidom


def set_test_os():
    """Returns the os string for the SUT
    """
    if selvars.sauce:
        return "Windows"
    if sys.platform.startswith("win32"):
        return "Windows"
    elif sys.platform.startswith("lin"):
        return "Linux"
    elif sys.platform.startswith("darwin"):
        return "OS X"
    else:
        print ("I don't know how to handle platform '%s'", sys.platform)

def set_test_browser():
    """Returns the browser name for the litmus platform field"

    """
    if selvars.vbrowser == "*firefox":
        return "Firefox"
    elif selvars.vbrowser == "*chrome":
        return "Firefox"
    elif selvars.vbrowser == "*safari":
        return "Safari"
    elif selvars.vbrowser == "*opera":
        return "Opera"
    elif selvars.vbrowser == "*google-chrome":
        return "Google Chrome"
    else:
        print "no idea what the browser is"

def set_build_id():
##    if selvars.builid:
##        return selvars.builid
##    else:
    buildid = time.strftime("%Y%m%d", time.gmtime()) + "99"
    return buildid

    


HEADER = """<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<litmusresults action="submit" useragent="UberSeleniumAgent/1.0 (machine foobar)" machinename="seltest_machine">
   <testresults
   username="pcf.subwriter@gmail.com"
   authtoken="autotester"
   product="MiroSubtitles"
   platform="%(browser)s"
   opsys="%(opsys)s"
   branch="master"
   buildid="%(buildid)s"
   locale="en-US"
   >
"""

STORY = """<result testid="%(testid)s"
        is_automated_result="0"
        resultstatus="%(status)s"
        exitstatus="0"
        timestamp="%(timestamp)s"
        >
       <comment>%(error_msg)s</comment>
       </result>
"""

FOOTER = """</testresults>
</litmusresults>
"""

def write_log(testid, status="pass", error_info=None):
    f = open("log.xml", "w")
    f.write(HEADER % {"buildid": set_build_id(),
                      "opsys": set_test_os(),
                      "browser": set_test_browser()})

    f.write(STORY % {"testid": testid,
                     "status": status,
                     "timestamp": time.strftime("%Y%m%d%H%M%S", time.gmtime()),
                     "error_msg": error_info
                         })

    f.write(FOOTER)
    f.close
    
                 



def send_result():
    f = open("log.xml")
    log_data = f.read()
  
    params = urllib.urlencode({'data':log_data

                                })
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = httplib.HTTPConnection("litmus.pculture.org")

    print "sending test result..."
    conn.request("POST", "/process_test.cgi", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()


if __name__ == "__main__":

    write_log("381","fail","this is a test of automatic results submission")
    send_result()

