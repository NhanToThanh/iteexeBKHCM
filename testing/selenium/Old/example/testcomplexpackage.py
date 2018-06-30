import testing.selenium.unittest
from selenium.webdriver.common.keys import Keys
from js import extjs
from exe.engine.path import toUnicode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time


class PackageWithPrecondition(testing.selenium.unittest.TestCase):

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

        ####################################     Rename The Root Into PackageTD      ###################################
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
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Package1')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     Rename The Root Into PackageTD      ###################################


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

        ###########################################     CREATE Bai 3      ##############################################
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
        ###########################################     CREATE Bai 3      ##############################################


        ###########################################     RENAME Bai 3      ##############################################
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
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Bai3')      ## Doi ten bai 3
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###########################################     RENAME Bai 3      ##############################################


        ###################################     Add Sequencing Config Bai 1      #######################################
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
            if namenode == 'Bai1':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()
                driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                #lstjson = driver.find_element_by_xpath('//div[contains(@class, "x-boundlist-list-ct")]')
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   Chuong1":
                        option.click()
                        btnSave.click()
                        stopvent = 10

        ###################################     Add Sequencing Config Bai 1      #######################################


        ###################################     Add Sequencing Config Bai 2      #######################################
        time.sleep(0.5)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Bai2':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                time.sleep(0.1)
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                #lstjson = driver.find_element_by_xpath('//div[contains(@class, "x-boundlist-list-ct")]')
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "      Bai1":
                        option.click()
                        btnSave.click()
                        stopvent = 10

        ###################################     Add Sequencing Config Bai 2      #######################################


        ###################################     Add Sequencing Config Bai 3      #######################################
        time.sleep(0.5)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.1)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == 'Bai3':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                time.sleep(0.1)
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                #lstjson = driver.find_element_by_xpath('//div[contains(@class, "x-boundlist-list-ct")]')
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "      Bai2":
                        option.click()
                        btnSave.click()
                        stopvent = 10

        ###################################     Add Sequencing Config Bai 3      #######################################


        ##################################      Export Package as SCORM     ############################################
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="accesskey_button-1010"]').click()
        time.sleep(0.5)
        hoverexport = ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1037-itemEl"]')).perform()
        time.sleep(0.5)
        hoveredu = ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1039-itemEl"]')).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1043"]').click()
        time.sleep(0.5)


        lstTextBox = driver.find_elements_by_xpath('//input[contains(@type, "text")]')
        lstTextBox[2].send_keys('PackageWithPreconditon')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()

        ##################################      Export Package as SCORM     ############################################



        #xxx = driver.find_element_by_xpath('//*[@id="treeview-2526"]/table/tbody/tr[1]')
        #zzz = driver.find_elements_by_xpath('//div[contains(@class, "x-tree-icon x-tree-icon-inline")]')

        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    testing.selenium.unittest.main()

