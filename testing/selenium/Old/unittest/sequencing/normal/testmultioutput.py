# -*- coding: utf-8 -*-
"""
sequencingwithmultioutput is responsible for creating the package for the testing
of the eXe's Sequencing Feature.

In this package:
- You can learn many different chapters after completing chapter 1
- After passing ANY quiz in chapter 1, you can study chapter 2 or chapter 3.

Structure:

        # sequencingwithmultioutput
        #         |_Thiên Long Bát Bộ
        #         |                 |_Chương 1: Nhân vật chính
        #         |                 |               |_I. Tiêu Phong
        #         |                 |               |_II. Hư Trúc
        #         |                 |               |_III. Đoàn Dự
        #         |                 |_Chương 2: Bang phái
        #         |                 |               |_I. Các bang phái chính
        #         |                 |               |_II. Một số bang phái khác
        #         |                 |_Chương 3: Một số võ công
        #         |                 |               |_I. Tiêu Dao phái
        #         |                 |               |_II. Cái Bang
        #         |                 |_Tổng kết
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


class TestMultiOutput(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_multioutput(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()


        ################################      Open Package rawdatanormal     #########################################
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="accesskey_button-1010"]').click()
        time.sleep(0.5)

        clickopen = driver.find_element_by_xpath('//*[@id="accesskey_menuitem-1014-itemEl"]').click()
        lsthome = driver.find_elements_by_xpath('//button[contains(@class, "x-btn-center")]')

        #lsthome[13] == Home folder
        lsthome[13].click()


        lstTextBox = driver.find_elements_by_xpath('//input[contains(@type, "text")]')
        time.sleep(0.5)
        lstTextBox[1].send_keys('rawdatanormal.elp')
        time.sleep(0.5)

        ### lstBtn is a Open button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[4].click()
        time.sleep(5)
        ################################      Open Package rawdatanormal     #########################################
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
                """
                postConditionTab = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                """
                btnSave.click()
                stopvent = 10

        #####################     Add Sequencing Config for Chương 1: Nhân vật chính      ########################

        ###############################     Add Sequencing Config for I. Tiêu Phong      ###################################
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
            if namenode == u'I. Tiêu Phong':
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
                        ### Add Post Condition
                time.sleep(0.5)
                """
                postConditionTab = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                """
                btnSave.click()
                stopvent = 10

        ###############################     Add Sequencing Config for I. Tiêu Phong      ###################################

        ############################     Add Sequencing Config for II. Hư Trúc      ################################
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
            if namenode == u'II. Hư Trúc':
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
                    if optionname == u"         I. Tiêu Phong":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                """
                postConditionTab = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                """
                btnSave.click()
                stopvent = 10

        ############################     Add Sequencing Config for II. Hư Trúc      ################################

        ############################     Add Sequencing Config for III. Đoàn Dự      ################################
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
            if namenode == u'III. Đoàn Dự':
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
                    if optionname == u"         II. Hư Trúc":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                """
                postConditionTab = driver.find_elements_by_xpath(
                    '//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                """
                btnSave.click()
                stopvent = 10

        ############################     Add Sequencing Config for III. Đoàn Dự      ################################

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
                    if optionname == u"         III. Đoàn Dự":
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

        #         |                 |_Chương 3: Một số võ công
        #         |                 |               |_I. Tiêu Dao phái
        #         |                 |               |_II. Cái Bang

        ########################     Add Sequencing Config for Chương 3: Một số võ công      ##########################
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
            if namenode == u'Chương 3: Một số võ công':
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
                    if optionname == u"         III. Đoàn Dự":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ########################     Add Sequencing Config for Chương 3: Một số võ công      ##########################

        ##########################     Add Sequencing Config for I. Tiêu Dao phái      #############################
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
            if namenode == u'I. Tiêu Dao phái':
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
                    if optionname == u"      Chương 3: Một số võ công":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        ##########################     Add Sequencing Config for I. Tiêu Dao phái      #############################

        #########################     Add Sequencing Config for II. Cái Bang      ############################
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
            if namenode == u'II. Cái Bang':
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
                    if optionname == u"         I. Tiêu Dao phái":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        #########################     Add Sequencing Config for II. Cái Bang      ############################

        #########################     Add Sequencing Config for Tổng Kết      ############################
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
            if namenode == u'Tổng Kết':
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
                    if optionname == u"         II. Cái Bang":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)

                btnSave.click()
                stopvent = 10

        #########################     Add Sequencing Config for Tổng Kết      ############################

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
        lstTextBox[1].send_keys('testmultioutput')
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