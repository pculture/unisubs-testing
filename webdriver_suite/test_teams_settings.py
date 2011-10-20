import unittest
from base_test_case import BaseTestCase
import testsetup
from html.unisubs_page import UnisubsPage

class TestTeamsSettingsBasic(BaseTestCase):
    '''Tests for Unisubs basic team settings.'''

    def test_panels_display(self):
        try:
            p = UnisubsPage()

            p.open_page('teams/')
            p.log_in(testsetup.admin_user, testsetup.admin_pass)
            p.click_link_partial_text(testsetup.team['name'])
            p.click_link_partial_text("Manager's Settings")

            self.assertTrue(p.is_element_visible('.panel-basic'))
            self.assertFalse(p.is_element_visible('.panel-project'))
            self.assertFalse(p.is_element_visible('.panel-tasks'))

            p.click_link_text('Projects')
            p.wait_for_element_visible('.panel-project')

            self.assertFalse(p.is_element_visible('.panel-basic'))
            self.assertTrue(p.is_element_visible('.panel-project'))
            self.assertFalse(p.is_element_visible('.panel-tasks'))

            p.click_link_text('Tasks')
            p.wait_for_element_visible('.panel-tasks')

            self.assertFalse(p.is_element_visible('.panel-basic'))
            self.assertFalse(p.is_element_visible('.panel-project'))
            self.assertTrue(p.is_element_visible('.panel-tasks'))
        except:
            p.record_error()
            raise

    def test_basic_settings(self):
        try:
            p = UnisubsPage()

            p.open_page('teams/')
            p.log_in(testsetup.admin_user, testsetup.admin_pass)
            p.click_link_partial_text(testsetup.team['name'])
            p.click_link_partial_text("Manager's Settings")

            self.assertTrue(p.is_element_visible('.panel-basic'))

            # TODO: Check more things.
        except:
            p.record_error()
            raise

if __name__ == "__main__":
    unittest.main()

