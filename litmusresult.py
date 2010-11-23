#Submit test results to litmus automatically

import sys
import os
import httplib
import urllib
import json
import time
import selvars


def set_test_os():
    """Returns the os string for the SUT
    """
    if selvars.set_sauce():
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
    if selvars.set_sauce() == True:
        b = json.loads(selvars.set_browser())
        if b["browser"] == "firefox":
            return "Firefox"
        elif b["browser"] == "chrome":
            return "Firefox"
        elif b["browser"] == "safariproxy":
            return "Safari"
        elif b["browser"] == "opera":
            return "Opera"
        elif b["browser"] == "iexplore":
            return "IE 8"
        elif b["browser"] == "iexploreproxy":
            return "IE 8"
        elif b["browser"] == "googlechrome":
            return "Google Chrome"
        else:
            print "no idea what the browser is: "+ b["browser"]
      
    if selvars.set_browser() == "*firefox":
        return "Firefox"
    elif selvars.set_browser() == "*chrome":
        return "Firefox"
    elif selvars.set_browser() == "*safari":
        return "Safari"
    elif selvars.set_browser() == "*opera":
        return "Opera"
    elif selvars.set_browser() == "*iexplore":
        return "IE 8"
    elif selvars.set_browser() == "*iexploreproxy":
        return "IE 8"
    elif selvars.set_browser() == "*googlechrome":
        return "Google Chrome"
    else:
        print "no idea what the browser is"


def set_test_id(test_id):
    
    s = str(test_id).strip(">,<,[,]")
    L = s.split('_')
    testid = L.pop()
    return testid

def set_status(stat):
    print stat
    if stat == ".":
        status = "pass"
    else:
        status = "fail"
    return status


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
         <comment><![CDATA[
         %(error_msg)s

         ]]>

         </comment>
       </result>
"""

FOOTER = """</testresults>
</litmusresults>
"""

def write_log(testid,stat,buildid,error_info=""):
       
    f = open("log.xml", "w")
    f.write(HEADER % {"buildid": buildid,
                      "opsys": set_test_os(),
                      "browser": set_test_browser()})

    f.write(STORY % {"testid": set_test_id(testid),
                     "status": set_status(stat),
                     "timestamp": time.strftime("%Y%m%d%H%M%S", time.gmtime()),
                     "error_msg": error_info.lstrip('.')
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
    print data
    conn.close()
    f.close()


if __name__ == "__main__":

 #   write_log("381",None)
    send_result()

