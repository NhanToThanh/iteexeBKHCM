import testing.selenium.unittest
from selenium import webdriver


class TestOpenBrowser(testing.selenium.unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def testOpen(self):
        self.browser.get('http://www.ubuntu.com/')
        self.assertIn('Ubuntu', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    testing.selenium.unittest.main(verbosity=2)