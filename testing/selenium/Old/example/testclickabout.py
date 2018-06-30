import testing.selenium.unittest
from js import extjs
from exe.engine.path import toUnicode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver     import ActionChains


class PythonOrgSearch(testing.selenium.unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("localhost:51235")
        wait = WebDriverWait(driver, 7)
        #extjs.basic.need()


        element = wait.until(
               EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-2520"))
           )

        addPage = driver.find_element_by_css_selector("#button-2520")


        #actionChains.context_click(addPage).perform()
        addPage.click()

        xxx = driver.find_element_by_xpath('//*[@id="treeview-2526"]/table/tbody/tr[1]')
        yyy = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')

        zzz = driver.find_elements_by_xpath('//div[contains(@class, "x-tree-icon x-tree-icon-inline")]')

        for e in yyy:
            texttt = toUnicode(e.text, e.text)
            if texttt == 'Home':
                actionChains = ActionChains(driver)
                actionChains.context_click(e).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

        a = 1


        # self.assertIn("eXe Learning", driver.title)
        # driver.find_element_by_id('accesskey_button-1061-btnEl').click()
        #driver.find_element_by_css_selector("#accesskey_button-1076").click()
        a = 1
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    testing.selenium.unittest.main()

