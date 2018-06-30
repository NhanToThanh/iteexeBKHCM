# -*- coding: utf-8 -*-
"""
scormtestallquestions is responsible for creating the package for the testing
of the eXe's Test Feature.

In this package:
- You have to learn sequentially from top to bottom.
- It have some quizzes and you MUST pass ANY quiz to continue.
- In final chapter, SCORM Test will collect all SCORM Quiz and choose some questions base on user's setting.


Structure:

        # scormtestallquestions
        #         |_Thiên Long Bát Bộ
        #         |                 |_Chương 1: Nhân vật chính
        #         |                 |               |_I. Giới thiệu tổng quan
        #         |                 |               |_II. Câu hỏi ôn tập (pass ANY quiz along Test1, Test2, Test 3 and Test 4)
        #         |                 |_Chương 2: Bang phái
        #         |                 |               |_I. Các bang phái chính
        #         |                 |               |_II. Một số bang phái khác
        #         |                 |_Ôn tập cuối kỳ
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


class ScormTestAllQuestions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_scormtest_allquestions(self):
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
        lstTextBox[1].send_keys('rawdatascormtest.elp')
        time.sleep(0.5)

        ### lstBtn is a Open button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[4].click()
        time.sleep(5)
        ################################      Open Package rawdatascormtest     #########################################
        driver.switch_to_default_content()
        time.sleep(0.5)


        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_elements_by_xpath('//iframe[contains(@name, "authoringIFrame1-frame")]')[0]
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        ### Click edit
        driver.find_element_by_xpath('//img[contains(@alt, "Edit")]').click()


        ##################################################  SCORM Test  ##################################################
        time.sleep(1)
        hardtest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 1hard")]').send_keys('3')
        time.sleep(1)
        mediumtest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 1med")]').send_keys('1')
        time.sleep(1)
        easytest1 = driver.find_element_by_xpath('//input[contains(@id, "Test 1easy")]').send_keys('1')
        time.sleep(1)

        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 2hard")]').send_keys('2')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 2med")]').send_keys('1')
        time.sleep(1)
        hardtest2 = driver.find_element_by_xpath('//input[contains(@id, "Test 2easy")]').send_keys('1')
        time.sleep(1)

        hardtest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 3hard")]').send_keys('2')
        time.sleep(1)
        mediumtest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 3med")]').send_keys('1')
        time.sleep(1)
        easytest3 = driver.find_element_by_xpath('//input[contains(@id, "Test 3easy")]').send_keys('1')
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

        #############################     Add Data for Ôn tập cuối kỳ      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        #####################     Add Sequencing Config for Chương 1: Nhân vật chính      ########################
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
            if namenode == u'Chương 1: Nhân vật chính':
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
                    if optionname == u"   Thiên Long Bát Bộ":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        #####################     Add Sequencing Config for Chương 1: Nhân vật chính      ########################

        ###############################     Add Sequencing Config for I. Giới thiệu tổng quan      ###################################
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
            if namenode == u'I. Giới thiệu tổng quan':
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
                    if optionname == u"      Chương 1: Nhân vật chính":
                        option.click()

                btnSave.click()
                stopvent = 10

        ###############################     Add Sequencing Config for I. Giới thiệu tổng quan      ###################################

        ############################     Add Sequencing Config for II. Câu hỏi ôn tập      ################################
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
            if namenode == u'II. Câu hỏi ôn tập':
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
                    if optionname == u"         I. Giới thiệu tổng quan":
                        option.click()
                ### Add Post Condition
                time.sleep(0.5)

                postConditionTab = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(1)
                # timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')

                #passquiz1 = driver.find_element_by_xpath('//input[contains(@id, "1Quiz-inputEl")]').click()
                #time.sleep(1)
                #passquiz2 = driver.find_element_by_xpath('//input[contains(@id, "2Quiz-inputEl")]').click()
                #time.sleep(1)
                #passquiz3 = driver.find_element_by_xpath('//input[contains(@id, "3Quiz-inputEl")]').click()
                #time.sleep(1)
                passanyquiz = driver.find_element_by_xpath('//input[contains(@id, "anycon-inputEl")]').click()

                time.sleep(1)
                #timeTextBox.send_keys('5')
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        ############################     Add Sequencing Config for II. Câu hỏi ôn tập      ################################

        ########################     Add Sequencing Config for Chương 2: Bang phái      ##########################
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
            if namenode == u'Chương 2: Bang phái':
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
                    time.sleep(0.5)
                    optionname = toUnicode(option.text, option.text)
                    time.sleep(0.5)
                    if optionname == u"         II. Câu hỏi ôn tập ( 3 Quiz)":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ########################     Add Sequencing Config for Chương 2: Bang phái      ##########################

        ##########################     Add Sequencing Config for I. Các bang phái chính      #############################
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
            if namenode == u'I. Các bang phái chính':
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
                    if optionname == u"      Chương 2: Bang phái":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        ##########################     Add Sequencing Config for I. Các bang phái chính      #############################

        #########################     Add Sequencing Config for II. Một số bang phái khác      ############################
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
            if namenode == u'II. Một số bang phái khác':
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
                    if optionname == u"         I. Các bang phái chính":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        #########################     Add Sequencing Config for II. Một số bang phái khác      ############################

        #########################     Add Sequencing Config for Ôn tập cuối kỳ      ############################
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
            if namenode == u'Ôn tập cuối kỳ':
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
                    if optionname == u"         II. Một số bang phái khác":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        #########################     Add Sequencing Config for Ôn tập cuối kỳ      ############################

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
        lstTextBox[1].send_keys('scormtestallquestions')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()

        ##################################      Export Package as SCORM     ############################################
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()