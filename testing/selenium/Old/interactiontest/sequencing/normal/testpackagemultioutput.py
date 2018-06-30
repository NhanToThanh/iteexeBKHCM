# -*- coding: utf-8 -*-

"""
testpackagetopdown is responsible for creating the package for the testing
of the eXe's Sequencing Feature.

In this package:
- You have to learn sequentially from top to bottom.
- No quiz and no time.


Structure:

        # sequencingnoquiz
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
        #         |                 |_Tổng Kết

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


class TestPackageMultiOutput(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_package_multioutput(self):
        driver = self.driver
        time.sleep(1)
        driver.get("https://cloud.scorm.com/sc/user/Library")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)


        ###########################     RENAME THE ROOT INTO PackageTD      ########################################

        ####################################     Rename The Root Into PackageTD      ###################################


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
        chooseFile = driver.find_element_by_xpath('//input[contains(@id, "lib_importForm_fileToImport")]').send_keys("/home/thanhnhan/Videos/eXe_handmake/testing/selenium/TestPackages/sequencing/testmultioutput.zip")
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
        driver.find_element_by_xpath('//li[contains(@title, "Chương 1: Nhân vật chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Phong")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Hư Trúc")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "III. Đoàn Dự")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ### Click Thiên Long Bát Bộ
        begin = driver.find_element_by_xpath('//li[contains(@title, "Thiên Long Bát Bộ")]').click()
        time.sleep(10)
        ### Click Thiên Long Bát Bộ


        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Phong")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Hư Trúc")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "III. Đoàn Dự")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ### Click Chương 1: Nhân vật chính
        time.sleep(1)
        chuong1 = driver.find_element_by_xpath('//li[contains(@title, "Chương 1: Nhân vật chính")]').click()
        time.sleep(1)
        ### Click Chương 1: Nhân vật chính


        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "II. Hư Trúc")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "III. Đoàn Dự")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################


        ### Click I. Tiêu Phong
        time.sleep(1)
        quymo = driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Phong")]').click()
        time.sleep(1)
        ### Click I. Tiêu Phong


        ###################################     Disable     #######################################
        time.sleep(10)

        driver.find_element_by_xpath('//li[contains(@title, "III. Đoàn Dự")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ### Click II. Hư Trúc
        time.sleep(1)
        nguyennhan = driver.find_element_by_xpath('//li[contains(@title, "II. Hư Trúc")]').click()
        time.sleep(1)
        ### Click II. Hư Trúc

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ### Click III. Đoàn Dự
        time.sleep(1)
        nguyennhan = driver.find_element_by_xpath('//li[contains(@title, "III. Đoàn Dự")]').click()
        time.sleep(1)
        ### Click III. Đoàn Dự

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        #driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        #time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################


        ### Click Chương 2: Bang phái
        time.sleep(1)
        chuong2 = driver.find_element_by_xpath('//li[contains(@title, "Chương 2: Bang phái")]').click()
        time.sleep(1)
        ### Click Chương 2: Bang phái

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        time.sleep(1)
        #driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        #time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################


        ### Click I. Các bang phái chính
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "I. Các bang phái chính")]').click()
        ### Click I. Các bang phái chính

        ###################################     Disable     #######################################
        time.sleep(10)
        #driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        #time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ### Click II. Một số bang phái khác
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "II. Một số bang phái khác")]').click()
        ### Click II. Một số bang phái khác

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################


        ### Click Chương 3: Một số võ công
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "Chương 3: Một số võ công")]').click()
        ### Click Chương 3: Một số võ công

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        time.sleep(1)
        ###################################     Disable     #######################################

        ### Click I. Tiêu Dao phái
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "I. Tiêu Dao phái")]').click()
        ### Click I. Tiêu Dao phái

        ###################################     Disable     #######################################
        time.sleep(10)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        ###################################     Disable     #######################################

        ### Click II. Cái Bang
        time.sleep(5)
        mtphiatay = driver.find_element_by_xpath('//li[contains(@title, "II. Cái Bang")]').click()
        ### Click II. Cái Bang

        ### Click II. Cái Bang
        time.sleep(5)
        driver.find_element_by_xpath('//li[contains(@title, "Tổng Kết")]').click()
        ### Click II. Cái Bang


        ### Click Thiên Long Bát Bộ
        time.sleep(5)
        begin = driver.find_element_by_xpath('//li[contains(@title, "Thiên Long Bát Bộ")]').click()
        time.sleep(5)
        ### Click Thiên Long Bát Bộ

    def tearDown(self):
        self.driver.close()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()

