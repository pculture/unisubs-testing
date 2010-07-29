# Module APLIB.PY
# includes:
#   * function remove_html_tags(data) - strips Python string of HTML tags
#   * subroutine AppendErrorMessage(self,sel,msg) - inserts <msg> error message
#                into verificationErrors list and into output log

import re, time, testvars

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def AppendErrorMessage(self,sel,msg):
    self.verificationErrors.append(msg)
    print "**** Error ****   "+msg

def AppendInfoMessage(self,sel,msg):
    self.verificationErrors.append(msg)
    print "---- Info----   "+msg

def wait_for_element_present(self,sel,input_field):
    for i in range(60):
        try:
            if sel.is_element_present(input_field): break
        except: pass
        time.sleep(1)
    else:
        self.fail("time out waiting for element " +input_field)

def wait_for_video_to_buffer(self,sel):
    wait_for_element_present(self,sel,"css=.mirosubs-buffered")
    print " - waiting for video to buffer " +time.strftime("%M:%S", time.gmtime())
    for i in range(300):
        try:
            if int(sel.get_element_width("css=.mirosubs-buffered")) >= 125: break
        except: pass
        time.sleep(1)
    print " - video buffered to 50% " +time.strftime("%M:%S", time.gmtime())
   


