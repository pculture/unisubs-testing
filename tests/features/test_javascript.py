import unittest
from base_test_case import BaseTestCase
from html.js_test_page import JsTestPage

class TestJavascript(BaseTestCase):
    def test_javascript(self):
        page = JsTestPage()
        page.open()
        page.click_start()
        self.assertEquals(0, page.num_failed_tests())


if __name__ == "__main__":
    unittest.main()
