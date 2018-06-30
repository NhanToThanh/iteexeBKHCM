# -*- coding: utf-8 -*-

"""
testcase2 is responsible for creating the package for the testing
of the eXe's Sequencing Feature.

The order of the lessons in this package:
Bài 1 => Bài 2 => Bài 4 => Bài 3 => Bài 5: Tổng kết


Structure:

        # testcase3
        #         |_Bài 1: Mở đầu
        #         |_Bài 2
        #         |_Bài 3
        #         |_Bài 4
        #         |_Bài 5: Tổng kết

"""

import unittest
from selenium.webdriver.common.keys import Keys
from js import extjs
from exe.engine.path import toUnicode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class TestCase4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testcase4(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()

        ################################      Open Package rawdatascormtest     #########################################
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="accesskey_button-1010"]').click()
        time.sleep(0.5)

        clickopen = driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1014-itemEl"]').click()
        lsthome = driver.find_elements_by_xpath('//button[contains(@class, "x-btn-center")]')

        #lsthome[13] == Home folder
        lsthome[13].click()


        lstTextBox = driver.find_elements_by_xpath('//input[contains(@type, "text")]')
        time.sleep(0.5)
        lstTextBox[1].send_keys('rawdata.elp')
        time.sleep(0.5)

        ### lstBtn is a Open button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[4].click()
        time.sleep(5)
        ################################      Open Package rawdatascormtest     #########################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ##############################     Rename rawdata to testcase4     ################################
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
            if namenode == 'rawdata':
                node.click()
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.BACKSPACE * 7)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'testcase4')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ##############################     Rename rawdata to testcase2     ################################
        time.sleep(0.1)

        #####################     Add Sequencing Config for Bài 1      ########################
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
            if namenode == u'Bài 1: Mở đầu':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon

                btnSave = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1

                postConditionTab = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('5')
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        #####################     Add Sequencing Config for Bài 1      ########################

        #####################     Add Sequencing Config for Bài 2      ########################
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
            if namenode == u'Bài 2':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == u"   Bài 4 ( 3 Quiz)":
                        option.click()
                        postConditionTab = driver.find_elements_by_xpath(
                            '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                        postConditionTab[1].click()
                        time.sleep(1)

                        passanyquiz = driver.find_element_by_xpath('//input[contains(@id, "anycon-inputEl")]').click()

                        time.sleep(1)
                        btnSave.click()
                        stopvent = 10

                stopvent = 10

        #####################     Add Sequencing Config for Bài 2      ########################

        #####################     Add Sequencing Config for Bài 3      ########################
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
            if namenode == u'Bài 3':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == u"   Bài 1: Mở đầu":
                        time.sleep(1)
                        option.click()
                        postConditionTab = driver.find_elements_by_xpath(
                            '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                        postConditionTab[1].click()
                        time.sleep(1)

                        passanyquiz = driver.find_element_by_xpath('//input[contains(@id, "anycon-inputEl")]').click()

                        time.sleep(1)
                        btnSave.click()
                        stopvent = 10

        #####################     Add Sequencing Config for Bài 3      ########################

        #####################     Add Sequencing Config for Bài 4      ########################
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
            if namenode == u'Bài 4':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == u"   Bài 3 ( 3 Quiz)":
                        option.click()
                        postConditionTab = driver.find_elements_by_xpath(
                            '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                        postConditionTab[1].click()
                        time.sleep(1)

                        passanyquiz = driver.find_element_by_xpath('//input[contains(@id, "anycon-inputEl")]').click()

                        time.sleep(1)
                        btnSave.click()
                        stopvent = 10

                stopvent = 10

        #####################     Add Sequencing Config for Bài 4      ########################

        #####################     Add Sequencing Config for Bài 5: Tổng kết      ########################
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
            if namenode == u'Bài 5: Tổng kết':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath(
                    '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == u"   Bài 2 ( 3 Quiz)":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        #####################     Add Sequencing Config for Bài 5: Tổng kết      ########################


        ##################################      Export Package as SCORM     ############################################
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="accesskey_button-1010"]').click()
        time.sleep(0.5)
        hoverexport = ActionChains(driver).move_to_element(
            driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1037-itemEl"]')).perform()
        time.sleep(0.5)
        hoveredu = ActionChains(driver).move_to_element(
            driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1039-itemEl"]')).perform()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1043"]').click()
        time.sleep(0.5)

        lstTextBox = driver.find_elements_by_xpath('//input[contains(@type, "text")]')
        lstTextBox[2].send_keys('testcase4')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()

        ##################################      Export Package as SCORM     ############################################
        time.sleep(2)

        ### Begin SCORM Cloud
        driver.get("https://cloud.scorm.com/sc/user/Library")

        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            #alert = browser.switch_to.alert
            #alert.accept()
            time.sleep(2)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        time.sleep(10)


        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)

        #time.sleep(0.5)
        #lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        id = driver.find_element_by_xpath('//input[contains(@type, "email")]')
        id.send_keys("tothanhnhan19961@gmail.com")
        time.sleep(1)
        password = driver.find_element_by_xpath('//input[contains(@type, "password")]')
        password.send_keys("2w97b8bxz0!!!@")
        time.sleep(3)
        login = driver.find_element_by_xpath('//input[contains(@type, "submit")]').click()

        #login = driver.find_element_by_xpath('//input[contains(@type, "submit")]').click()
        #login.click()
        time.sleep(5)
        #time.sleep(1)

        ##### Wait to login and click the library
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable,
                                             (By.XPATH, '//a[contains(@href, "/sc/user/Library")]'))

            driver.find_element_by_xpath('//a[contains(@href, "/sc/user/Library")]').click()
        except TimeoutException:
            print("Cannot login")
        ##### Wait to login and click the library

        time.sleep(1)
        addContent = driver.find_element_by_xpath('//a[contains(@class, "dropdown-toggle btn-success")]').click()
        time.sleep(1)
        importScorm = driver.find_element_by_xpath('//a[contains(@href, "/sc/user/authoring/UploadCourse")]').click()
        #chooseFile = driver.find_element_by_xpath('//input[contains(@id, "lib_importForm_fileToImport")]').click()
        time.sleep(1)
        #chooseFile = driver.find_element_by_xpath('//input[contains(@id, "lib_importForm_fileToImport")]').send_keys("/home/thanhnhan/SCORM_Test/sequencingtopdown.zip")
        chooseFile = driver.find_element_by_xpath('//input[contains(@id, "lib_importForm_fileToImport")]').send_keys("/home/thanhnhan/testcase4.zip")
        time.sleep(1)
        importButton = driver.find_element_by_xpath('//button[contains(@id, "startImportButton")]').click()
        time.sleep(20)

        # Reset Global
        driver.find_element_by_xpath('//div[contains(@title, "Reset the Sandbox Globals for this Course")]').click()
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            #alert = browser.switch_to.alert
            #alert.accept()
            time.sleep(2)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        time.sleep(10)

        # Reset Progress
        driver.find_element_by_xpath('//div[contains(@title, "Reset the Sandbox progress of this Course")]').click()
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            #alert = browser.switch_to.alert
            #alert.accept()
            time.sleep(2)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        time.sleep(10)

        ##### Wait to lunch the course
        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable,
                                             (By.XPATH, '//div[contains(@title, "Launch this course in the Sandbox")]'))

            driver.find_element_by_xpath('//div[contains(@title, "Launch this course in the Sandbox")]').click()
        except TimeoutException:
            print("Cannot launch the course")
        ##### Wait to lunch the course


       ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 2")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 3")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 4")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 5: Tổng kết")]').click()
        ###################################     Disable     #######################################

        ### Click Bài 1: Mở đầu
        time.sleep(1)
        begin = driver.find_element_by_xpath('//li[contains(@title, "Bài 1: Mở đầu")]').click()
        time.sleep(1)
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            time.sleep(2)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        ### Click Bài 1: Mở đầu


       ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 2")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 4")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Bài 5: Tổng kết")]').click()
        time.sleep(1)

        ###################################     Disable     #######################################

        ### Click Bài 3
        begin = driver.find_element_by_xpath('//li[contains(@title, "Bài 3")]').click()
        time.sleep(2)
        ### Click Bài 3


        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_element_by_xpath('//iframe[contains(@title, "Bài 3")]')
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        #################################     Learn Quiz (Bai 3)     #####################################

        ### Test 1
        time.sleep(1)
        cau1 = driver.find_element_by_xpath('//input[contains(@id, "key0b41")]').click()
        time.sleep(1)
        cau2 = driver.find_element_by_xpath('//input[contains(@id, "key1b41")]').click()
        time.sleep(1)

        ### Submit
        time.sleep(1)
        submit = driver.find_element_by_xpath('//input[contains(@onclick, "calcScore21()")]').click()

        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            # alert = browser.switch_to.alert
            # alert.accept()
            time.sleep(3)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        ### Submit

        ### Test 1

        #################################     Learn Quiz  (Bai 3)    #####################################

        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)

        ### Click Bài 4
        time.sleep(1)
        begin = driver.find_element_by_xpath('//li[contains(@title, "Bài 4")]').click()
        time.sleep(2)
        ### Click Bài 4


        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_element_by_xpath('//iframe[contains(@title, "Bài 4")]')
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        #################################     Learn Quiz (Bai 4)     #####################################

        ### Test 1
        time.sleep(1)
        cau1 = driver.find_element_by_xpath('//input[contains(@id, "key0b71")]').click()
        time.sleep(1)
        cau2 = driver.find_element_by_xpath('//input[contains(@id, "key1b72")]').click()
        time.sleep(1)

        ### Submit
        time.sleep(1)
        submit = driver.find_element_by_xpath('//input[contains(@onclick, "calcScore21()")]').click()

        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            # alert = browser.switch_to.alert
            # alert.accept()
            time.sleep(3)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        ### Submit

        ### Test 1

        #################################     Learn Quiz  (Bai 4)    #####################################

        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)

        ### Click Bài 2
        begin = driver.find_element_by_xpath('//li[contains(@title, "Bài 2")]').click()
        time.sleep(2)
        ### Click Bài 2

        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_element_by_xpath('//iframe[contains(@title, "Bài 2")]')
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        #################################     Learn Quiz (Bai 2)     #####################################

        ### Test 1
        time.sleep(1)
        cau1 = driver.find_element_by_xpath('//input[contains(@id, "key0b11")]').click()
        time.sleep(1)
        cau2 = driver.find_element_by_xpath('//input[contains(@id, "key1b11")]').click()
        time.sleep(1)

        ### Submit
        time.sleep(1)
        submit = driver.find_element_by_xpath('//input[contains(@onclick, "calcScore21()")]').click()

        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            # alert = browser.switch_to.alert
            # alert.accept()
            time.sleep(3)
            driver.switch_to.alert.accept()
        except TimeoutException:
            print("No alert")
        ### Submit

        ### Test 1


        #################################     Learn Quiz  (Bai 2)    #####################################

        ### Click Bài 5: Tổng kết
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(1)
        begin = driver.find_element_by_xpath('//li[contains(@title, "Bài 5: Tổng kết")]').click()
        time.sleep(5)
        ### Click Bài 5: Tổng kết

        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_element_by_xpath('//iframe[contains(@title, "Bài 5: Tổng kết")]')
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        #################################     Learn Scorm Test     #####################################

        ### Test
        time.sleep(5)
        cau1 = driver.find_element_by_xpath('//input[contains(@id, "question_question_7_0")]').click()
        time.sleep(1)
        cau2 = driver.find_element_by_xpath('//input[contains(@id, "question_question_3_1")]').click()
        time.sleep(1)
        cau3 = driver.find_element_by_xpath('//input[contains(@id, "question_question_1_1")]').click()
        time.sleep(1)
        cau4 = driver.find_element_by_xpath('//input[contains(@id, "question_question_2_1")]').click()
        time.sleep(1)
        cau5 = driver.find_element_by_xpath('//input[contains(@id, "question_question_4_1")]').click()
        time.sleep(1)
        cau6 = driver.find_element_by_xpath('//input[contains(@id, "question_question_5_0")]').click()
        time.sleep(1)
        cau7 = driver.find_element_by_xpath('//input[contains(@id, "question_question_6_0")]').click()
        time.sleep(1)
        cau8 = driver.find_element_by_xpath('//input[contains(@id, "question_question_8_0")]').click()
        time.sleep(1)
        cau9 = driver.find_element_by_xpath('//input[contains(@id, "question_question_10_0")]').click()
        time.sleep(1)
        cau10 = driver.find_element_by_xpath('//input[contains(@id, "question_question_9_1")]').click()

        ### Submit
        time.sleep(1)
        submit = driver.find_element_by_xpath('//input[contains(@onclick, "SubmitAnswers();")]').click()


        #################################     Learn Scorm Test     #####################################
        time.sleep(3)
        driver.switch_to_default_content()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()