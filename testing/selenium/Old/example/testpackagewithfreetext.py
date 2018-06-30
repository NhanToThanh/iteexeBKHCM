# -*- coding: utf-8 -*-
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


class PackageWithFreeText(testing.selenium.unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()



    def test_package_with_free_text(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()

        #time.sleep(1)
        #driver.execute_script("document.body.style.zoom='120%'")
        #time.sleep(1)

        #driver.execute_script("document.body.style.zoom='110%'")
        #time.sleep(5)
        #element = wait.until(
        #       EC.element_to_be_clickable((By.XPATH, '//*[@id="button-2520"]'))
        #)

        #element1 = wait.until(
        #       EC.element_to_be_clickable((By.XPATH, '//*[@id="button-1005-btnInnerEl"]'))
        #)

        #element = WebDriverWait(driver, 10).until(
        #    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="messagebox-1001-testfield-inputEl"]'))
        #)

        # Find AddPage button
        # addPage = driver.find_element_by_css_selector("#button-2520")



        #addPage.click()


        ###########################     RENAME THE ROOT INTO PackageTD      ########################################

        ####################################     Rename The Root Into PackageTD      ###################################

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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.BACKSPACE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('PackageWithFreeText')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     Rename The Root Into PackageTD      ###################################


        ########################################     Create Introduction      ##########################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2520"]').click()
        time.sleep(0.1)
        ########################################     Create Introduction      ##########################################


        #########################################     RENAME Introduction      #########################################
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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Introduction')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #########################################     RENAME Introduction      #########################################

        time.sleep(0.1)

        #################################     Add Free Text for Introduction      ######################################
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
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
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
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        #########################################  Enable the button Bold  #############################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-bold")]').click()
        #########################################  Enable the button Bold  #############################################

        ###############################################  Text with BOLD  ###############################################
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u"Lập trình hàm (Functional Programming) là gì ?")
        time.sleep(0.5)
        ###############################################  Text with BOLD  ###############################################

        ##########################################  Disable the button Bold  ###########################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-bold")]').click()
        ##########################################  Disable the button Bold  ###########################################


        ##################################################  TextArea  ##################################################
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(""u"""
Lập trình hàm là một trường phái trong đó coi hàm (không phải object) là các khối nền tảng để xây dựng chương trình, với ý tưởng ta có thể truyền hàm như là tham số tới các hàm khác và có thể trả về chúng như giá trị.
Lập trình hàm liên quan đến việc viết code không thay đổi trạng thái.
Lý do chính là các lời gọi hàm liên tiếp sẽ cho ra cùng kết qủa.
Ta có thể dùng lập trình hàm với bất kỳ ngôn ngữ nào hỗ trợ first-class functions.
Một số ngôn ngữ như Haskell, không cho phép thay đổi trạng thái (ví dụ: các thao tác vào ra).
        """)
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

        #################################     Add Free Text for Introduction      ######################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ####################################     CREATE High-order Functions      ######################################
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
            if namenode == 'PackageWithFreeText':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2520"]').click()
                stopvent = 10
        ####################################     CREATE High-order Functions      ######################################

        ####################################     RENAME High-order Functions      ######################################
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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    'High-order Functions')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     RENAME High-order Functions      ######################################
        time.sleep(0.1)

        #############################     Add Free Text for High-order Functions      ##################################

        """
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
        """

        stopvent = 1
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
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
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        ########################################  Enable the button Bullet  ############################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-bullist")]').click()
        ########################################  Enable the button Bullet  ############################################


        ##################################################  TextArea  ##################################################
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Một hay nhiều đối số của nó là hàm và giá trị trả ra không phải là hàm.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Nó trả ra một hàm khác nhưng không có đối số nào là hàm.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đối số là hàm và giá trị trả về cũng là hàm.')
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
        time.sleep(0.5)

        #############################     Add Free Text for High-order Functions      ##################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ########################################     CREATE Immutability      ##########################################
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
            if namenode == 'PackageWithFreeText':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2520"]').click()
                stopvent = 10
        ########################################     CREATE Immutability      ##########################################

        ########################################     RENAME Immutability      ##########################################
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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Immutability')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ########################################     RENAME Immutability      ##########################################

        time.sleep(0.1)
        #################################     Add Free Text for Immutability      ######################################

        """
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
        """

        stopvent = 1
        time.sleep(0.1)
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
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
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        ########################################  Click the Embedded Media  ############################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-media")]').click()
        ########################################  Click the Embedded Media  ############################################


        ##################################################  TextArea  ##################################################
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@class, "mce-textbox")]').send_keys('https://youtu.be/b8mGfV0NtgI')
        time.sleep(0.1)
        driver.find_element_by_xpath('//div[contains(@class, "mce-widget mce-btn mce-primary mce-abs-layout-item mce-first mce-btn-has-text")]').click()
        time.sleep(0.1)
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

        #################################     Add Free Text for Immutability      ######################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     CREATE Pattern matching      ########################################
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
            if namenode == 'PackageWithFreeText':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2520"]').click()
                stopvent = 10
        ######################################     CREATE Pattern matching      ########################################

        ######################################     RENAME Pattern matching      ########################################
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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Pattern matching')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ######################################     RENAME Pattern matching      ########################################

        time.sleep(0.1)
        ###############################     Add Free Text for Pattern matching      ####################################

        """
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
        """

        stopvent = 1
        time.sleep(0.1)
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
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
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        ########################################  Click the Embedded Media  ############################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-media")]').click()
        ########################################  Click the Embedded Media  ############################################


        ##################################################  TextArea  ##################################################
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@class, "mce-textbox")]').send_keys('https://youtu.be/GZXK5J-i9qs')
        time.sleep(0.1)
        driver.find_element_by_xpath('//div[contains(@class, "mce-widget mce-btn mce-primary mce-abs-layout-item mce-first mce-btn-has-text")]').click()
        time.sleep(0.1)
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

        #################################     Add Free Text for Immutability      ######################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     CREATE Lazy Evaluation      #########################################
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
            if namenode == 'PackageWithFreeText':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2520"]').click()
                stopvent = 10
        ######################################     CREATE Lazy Evaluation      #########################################

        ######################################     RENAME Lazy Evaluation      #########################################
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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Lazy Evaluation')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ######################################     RENAME Lazy Evaluation      #########################################

        time.sleep(0.1)
        ################################     Add Free Text for Lazy Evaluation      ####################################

        """
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
        """

        stopvent = 1
        time.sleep(0.1)
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
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
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        ########################################  Click the Embedded Media  ############################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-media")]').click()
        ########################################  Click the Embedded Media  ############################################


        ##################################################  TextArea  ##################################################
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@class, "mce-textbox")]').send_keys('https://youtu.be/etKOTUF7R4g')
        time.sleep(0.1)
        driver.find_element_by_xpath('//div[contains(@class, "mce-widget mce-btn mce-primary mce-abs-layout-item mce-first mce-btn-has-text")]').click()
        time.sleep(0.1)
        ##################################################  TextArea  ##################################################

        ########################################## Submit FreeText #####################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//img[contains(@alt, "Done")]').click()
        time.sleep(0.5)
        ########################################## Submit FreeText #####################################################

        ################################     Add Free Text for Lazy Evaluation      ####################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        ######################################     CREATE Type Inference      ##########################################
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
            if namenode == 'PackageWithFreeText':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2520"]').click()
                stopvent = 10
        ######################################     CREATE Type Inference      ##########################################

        ######################################     RENAME Type Inference      ##########################################
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
                driver.find_element_by_xpath('//*[@id="button-2522"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 5)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys('Type Inference')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ######################################     RENAME Type Inference      ##########################################

        ################################     Add Free Text for Type Inference      #####################################

        """
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
        """

        stopvent = 1
        time.sleep(0.1)
        lstIdevices = driver.find_elements_by_xpath('//div[contains(@class, "x-grid-cell-inner ")]')
        for idevice in lstIdevices:
            if stopvent == 10:
                break
            #time.sleep(0.1)
            nameidevice = toUnicode(idevice.text, idevice.text)
            #time.sleep(0.1)
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
        frametext = driver.find_element_by_xpath('//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        ###############################################  Enter TextArea  ###############################################

        ########################################  Click the Embedded Media  ############################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        time.sleep(0.5)
        driver.find_element_by_xpath('//i[contains(@class, "mce-ico mce-i-media")]').click()
        ########################################  Click the Embedded Media  ############################################


        ##################################################  TextArea  ##################################################
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@class, "mce-textbox")]').send_keys('https://youtu.be/D5SlVhp-E90')
        time.sleep(0.1)
        driver.find_element_by_xpath('//div[contains(@class, "mce-widget mce-btn mce-primary mce-abs-layout-item mce-first mce-btn-has-text")]').click()
        time.sleep(0.1)
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

        ################################     Add Free Text for Type Inference      #####################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ##############################     Add Sequencing Config for Introduction      #################################
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
            if namenode == 'Introduction':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()

                ### Add Preconditon
                #availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                #options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                stopvent = 1
                #for option in options:
                    #if stopvent == 10:
                        #break
                    #optionname = toUnicode(option.text, option.text)
                    #if optionname == "   Introduction":
                        #option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('5')
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ##############################     Add Sequencing Config for Introduction      #################################


        ##########################     Add Sequencing Config for High-order Functions      #############################
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
            if namenode == 'High-order Functions':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   Introduction":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ##########################     Add Sequencing Config for High-order Functions      #############################


        #############################     Add Sequencing Config for Immutability      ##################################
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
            if namenode == 'Immutability':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   High-order Functions":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        #############################     Add Sequencing Config for Immutability      ##################################

        ###########################     Add Sequencing Config for Pattern matching      ################################
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
            if namenode == 'Pattern matching':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   Immutability":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ###########################     Add Sequencing Config for Pattern matching      ################################

        ###########################     Add Sequencing Config for Lazy Evaluation      #################################
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
            if namenode == 'Lazy Evaluation':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   Pattern matching":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('7')
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ###########################     Add Sequencing Config for Lazy Evaluation      #################################

        ###########################     Add Sequencing Config for Type Inference      ##################################
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
            if namenode == 'Type Inference':
                actionChains = ActionChains(driver)
                actionChains.context_click(node).perform()
                seq = driver.find_elements_by_xpath('//div[contains(@class, "x-component x-box-item x-component-default x-menu-item")]')
                for seqele in seq:
                    seqtext = toUnicode(seqele.text, seqele.text)
                    if seqtext == "Sequcing config":
                        seqele.click()

                time.sleep(0.1)
                ### Add Preconditon
                availableWhen = driver.find_element_by_xpath('//div[contains(@class, "x-trigger-index-0 x-form-trigger x-form-arrow-trigger x-form-trigger-last x-unselectable")]').click()
                time.sleep(0.1)
                btnSave = driver.find_element_by_xpath('//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
                time.sleep(0.1)
                options = driver.find_elements_by_xpath('//li[contains(@role, "option")]')
                time.sleep(0.1)
                stopvent = 1
                for option in options:
                    if stopvent == 10:
                        break
                    optionname = toUnicode(option.text, option.text)
                    if optionname == "   Lazy Evaluation":
                        option.click()
                        ### Add Post Condition
                time.sleep(0.5)
                postConditionTab = driver.find_elements_by_xpath('//div[contains(@class, "x-tab x-box-item x-tab-default x-noicon x-tab-noicon x-tab-default-noicon x-top x-tab-top x-tab-default-top")]')
                postConditionTab[1].click()
                time.sleep(0.5)
                timeTextBox = driver.find_element_by_xpath('//*[@id="editorMode"]')
                time.sleep(0.5)
                timeTextBox.send_keys('5')
                time.sleep(0.5)
                btnSave.click()
                stopvent = 10

        ###########################     Add Sequencing Config for Type Inference      ##################################


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
        lstTextBox[2].send_keys('PackageWithFreeText')
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
    testing.selenium.unittest.main()

