# -*- coding: utf-8 -*-
import unittest
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


class PackageWithPrecondition(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()
        time.sleep(0.5)

        time.sleep(1)



        ################################     Rename The Root Into sequencingwithquiz      ###############################

        time.sleep(0.5)
        lstnode = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner")]')
        time.sleep(0.5)
        stopvent = 1
        for node in lstnode:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namenode = toUnicode(node.text, node.text)
            time.sleep(0.1)
            if namenode == u'Home':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    Keys.BACKSPACE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    'sequencingwithquiz')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ################################     Rename The Root Into sequencingwithquiz      ###############################


        ##########################################     Create Chuong1      #############################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2519"]').click()
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
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Chuong1')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ##########################################     RENAME Chuong1      #############################################


        ###########################################     Create Bai 1      ##############################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2519"]').click()
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
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 7)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Bai1')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###########################################     RENAME Bai 1      ##############################################


        ######################################     Add Test 1 for Bai 1      #########################################
        stopvent = 1
        lstGroupIdevice = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-group-title")]')
        for groupIdevice in lstGroupIdevice:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namegroup = toUnicode(groupIdevice.text, groupIdevice.text)
            time.sleep(0.1)
            if namegroup == 'Interactive Activities':
                groupIdevice.click()
                stopvent = 10

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.1)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(Keys.BACKSPACE * 10)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 1')


        question = driver.find_element_by_xpath('//div[contains(@id, "question0b0-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b0-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b01")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b0")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b0")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q0b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q0b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b0")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q0b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q0b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b0")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 1 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b0-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b0-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey1b02")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b0")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b0")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q1b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q1b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b0")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q1b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q1b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q1b0")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 2 Test 1################################################

        ##################################### Add Question 3 Test 1 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question3 = driver.find_element_by_xpath('//div[contains(@id, "question2b0-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q2b0-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q2b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey2b03")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b0")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q2b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q2b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b0")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q2b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q2b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b0")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q2b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q2b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q2b0")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 3 Test 1 ################################################

        ##################################### Add Question 4 Test 1 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question4 = driver.find_element_by_xpath('//div[contains(@id, "question3b0-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q3b0-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q3b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey3b04")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b0")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q3b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q3b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b0")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q3b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q3b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b0")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q3b0-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q3b0_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q3b0")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 4 Test 1 ################################################



        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 1 for Bai 1      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)


        ######################################     Add Test 2 for Bai 1      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 2')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b1-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b1-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b11")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b1")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b1")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q0b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q0b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b1")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q0b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q0b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b1")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b1-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b1-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey1b12")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b1")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b1")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q1b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q1b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b1")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q1b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q1b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q1b1")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 2 Test 2 ################################################

        ##################################### Add Question 3 Test 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question3 = driver.find_element_by_xpath('//div[contains(@id, "question2b1-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q2b1-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q2b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey2b13")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b1")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q2b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q2b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b1")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q2b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q2b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b1")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q2b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q2b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q2b1")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 3 Test 2 ################################################

        ##################################### Add Question 4 Test 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question4 = driver.find_element_by_xpath('//div[contains(@id, "question3b1-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q3b1-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q3b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey3b14")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b1")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q3b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q3b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b1")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q3b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q3b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b1")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q3b1-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q3b1_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q3b1")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 4 Test 2 ################################################



        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 2 for Bai 1      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 3 for Bai 1      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 3')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b2-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b2-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b21")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b2")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b2")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q0b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q0b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b2")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q0b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q0b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b2")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b2-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b2-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey1b22")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b2")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b2")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q1b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q1b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b2")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q1b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q1b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q1b2")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 2 Test 2 ################################################

        ##################################### Add Question 3 Test 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question3 = driver.find_element_by_xpath('//div[contains(@id, "question2b2-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q2b2-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q2b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey2b23")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b2")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q2b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q2b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b2")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q2b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q2b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b2")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q2b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q2b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q2b2")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 3 Test 2 ################################################

        ##################################### Add Question 4 Test 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "Add another Question")]').click()
        time.sleep(0.5)

        ######$$$$$$$$$$$$
        question4 = driver.find_element_by_xpath('//div[contains(@id, "question3b2-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        #xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        #driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cho đoạn mã viết bằng ngôn ngữ C sau: \ni = a = b * 34 + c5; \nHỏi bộ phân tích từ vựng sẽ lần lượt trả về bao nhiêu tokens cho đoạn mã trên ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q3b2-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q3b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('10')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey3b24")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b2")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q3b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q3b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('6')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b2")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q3b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q3b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys('9')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b2")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q3b2-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q3b2_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một giá trị khác')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q3b2")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################


        ##################################### Add Question 4 Test 2 ################################################



        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 3 for Bai 1      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)


        ###########################################     CREATE Bai 2      ##############################################
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
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
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
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
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
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
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
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
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
            if namenode == 'Bai1 ( 1 Quiz)':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequencing config":
                        seqele.click()

                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   Chuong1":
                        option.click()
                        ### Add Post Condition
                        postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                        postConditionTab[1].click()
                        timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                        timeTextBox.send_keys('5')
                        a = 1
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
                    if seqtext == "Sequencing config":
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
                    if optionname == "      Bai1 (Quiz)":
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
                    if seqtext == "Sequencing config":
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
        lstTextBox[2].send_keys('PackageWithQuiz')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()

        ##################################      Export Package as SCORM     ############################################


        time.sleep(1)


    def tearDown(self):
        self.driver.close()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()

