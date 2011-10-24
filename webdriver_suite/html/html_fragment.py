#!/usr/bin/env python
import re
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.common.exceptions import NoSuchElementException

import testsetup

http_regex = re.compile('https?://((\w+\.)+\w+\.\w+)')
nums_regex = re.compile(r'(\D+)(\d+)')


MULTIPLE_ELS = '%s exists on multiple places on the page, please be more specific'

class HtmlFragment(object):
    """
    Base class for all Pages
    """
    def __init__(self):
        '''Constructor'''
        self.base_url = testsetup.base_url
        self.browser = testsetup.browser
        self.username = testsetup.admin_user
        self.password = testsetup.admin_pass
        self.timeout = testsetup.timeout
        self.wait = ui.WebDriverWait(self.browser, self.timeout, poll_frequency=.5)


    def click_by_css(self, element, wait_for_element=None):
        try:
            elem = self.browser.find_element_by_css_selector(element)
        except:
            self.record_error()
            raise Exception(elem + "not found")
        
        elem.click()
        if wait_for_element:
            self.wait_for_element_present(wait_for_element)

    def click_link_text(self, text, wait_for_element=None):
        try:
            elem = self.browser.find_element_by_link_text(text)
        except:
            curr_page = self.record_error()
            raise Exception(("link text: {0} not found on current page: {1}").format(str(text), str(curr_page)))
        elem.click()
        if wait_for_element:
            self.wait_for_element_present(wait_for_element)

    def click_link_partial_text(self, text, wait_for_element=None):
        try:
            elem = self.browser.find_element_by_partial_link_text(text)
        except:
            curr_page = self.record_error()
            raise Exception(("partial link text: {0} not found on current page: {1}").format(str(text), str(curr_page)))
        elem.click()
        if wait_for_element:
            self.wait_for_element_present(wait_for_element)

    def type_by_css(self, element, text):
        elem = self.browser.find_element_by_css_selector(element)
        elem.send_keys(text)

    def get_text_by_css(self, element):
        return self.browser.find_element_by_css_selector(element).text

    def get_size_by_css(self, element):
        return self.browser.find_element_by_css_selector(element).size

    def submit_form_text_by_css(self, element, text):
        elem = self.browser.find_element_by_css_selector(element)
        elem.send_keys(text)
        elem.submit()    

    def is_element_present(self, element):
        try:
            elements_found = self.browser.find_elements_by_css_selector(element)
        except NoSuchElementException():
            return False
        if len(elements_found) > 0:
            return True
        else:
            return False

    def is_element_visible(self, element):
        if not self.is_element_present(element):
            return False
        else:
            return any([e.is_displayed() for e in
                        self.browser.find_elements_by_css_selector(element)])

    def is_unique_text_present(self, element, text):
        try:
            elements_found = self.browser.find_elements_by_css_selector(element)
        except NoSuchElementException():
            return False
        if len(elements_found) > 1:
            raise Exception(MULTIPLE_ELS % element)
        else:
            element_text = self.browser.find_element_by_css_selector(element).text
            if str(element_text) == text:
                return True
            else:
                return False
            
    def is_text_present(self, element, text):
        try:
            elements_found = self.browser.find_elements_by_css_selector(element)
        except NoSuchElementException():
            return False
        for elem in elements_found:
            if text == elem.text:
                return True
            else:
                return False

    def verify_text_present(self, element, text):
        elements_found = self.browser.find_elements_by_css_selector(element)
        if len(elements_found) > 1:
            raise Exception(MULTIPLE_ELS % element)
        else:
            element_text = self.browser.find_element_by_css_selector(element).text()
            if str(element_text) == text:
                return True
            else:
                self.record_error()
                raise Exception('found:' +element_text+ 'but was expecting: '+text)
                return False


    def wait_for_element_present(self, element):
        for i in range(60):
            try:
                time.sleep(1)
                if self.is_element_present(element): break
            except: pass
        else:
            raise Exception("Element %s is not present." % element)                   

  
    def wait_for_element_not_present(self, element):
        for i in range(60):
            try:
                time.sleep(1)
                if self.is_element_present(element) == False: break
            except: pass
        else:
            raise Exception("%s is still present" % element)

    def wait_for_text_not_present(self, text):
        for i in range(60):
            try:
                time.sleep(1)
                if self.is_text_present(text) == False: break
            except: pass
        else:
            raise Exception("%s is still present" % text)

    def wait_for_element_visible(self, element):
        for i in range(60):
            time.sleep(0.5)
            if self.is_element_visible(element):
                break
        else:
            self.record_error()
            raise Exception(element + ' has not appeared')

    def wait_for_element_not_visible(self,element):
        for i in range(30):
            try:
                time.sleep(1)
                self.browser.find_elements_by_css_selector(element).is_displayed()
            except: break
        else:
            self.record_error()
            raise Exception(element + ' has not disappeared')


    def get_absolute_url(self, url):
        if url.startswith("http"):
            full_url = url
        else:
            full_url = self.base_url + url
        return full_url


    def get_attr(self, element, attr):
        try:
            elements_found = self.browser.find_elements_by_css_selector(element)
        except NoSuchElementException:
            raise Exception("%s does not exist on the page" % element)

        if len(elements_found) > 1:
            raise Exception(MULTIPLE_ELS % element)

        return elements_found[0].get_attribute(attr)


    def open_page(self, url):
        self.browser.get(self.get_absolute_url(url))


    def go_back(self):
        self.browser.back()

    def page_down(self, elements):
        """elements are a list not a single element to try to page down.

        """
        if not isinstance(elements, basestring):
            for x in elements:
                if self.is_element_present(x):
                    elem = self.browser.find_element_by_css_selector(x)
                    break
        else:
            if self.is_element_present(elements):
                elem = self.browser.find_element_by_css_selector(elements)
        elem.send_keys("PAGE_DOWN")
       

    def record_error(self):
        """
            Records an error. 
        """

        http_matches = http_regex.match(self.base_url)
        file_name = http_matches.group(1)

        print '-------------------'
        print 'Error at ' + self.browser.current_url
        print '-------------------'
        filename = file_name + '_' + str(time.time()).split('.')[0] + '.png'

        print 'Screenshot of error in file ' + filename
#        f = open(filename, 'wb')
        self.browser.get_screenshot_as_file(filename)
#        f.close()
        return self.browser.current_url
