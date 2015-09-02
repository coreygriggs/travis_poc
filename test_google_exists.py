import unittest
from selenium import webdriver
from os import environ

class TestGoogleWorks(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Remote(command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub'
                                        % (environ['SAUCE_USERNAME'], environ['SAUCE_ACCESS_KEY']),
                                        desired_capabilities={'browserName': 'firefox', 'platform': 'linux',
                                                              'version': '40.0'})
    def test_google_exists(self):
        self.browser.get('http://google.com')
        self.assertEqual(self.browser.title, 'Google')

    def tearDown(self):
        self.browser.quit()

if __name__ in ('main', '__main__'):
    unittest.main()
