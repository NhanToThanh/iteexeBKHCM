import testing.selenium.unittest
from selenium.webdriver.common.keys import Keys
from js import extjs
from exe.engine.path import toUnicode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


class PythonOrgSearch(testing.selenium.unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("localhost:51235")

        time.sleep(1)



        #element = wait.until(
        #       EC.element_to_be_clickable((By.XPATH, '//*[@id="button-2520"]'))
        #  )

        #element1 = wait.until(
        #       EC.element_to_be_clickable((By.XPATH, '//*[@id="button-1005-btnInnerEl"]'))
        #   )

        #element = WebDriverWait(driver, 10).until(
        #    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="messagebox-1001-testfield-inputEl"]'))
        #)

        # Find AddPage button
       # addPage = driver.find_element_by_css_selector("#button-2520")



        #addPage.click()


        ###########################     RENAME THE ROOT INTO PackageTD      ########################################
        time.sleep(0.1)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Home':
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.BACKSPACE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('PackageTD')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###########################     RENAME THE ROOT INTO PackageTD      ########################################


        ##########################################     Create Chuong1      #############################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2520"]').click()
        time.sleep(0.1)
        ##########################################     Create Chuong1      #############################################


        ##########################################     RENAME Chuong1      #############################################
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Topic':
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Chuong1')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ##########################################     RENAME Chuong1      #############################################


        ###########################################     Create Bai 1      ##############################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2520"]').click()
        time.sleep(0.1)
        ###########################################     Create Bai 1      ##############################################

        ###########################################     RENAME Bai 1      ##############################################
        time.sleep(0.1)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Section':
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 7)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Bai1')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###########################################     RENAME Bai 1      ##############################################

        ###########################################     CREATE Bai 2      ##############################################
        time.sleep(0.1)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Chuong1':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2520"]').click()
                stopvent = 10
        ###########################################     CREATE Bai 2      ##############################################


        ###########################################     RENAME Bai 2      ##############################################
        time.sleep(0.1)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Section':
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 7)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Bai2')      ## Doi ten bai 2
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###########################################     RENAME Bai 2      ##############################################



        time.sleep(0.1)

        xxx = driver.find_element_by_xpath('//*[@id="treeview-2526"]/table/tbody/tr[1]')


        zzz = driver.find_elements_by_xpath('//div[contains(@class, "x-tree-icon x-tree-icon-inline")]')



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

