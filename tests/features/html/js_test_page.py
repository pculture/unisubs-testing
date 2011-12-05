from page import Page
import time
import re

class JsTestPage(Page):
    def open(self):
        print("Opening /jstest/alltests")
        self.open_page("jstest/alltests")
      
    def click_start(self):
        print("Waiting for Start button to appear")
        BUTTON_CSS = ".goog-testrunner-buttons button:first-child"
        self.wait_for_element_present(BUTTON_CSS)
        print("Clicking Start button")
        self.click_by_css(BUTTON_CSS)

    def num_failed_tests(self):
        PROG_CSS = ".goog-testrunner-progress-summary"
        print("Waiting for tests to finish running")
        self.wait_for_element_present(PROG_CSS)
        matches = None
        for x in range(60):           
            text = self.get_text_by_css(PROG_CSS)
            matches = re.search(r"(\d+) failed", text)
            if matches is not None:
                break
            time.sleep(1)
        if matches is None:
            raise Exception("Tests never finished running :(")
        else:
            return int(matches.group(1))
