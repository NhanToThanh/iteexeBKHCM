# -*- coding: utf-8 -*-
"""
rawdata is responsible for creating the raw data for the testing
of the eXe's Sequencing Feature.


Structure:

        # rawdata
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
from selenium.webdriver.support.ui import Select
import time


class RawData(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rawdata(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()

        ################################     Rename The Root Into rawdata      ###############################

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
            if namenode == 'Home':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    Keys.BACKSPACE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    'rawdata')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ################################     Rename The Root Into rawdata      ###############################

        ##############################     Create Bài 1: Mở đầu     ################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2519"]').click()
        time.sleep(0.1)
        ##############################     Create Bài 1: Mở đầu     ################################

        ##############################     Rename Bài 1: Mở đầu     ################################
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
            if namenode == 'Topic':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Bài 1: Mở đầu')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ##############################     Rename Bài 1: Mở đầu    ################################
        time.sleep(0.1)

        #########################     Add Data for Bài 1: Mở đầu      ##############################
        stopvent = 1
        lstGroupIdevice = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-group-title")]')
        for groupIdevice in lstGroupIdevice:
            if stopvent == 10:
                break
            time.sleep(0.1)
            namegroup = toUnicode(groupIdevice.text, groupIdevice.text)
            time.sleep(0.1)
            if namegroup == 'Textual Information':
                groupIdevice.click()
                stopvent = 10

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'Free Text':
                idevice.click()
                stopvent = 10

        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        ###############################################  Enter TextArea  ###############################################
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        ##################################################  TextArea  ##################################################
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u"""Bài 1: Mở đầu giới thiệu sơ lược về khóa học, học viên cần dành tối thiểu 5s tại đây để hoàn thành bài hoc.""")
        time.sleep(0.5)
        ##################################################  TextArea  ##################################################


        ########################################## Submit FreeText #####################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ########################################## Submit FreeText #####################################################

        #########################     Add Data for Bài 1: Mở đầu     ##############################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ###############################     Create Bài 2      ################################
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
            if namenode == u'rawdata':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ###############################     Create Bài 2      ################################

        ###############################     Rename Bài 2      ################################
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
            if namenode == 'Topic':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Bài 2')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###############################     Rename Bài 2      ################################
        time.sleep(0.1)

        ##########################     Add Data for Bài 2      ###############################

        ######################################     Add QuizTest for II. Câu hỏi ôn tập      #########################################

        ######################################     Add Test 1 for II. Câu hỏi ôn tập      #########################################
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
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 1')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b1-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Cao độ là gì ?')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Mức độ trầm bổng của âm thanh. (T)')

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Mức độ ngắn dài của âm thanh.')
        ##################################### Add option 2 ################################################


        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b1")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b1-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Mức độ ngắn dài của âm thanh là gì ?')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Trường độ (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Medium)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "mkey1b12")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Medium)

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Cao độ')
        ##################################### Add option 2 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b1")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 1################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 1 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 2 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 2')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b2-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Trường độ là gì ?')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Mức độ ngắn dài của âm thanh. (T)')

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Độ mạnh các nốt nhạc.')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        ## Ý thứ 2 đúng     0 -> ý 1
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
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Ví dụ về Cường độ âm thanh là ? ')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Tiếng thác chảy. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey1b22")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)


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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Tiếng đồng hồ.')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b2")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 2 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 3')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b3-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Tiếng thác chảy mô tả :')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b3-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Cao độ')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b31")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b3")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Cường độ (T)')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        ## Ý thứ 2 đúng     0 -> ý 1
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q0b3")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b3-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Định nghĩa đúng về âm sắc là ? ')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b3-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Những âm thanh khác nhau về cường độ.')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey1b32")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)


        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b3")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Những âm thanh giống nhau về Cao độ, Trường độ, Cường độ nhưng chúng khác nhau về âm sắc. (T)')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q1b3")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################


        ##########################     Add Data for Bài 2      ###############################
        driver.switch_to_default_content()
        time.sleep(0.5)


        #########################################     Create Bài 3      ############################################
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
            if namenode == u'rawdata':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        #########################################     Create Bài 3      ############################################

        #########################################     Rename Bài 3      ############################################
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
            if namenode == 'Topic':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(u'Bài 3')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #########################################     Rename Bài 3      ############################################

        time.sleep(0.1)
        ##########################     Add Data for Bài 3      ###############################

        ######################################     Add QuizTest for II. Câu hỏi ôn tập      #########################################

        ######################################     Add Test 1 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 4')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b4-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Khuông nhạc dùng để biểu diễn ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b4-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Các thông tin về bản nhạc. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b41")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b4")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Độ mạnh yếu các nốt nhạc.')
        ##################################### Add option 2 ################################################


        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b4")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b4-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Số dòng kẻ trong một khuông nhạc là :')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b4-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'4')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Medium)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "mkey1b42")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Medium)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b4")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'5 (T)')
        ##################################### Add option 2 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q1b4")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 1################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 1 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 2 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 5')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b5-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Giữa các dòng kẻ gọi là ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b5-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Dấu hóa.')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b51")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b5")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Khe nhạc. (T)')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        ## Ý thứ 2 đúng     0 -> ý 1
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q0b5")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b5-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vị trí các khe nhạc nằm ở ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b5-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Giữa các dòng kẻ nhạc. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey1b52")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)


        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b5")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Trong một bản nhạc.')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b5")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 2 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 6')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b6-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Các thông tin về bản nhạc được biểu diễn bằng ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b6-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b6_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Khuông nhạc. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b61")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b6")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b6-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b6_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Nốt nhạc.')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        ## Ý thứ 2 đúng     0 -> ý 1
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b6")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b6-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Nốt Do nằm ở vị trí thứ ? ')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b6-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b6_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'1 (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey1b62")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)


        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b6")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b6-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b6_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'2')
        ##################################### Add option 2 ################################################


        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b6")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################



        ##########################     Add Data for Bài 3      ###############################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ###############################     Create Bài 4     ################################
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
            if namenode == u'rawdata':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ###############################     Create Bài 4      ################################

        ###############################     Rename Bài 4      ################################
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
            if namenode == 'Topic':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Bài 4')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###############################     Rename Bài 4      ################################
        time.sleep(0.1)

        ##########################     Add Data for Bài 4      ###############################

        ######################################     Add QuizTest for 4      #########################################

        ######################################     Add Test 1 for 4      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 7')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b7-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Các loại sáo có thể là ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b7-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b7_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Sáo ngang (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b71")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b7")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b7-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b7_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Sáo nghiên')
        ##################################### Add option 2 ################################################


        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b7")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b7-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Điểm khác biệt cơ bản giữa sáo dọc và sáo tiêu là :')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b7-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b7_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Người sử dụng')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Medium)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "mkey1b72")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Medium)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b7")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b7-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b7_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Kích thước. (T)')
        ##################################### Add option 2 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q1b7")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 1################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 1 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 2 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 8')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b8-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Các tông của sáo có tần âm cao là :')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b8-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b8_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Sol, Fa, Mi. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b81")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b8")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b8-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b8_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Do, Re, Mi.')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        ## Ý thứ 2 đúng     0 -> ý 1
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b8")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b8-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Sáo tiêu có phải là một loại sao hay không ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b8-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b8_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Có. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey1b82")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)


        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b8")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b8-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b8_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Không.')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b8")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 2 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Quiz':
                idevice.click()
                stopvent = 10

        vv = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.1)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        namequiz = driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(
            Keys.BACKSPACE * 10)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@value, "SCORM Quiz")]').send_keys(u'Test 9')
        time.sleep(0.5)

        question = driver.find_element_by_xpath('//div[contains(@id, "question0b9-viewer")]').click()
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Sáo ngáng và sáo dọc là:')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q0b9-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q0b9_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Nhạc lý.')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey0b91")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b9")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q0b9-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q0b9_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Nhạc cụ. (T)')
        ##################################### Add option 2 ################################################



        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        ## Ý thứ 2 đúng     0 -> ý 1
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q0b9")]').click()
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
        question2 = driver.find_element_by_xpath('//div[contains(@id, "question1b9-viewer")]').click()
        actionChains = ActionChains(driver)
        actionChains.double_click(question).perform()
        # xx = driver.find_element_by_xpath('//div[contains(@class, "mce-tinymce mce-container mce-panel")]')
        # driver.find_element_by_xpath('//div[contains(@class, "mce-edit-area mce-container mce-panel mce-stack-layout-item")]').send_keys('asasas')
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Loại sáo nào dành cho người mới bắt đầu ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q1b9-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q1b9_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Sáo đô c5. (T)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey1b92")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)


        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b9")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q1b9-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q1b9_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Sáo ngang.')
        ##################################### Add option 2 ################################################


        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b9")]').click()
        time.sleep(0.5)
        ### Check the correct answer #########################################################

        ##################################### Add Question 2 Test 2 ################################################


        ##################################### Submit Quiz #################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ##################################### Submit Quiz #################################################
        time.sleep(0.5)

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################



        ##########################     Add Data for Bài 3      ###############################
        driver.switch_to_default_content()
        time.sleep(0.5)


        ###############################     Create Bài 5: Tổng kết     ################################
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
            if namenode == u'rawdata':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ###############################     Create Bài 5: Tổng kết      ################################

        ###############################     Rename Bài 5: Tổng kết      ################################
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
            if namenode == 'Topic':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Bài 5: Tổng kết')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###############################     Rename Bài 5: Tổng kết      ################################
        time.sleep(0.1)

        ##########################     Add Data for Bài 5      ###############################

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            # time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            # time.sleep(0.1)
            if nameidevice == 'SCORM Test':
                idevice.click()
                stopvent = 10

        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################


        ##################################################  SCORM Test  ##################################################
        time.sleep(1)
        hardtest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 1hard")]').send_keys('1')
        time.sleep(1)
        mediumtest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 1med")]').send_keys('1')
        time.sleep(1)
        easytest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 1easy")]').send_keys('0')
        time.sleep(1)

        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 2hard")]').send_keys('1')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 2med")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 2easy")]').send_keys('1')
        time.sleep(1)

        hardtest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 3hard")]').send_keys('1')
        time.sleep(1)
        mediumtest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 3med")]').send_keys('0')
        time.sleep(1)
        easytest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 3easy")]').send_keys('1')
        time.sleep(1)

        time.sleep(1)
        hardtest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 4hard")]').send_keys('1')
        time.sleep(1)
        mediumtest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 4med")]').send_keys('1')
        time.sleep(1)
        easytest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 4easy")]').send_keys('0')
        time.sleep(1)

        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 5hard")]').send_keys('1')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 5med")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 5easy")]').send_keys('1')
        time.sleep(1)

        hardtest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 6hard")]').send_keys('0')
        time.sleep(1)
        mediumtest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 6med")]').send_keys('0')
        time.sleep(1)
        easytest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 6easy")]').send_keys('0')
        time.sleep(1)

        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 7hard")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 7med")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 7easy")]').send_keys('0')
        time.sleep(1)

        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 8hard")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 8med")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 8easy")]').send_keys('0')
        time.sleep(1)

        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 9hard")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 9med")]').send_keys('0')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 9easy")]').send_keys('0')
        time.sleep(1)

        ##################################################  TextArea  ##################################################

        ########################################## Submit FreeText #####################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ########################################## Submit FreeText #####################################################
        time.sleep(0.5)

        ##########################     Add Data for Bài 5      ###############################
        driver.switch_to_default_content()
        time.sleep(0.5)


        ##################################      Save Package as rawdata    ############################################
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="accesskey_button-1010"]').click()
        time.sleep(1)

        clicksaveas = driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1021-itemEl"]').click()
        time.sleep(1)
        lsthome = driver.find_elements_by_xpath('//button[contains(@class, "x-btn-center")]')

        time.sleep(1)
        #lsthome[13] == Home folder
        lsthome[17].click()
        time.sleep(1)

        lstTextBox = driver.find_elements_by_xpath('//input[contains(@type, "text")]')
        time.sleep(0.5)
        lstTextBox[2].send_keys('rawdata')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()
        time.sleep(5)
        ##################################      Export Package as rawdata     ############################################
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()