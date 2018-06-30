# -*- coding: utf-8 -*-
"""
scormtestalllevel is responsible for creating the package for the testing
of the eXe's Test Feature.

In this package:
- You have to learn sequentially from top to bottom.
- It have some quizzes and you MUST pass ANY quiz to continue.
- In final chapter, SCORM Test will select in each SCORM Quiz one hard question, one medium question and one easy question.


Structure:

        # scormtestalllevel
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
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class TestPackageAllQuestions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_package_allquestions(self):
        driver = self.driver
        driver.get("https://cloud.scorm.com/sc/user/Library")
        driver.maximize_window()

        id = driver.find_element_by_xpath('//input[contains(@type, "email")]')
        id.send_keys("tothanhnhan19961@gmail.com")
        time.sleep(1)
        password = driver.find_element_by_xpath('//input[contains(@type, "password")]')
        password.send_keys("2w97b8bxz0!!!@")
        time.sleep(3)
        login = driver.find_element_by_xpath('//input[contains(@type, "submit")]').click()

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
        chooseFile = driver.find_element_by_xpath('//input[contains(@id, "lib_importForm_fileToImport")]').send_keys(
            "/home/thanhnhan/Videos/eXe_handmake/testing/selenium/TestPackages/scormtest/scormtestallquestions.zip")
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
        driver.find_element_by_xpath('//li[contains(@title, "Chương 1: Nhân vật chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Giới thiệu tổng quan")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Câu hỏi ôn tập")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        time.sleep(1)

        ###################################     Disable     #######################################

        ### Click Thiên Long Bát Bộ
        begin = driver.find_element_by_xpath('//li[contains(@title, "Thiên Long Bát Bộ")]').click()
        time.sleep(10)
        ### Click Thiên Long Bát Bộ

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "I. Giới thiệu tổng quan")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Câu hỏi ôn tập")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        time.sleep(1)

        ###################################     Disable     #######################################

        ### Click Chương 1: Nhân vật chính
        time.sleep(1)
        chuong1 = driver.find_element_by_xpath('//li[contains(@title, "Chương 1: Nhân vật chính")]').click()
        time.sleep(1)
        ### Click Chương 1: Nhân vật chính

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "II. Câu hỏi ôn tập")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        time.sleep(1)

        ###################################     Disable     #######################################

        ### Click I. Giới thiệu tổng quan
        time.sleep(1)
        quymo = driver.find_element_by_xpath('//li[contains(@title, "I. Giới thiệu tổng quan")]').click()
        time.sleep(1)
        ### Click I. Giới thiệu tổng quan

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        time.sleep(1)

        ###################################     Disable     #######################################

        ### Click II. Câu hỏi ôn tập
        time.sleep(1)
        nguyennhan = driver.find_element_by_xpath('//li[contains(@title, "II. Câu hỏi ôn tập")]').click()
        time.sleep(1)
        ### Click II. Câu hỏi ôn tập

        ###################################     Disable     #######################################
        time.sleep(5)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_element_by_xpath('//iframe[contains(@title, "II. Câu hỏi ôn tập")]')
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        #################################     Learn Quiz (Pass)     #####################################

        ### Test 3
        time.sleep(3)
        cau1 = driver.find_element_by_xpath('//input[contains(@id, "key0b53")]').click()
        time.sleep(1)
        cau2 = driver.find_element_by_xpath('//input[contains(@id, "key1b53")]').click()
        time.sleep(1)
        cau3 = driver.find_element_by_xpath('//input[contains(@id, "key2b51")]').click()
        time.sleep(1)
        cau4 = driver.find_element_by_xpath('//input[contains(@id, "key3b53")]').click()
        time.sleep(1)

        ### Submit
        time.sleep(1)
        submit = driver.find_element_by_xpath('//input[contains(@onclick, "calcScore23()")]').click()

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

        ### Test 3

        #################################     Learn Quiz  (Pass)    #####################################

        ###################################     Disable     #######################################
        time.sleep(3)
        driver.switch_to_default_content()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        ###################################     Disable     #######################################



        ### Click Chương 2: Bang phái
        time.sleep(1)
        chuong2 = driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        ### Click Chương 2: Bang phái

        ###################################     Disable     #######################################
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        ###################################     Disable     #######################################

        ### Click I. Các bang phái chính
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        ### Click I. Các bang phái chính

        ###################################     Disable     #######################################
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        ###################################     Disable     #######################################

        ### Click II. Một số bang phái khác
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        ### Click II. Một số bang phái khác

        ### Click Ôn tập cuối kỳ
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "Ôn tập cuối kỳ")]').click()
        ### Click Ôn tập cuối kỳ

        ############################################  Enter authoringFrame  ############################################
        time.sleep(0.5)
        authoringFrame = driver.find_element_by_xpath('//iframe[contains(@title, "Ôn tập cuối kỳ")]')
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        ############################################  Enter authoringFrame  ############################################

        #################################     Learn Scorm Test     #####################################

        ### Test 1
        time.sleep(25)
        cau1 = driver.find_element_by_xpath('//input[contains(@id, "question_question_1_0")]').click()
        time.sleep(1)
        cau2 = driver.find_element_by_xpath('//input[contains(@id, "question_question_3_3")]').click()
        time.sleep(1)
        cau3 = driver.find_element_by_xpath('//input[contains(@id, "question_question_2_0")]').click()
        time.sleep(1)
        cau4 = driver.find_element_by_xpath('//input[contains(@id, "question_question_6_1")]').click()
        time.sleep(1)
        cau5 = driver.find_element_by_xpath('//input[contains(@id, "question_question_5_1")]').click()
        time.sleep(1)
        cau6 = driver.find_element_by_xpath('//input[contains(@id, "question_question_4_1")]').click()
        time.sleep(1)
        cau7 = driver.find_element_by_xpath('//input[contains(@id, "question_question_8_0")]').click()
        time.sleep(1)
        cau8 = driver.find_element_by_xpath('//input[contains(@id, "question_question_7_2")]').click()

        ### Submit
        time.sleep(1)
        submit = driver.find_element_by_xpath('//input[contains(@onclick, "SubmitAnswers();")]').click()


        #################################     Learn Scorm Test     #####################################
        time.sleep(3)
        driver.switch_to_default_content()
        time.sleep(1)

        ### Click Thiên Long Bát Bộ
        time.sleep(1)
        begin = driver.find_element_by_xpath('//li[contains(@title, "Thiên Long Bát Bộ")]').click()
        time.sleep(5)
        ### Click Thiên Long Bát Bộ

    def tearDown(self):
        self.driver.close()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()

