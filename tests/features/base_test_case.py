import unittest


class BaseTestCase(unittest.TestCase):       

    def setUp(self):
        print " - starting: ",self.shortDescription()
        
      
    def tearDown(self):
        print " - completed: ",self.id()
        
