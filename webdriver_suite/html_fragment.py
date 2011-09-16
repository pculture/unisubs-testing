#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla Firefox Support.
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#                 Dave Hunt <dhunt@mozilla.com>
#                 David Burns
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

'''
Modified for Universal Subtitles Sept 15, 2011
Created on Jun 21, 2010
'''
import re
import time
import base64

http_regex = re.compile('https?://((\w+\.)+\w+\.\w+)')


class HtmlFragment(object):
    """
    Base class for all Pages
    """
    def __init__(self, testsetup):
        '''
    Constructor
    '''
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.browser = testsetup.browser
        self.timeout = testsetup.timeout
       
    

    def click_by_css(self, element, wait_for_element=None):
        try:
            elem = self.browser.find_element_by_css_selector(element)
        except:
            self.record_error()
            raise Exception(elem + "not found")
        
        elem.click()
        if wait_for_element:
            self.wait_for_element_present(wait_for_element)

    def type_by_css(self, element, text):
        elem = self.browser.find_element_by_css_selector(element)
        elem.send_keys(text)
        

    def is_element_present(self, element):
        elements_found = self.browser.find_elements_by_css_selector(element)
        if len(elements_found) > 0:
            return True
        else:
            return False
                      

    def wait_for_element_present(self, element):
        count = 0
        while not self.browser.find_element_by_css_selector(element):
            time.sleep(1)
            count += 1
            if count == self.timeout / 1000:
                self.record_error()
                raise Exception(element + ' has not loaded')
##
##    def wait_for_element_visible(self, element):
##        self.wait_for_element_present(element)
##        count = 0
##        while not self.is_element_visible(element):
##            time.sleep(1)
##            count += 1
##            if count == self.timeout / 1000:
##                self.record_error()
##                raise Exception(element + " is not visible")
##
##    def wait_for_element_not_visible(self, element):
##        count = 0
##        while self.is_element_visible(element):
##            time.sleep(1)
##            count += 1
##            if count == self.timeout / 1000:
##                self.record_error()
##                raise Exception(element + " is still visible")


    def record_error(self):
        """
            Records an error. 
        """

        http_matches = http_regex.match(self.base_url)
        file_name = http_matches.group(1)

        print '-------------------'
        print 'Error at ' + self.browser.current_url
        print 'Page title ' + self.browser.title
        print '-------------------'
        filename = file_name + '_' + str(time.time()).split('.')[0] + '.png'

        print 'Screenshot of error in file ' + filename
#        f = open(filename, 'wb')
        self.browser.get_screenshot_as_file(filename)
#        f.close()
