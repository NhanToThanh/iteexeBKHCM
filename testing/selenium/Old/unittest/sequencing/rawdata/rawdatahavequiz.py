# -*- coding: utf-8 -*-

"""
sequencingtopdown is responsible for creating the package for the testing
of the eXe's Sequencing Feature.

In this package:
- You have to learn sequentially from top to bottom.
- No quiz and no time.

Structure:

        # sequencingtopdown
        #         |_Thiên Long Bát Bộ
        #         |                 |_Chương 1: Nhân vật chính
        #         |                 |               |_I. Giới thiệu tổng quan
        #         |                 |               |_II. Câu hỏi ôn tập (MUST pass Test 1, Test 2 and Test 3)
        #         |                 |_Chương 2: Bang phái
        #         |                 |               |_I. Các bang phái chính
        #         |                 |               |_II. Một số bang phái khác
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


class DataHaveQuiz(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_data_havetest(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()


        ################################     Rename The Root Into sequencinghavequiz      ###############################

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
                    'sequencinghavequiz')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ################################     Rename The Root Into sequencinghavequiz      ###############################

        ##############################     Create Thiên long bát bộ     ################################
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="button-2519"]').click()
        time.sleep(0.1)
        ##############################     Create Thiên long bát bộ     ################################

        ##############################     Rename  Thiên long bát bộ     ################################
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
                    u'Thiên Long Bát Bộ')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ##############################     Rename  Thiên long bát bộ     ################################
        time.sleep(0.1)

        #########################     Add Data for Thiên long bát bộ      ##############################
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u"""
                Tên gọi "Thiên long bát bộ" được tác giả Kim Dung lấy dựa theo kinh Phật Đại Thừa. Trong đó chỉ ra rằng "Thiên long bát bộ" là tám loài hữu tình trong thần thoại Phật Giáo. Trước kia họ hung ác, sau được Phật chuyển hoá thành những thần vật hộ trì phật pháp.
                """)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u"""
                Tuy tựa đề của Thiên Long bát bộ xuất phát từ Phật Giáo, nhưng nội dung của bộ truyện lại hoàn toàn kể về mối quan hệ giữa người với người (Kiều Phong, Hư Trúc, Đoàn Dự, A Tử, Vương Ngữ Yên,...) về cái phức tạp và đa dạng của con người trong xã hội. Kim Dung mượn tên tám loại phi nhân sức mạnh hơn người, mang hình dáng giống người nhưng không phải là người để ám chỉ từng nhân vật trong bộ truyện. Tám loại phi nhân đó là: Thiên, Long, Dạ Xoa, Càn Thát Bà, A Tu La, Ca Lâu La, Khẩn Na La, Ma Hầu La Gia. Tám loài này do Thiên và Long đứng đầu nên trong kinh Phật được gọi là "Thiên Long bát bộ".
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

        #########################     Add Data for Thiên long bát bộ      ##############################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ###############################     Create Chương 1: Nhân vật chính      ################################
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
            if namenode == u'Thiên Long Bát Bộ':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ###############################     Create Chương 1: Nhân vật chính      ################################

        ###############################     Rename Chương 1: Nhân vật chính      ################################
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
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Chương 1: Nhân vật chính')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ###############################     Rename Chương 1: Nhân vật chính      ################################
        time.sleep(0.1)

        ##########################     Add Data for Chương 1: Nhân vật chính      ###############################

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
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'I. Giới thiệu tổng quan')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'II. Câu hỏi ôn tập')

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

        ##########################     Add Data for Chương 1: Nhân vật chính      ###############################
        driver.switch_to_default_content()
        time.sleep(0.5)

        #########################################     Create I. Giới thiệu tổng quan      ############################################
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
            if namenode == u'Chương 1: Nhân vật chính':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        #########################################     Create I. Giới thiệu tổng quan      ############################################

        #########################################     Rename I. Giới thiệu tổng quan      ############################################
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
            if namenode == 'Unit':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'I. Giới thiệu tổng quan')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #########################################     Rename I. Giới thiệu tổng quan      ############################################

        time.sleep(0.1)
        #####################################     Add Data for I. Giới thiệu tổng quan      ##########################################

        stopvent = 1
        time.sleep(0.1)
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
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Tiêu Phong (Kiều Phong) là người trong Cái Bang. Với võ công cao cường và nhiều công trạng, dần dần uy tín của chàng lên cao. Khi bang chủ Cái Bang qua đời, chàng được phong làm bang chủ Cái Bang, sở hữu Hàng long thập bát chưởng và Đả cẩu bổng pháp. Lúc này trong giang hồ có câu nói Bắc Kiều Phong, Nam Mộ Dung để nói rằng uy tín của Tiêu Phong đã nổi khắp miền Trung Nguyên.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)

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

        #####################################     Add Data for I. Giới thiệu tổng quan      ##########################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ####################################     Create II. Câu hỏi ôn tập      #########################################
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
            if namenode == u'Chương 1: Nhân vật chính':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ####################################     Create II. Câu hỏi ôn tập      #########################################

        ####################################     Rename II. Câu hỏi ôn tập      #########################################
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
            if namenode == 'Unit':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'II. Câu hỏi ôn tập')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #########################################     Rename II. Câu hỏi ôn tập      ############################################

        time.sleep(0.1)
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
            u'Tiêu Phong là người gì ?')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Người Khiết Đan (C)')

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Người Tây Hạ')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b3")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q0b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q0b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Người Đại Lý')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b3")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q0b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q0b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Người Đại Liêu')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q0b3")]').click()
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
            u'Võ công mạnh nhất của Tiêu Phong là gì ?')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Giáng long thập bát chưởng (C)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Medium)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "mkey1b32")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Medium)

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đả cổng bổng pháp')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b3")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q1b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q1b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Lục Mạch Thần Kiếm')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b3")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q1b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q1b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đấu chuyển tinh di')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b3")]').click()
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
        question3 = driver.find_element_by_xpath('//div[contains(@id, "question2b3-viewer")]').click()
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
            u'Cha ruột của Kiều Phong là ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q2b3-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q2b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đoàn Chính Thuần')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey2b33")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b3")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q2b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q2b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Tiêu Viễn Sơn (C)')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b3")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q2b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q2b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Mộ Dung Bác')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b3")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q2b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q2b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Huyền Từ phương trượng')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q2b3")]').click()
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
        question4 = driver.find_element_by_xpath('//div[contains(@id, "question3b3-viewer")]').click()
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
            u'Ác Quán Mãn Doanh (Đệ nhất Ác Nhân) là biệt danh của ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q3b3-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q3b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đoàn Chính Thuần')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey3b34")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b3")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q3b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q3b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đoàn Dự')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b3")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q3b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q3b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đoàn Chính Minh')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b3")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q3b3-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q3b3_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Đoàn Diên Khánh (C)')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "3q3b3")]').click()
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
            u'Tứ Đại Ác Nhân bao gồm:')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Diên Khánh, Vân Trung Hạc, Mộ Dung Phục, Vương Ngữ Yên.')

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Nam Hải Ngạc Thần, Tô Tinh Hà, Vân Trung Hạc, Diệp Nhị Nương.')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b4")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q0b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q0b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Diên Khánh, Diệp Nhị Nương, Nam Hải Ngạc Thần, Mộ Dung Phục.')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b4")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q0b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q0b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Diên Khánh, Vân Trung Hạc, Nam Hải Ngạc Thần, Diệp Nhị Nương (C)')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "3q0b4")]').click()
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
            u'Tiêu Phong là bang chủ Cái Bang đời thứ ? ')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'6 (C)')

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'7')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b4")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q1b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q1b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'8')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b4")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q1b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q1b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'9')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q1b4")]').click()
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
        question3 = driver.find_element_by_xpath('//div[contains(@id, "question2b4-viewer")]').click()
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
            u'Hư Trúc là hòa thượng của chùa ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q2b4-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q2b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Chùa Thiên Long')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey2b43")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b4")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q2b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q2b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Chùa Thiếu Lâm (C)')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b4")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q2b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q2b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Chùa Đại Tuyết')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b4")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q2b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q2b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Chùa Đại Luân')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "1q2b4")]').click()
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
        question4 = driver.find_element_by_xpath('//div[contains(@id, "question3b4-viewer")]').click()
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
            u'Cha mẹ của Hư Trúc là ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q3b4-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q3b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Huyền Từ phương trượng - Diệp Nhị Nương (C)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey3b44")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b4")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q3b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q3b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Huyền Từ phương trượng - Tần Hồng Miên')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b4")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q3b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q3b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Chính Thuần - Tần Hồng Miên')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b4")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q3b4-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q3b4_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Chính Thuần - Diệp Nhị Nương')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q3b4")]').click()
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
            u'Những tuyệt kỹ của Hư Trúc là ?')
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
            u'Bắc Minh Thần Công, Bát Hoang Lục Hợp Duy Ngã Độc Tôn Công, Lục Mạch Thần Kiếm.')

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
            u'Bắc Minh Thần Công, Lăng Ba Vi Bộ, Tiểu Vô Tướng Công')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b5")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q0b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q0b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Bắc Minh Thần Công, Thiên Sơn Lục Dương Chưởng, Sinh Thổ Phù. (C)')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption0b5")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q0b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q0b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(u'Tất cả đều sai')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "2q0b5")]').click()
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
            u'Hư Trúc được nhận nội công từ những vị cao thủ phái Tiêu Dao, những vị đó là ?')
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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vô Nhai Tử, Đoàn Diên Khánh, Lý Thu Thủy')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Medium)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "mkey1b52")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Medium)

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
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vô Nhai Tử, Thiên Sơn Đồng Lão, Nam Hải Ngạc Thần')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b5")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q1b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q1b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vô Nhai Tử, Thiên Sơn Đồng Lão, Lý Thu Thủy (C)')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption1b5")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q1b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q1b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vô Nhai Tử, Đoàn Diên Khánh, Nam Hải Ngạc Thần')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "2q1b5")]').click()
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
        question3 = driver.find_element_by_xpath('//div[contains(@id, "question2b5-viewer")]').click()
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
            u'Đoàn Dự là con ruột của ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q2b5-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q2b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Diên Khánh - Đao Bạch Phượng (C)')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Easy)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "ekey2b53")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Easy)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b5")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q2b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q2b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Diên Khánh - Tần Hồng Miên')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b5")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q2b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q2b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Chính Thuần - Đao Bạch Phượng')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption2b5")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q2b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q2b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Chính Thuần - Tần Hồng Miên')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "0q2b5")]').click()
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
        question4 = driver.find_element_by_xpath('//div[contains(@id, "question3b5-viewer")]').click()
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
            u'Các tuyệt kỹ của Đoàn Dự là ?')
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        ### Option 1
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        option0 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer0q3b5-viewer")]')
        actionChains = ActionChains(driver)
        actionChains.double_click(option0).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer0q3b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Giáng long thập bát chưởng, Đấu chuyển tinh di, Lăng ba vi bộ')

        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)

        ### Set the Diffuculty (Hard)
        btnDiff = driver.find_element_by_xpath('//input[contains(@value, "hkey3b54")]').click()
        time.sleep(0.5)
        ### Set the Diffuculty (Hard)

        ##################################### Add option 2 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b5")]').click()
        time.sleep(0.5)
        option1 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer1q3b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option1).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer1q3b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Bắc Minh Thần Công, Lăng ba vi bộ, Dịch Cân Kinh')
        ##################################### Add option 2 ################################################

        ##################################### Add option 3 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b5")]').click()
        time.sleep(0.5)
        option2 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer2q3b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option2).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer2q3b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Bắc Minh Thần Công, Lăng ba vi bộ, Lục Mạch Thần Kiếm')
        ##################################### Add option 3 ################################################

        ##################################### Add option 4 ################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        time.sleep(0.5)
        driver.find_element_by_xpath('//input[contains(@name, "addOption3b5")]').click()
        time.sleep(0.5)
        option3 = driver.find_element_by_xpath('//div[contains(@id, "optionAnswer3q3b5-viewer")]')
        time.sleep(0.5)
        actionChains = ActionChains(driver)
        actionChains.click(option3).perform()
        time.sleep(0.5)
        frametext = driver.find_element_by_xpath('//iframe[contains(@id, "optionAnswer3q3b5_ifr")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Giáng long thập bát chưởng, Dịch Cân Kinh, Đấu Chuyển Tinh Di')
        ##################################### Add option 4 ################################################

        ### Check the correct answer #########################################################
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(vv)
        btn = driver.find_element_by_xpath('//input[contains(@value, "2q3b5")]').click()
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

        ######################################     Add Test 3 for II. Câu hỏi ôn tập      #########################################

        driver.switch_to_default_content()
        time.sleep(0.5)

        #################################     Create Chương 2: Bang phái      #####################################
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
            if namenode == u'Thiên Long Bát Bộ':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        #################################     Create Chương 2: Bang phái      #####################################

        #################################     Rename Chương 2: Bang phái      #####################################
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
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Chương 2: Bang phái')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #################################     Rename Chương 2: Bang phái      #####################################

        time.sleep(0.1)
        #############################     Add Data for Chương 2: Bang phái      ###################################

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
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'I. Các bang phái chính')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'II. Một số bang phái khác')

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

        #############################     Add Data for Chương 2: Bang phái      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ####################################     Create I. Các bang phái chính      ######################################
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
            if namenode == u'Chương 2: Bang phái':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ####################################     Create I. Các bang phái chính      ######################################

        ####################################     Rename I. Các bang phái chính      ######################################
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
            if namenode == 'Unit':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'I. Các bang phái chính')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     Rename I. Các bang phái chính      ######################################

        time.sleep(0.1)
        time.sleep(0.1)
        #############################     Add Data for I. Các bang phái chính      ###################################

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
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đại lý Đoàn Thị: Là hoàng tộc, thế gia võ lâm, tuy ở miền biên cảnh nhưng có qua lại ảnh hưởng lớn với võ lâm trung nguyên, chùa Thiên Long Tự là căn bản. Cao Thủ: Khô Vinh Đại Sư, Bảo Định Đế, Trấn Nam Vương Đoàn Chính Thuần, Bản Nhân,Bản Quan, Bản tham, Bản Tướng. Võ công tuyệt kĩ bao gồm: Nhất Dương Chỉ, Lục Mạch Thần Kiếm.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Thiếu Lâm tự: Thánh địa của võ lâm Trung nguyên. Phương Trượng: Linh Môn, Huyền Từ. Cao thủ: Lão tăng quyét rác (vô danh thần tăng), Huyền Trừng, Huyền Bi, Huyền Nạn, Huyền Thống, Huyền Khổ, Huyền Độ, Huyền Sinh... Tuyệt kĩ bao gồm: Dịch cân Kinh, 72 tuyệt kĩ...')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Tiêu Dao phái: Tiêu Dao phái ảnh hưởng của Đạo giáo thần tiên, võ công ảo diệu khôn lường đầy rẫy cao thủ kiêm cả cầm, kỳ, thi, họa, thổ (xây dựng), mộc (thủ công tinh xảo), y (thuốc), bốc (bói toán) nhưng ít nổi danh trên giang hồ do các trưởng bối đều ẩn cư. Chưởng Môn là Vô Nhai Tử, Hư Trúc. Môn hạ: Tề Tự Phong, Lý Thu Thủy, Tô Tinh Hà, Thiên Sơn Đồng Lão, Đinh Xuân Thu, Hàm Cốc Bát hữu(Tiết Mộ Hoa, Khang Quảng lăng,...). Bảo bối: nhẫn Cơ bảo của chưởng môn, Lang Hoàng Phúc Địa lưu giữ võ công của các nhà các phái... Tuyệt kĩ: Bắc Minh thần công, Lăng ba vi Bộ,... Tiểu Vô Tướng Công.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Cái Bang: Bang hội đông đảo, nghĩa hiệp, chuyên làm tai mắt tinh báo giúp nhà Tống chống ngoại xâm... Bang chủ: Uông kiếm Thông, Kiều Phong, Trang Tụ hiền (Du thản chi). Cao thủ: Từ trưởng lão, Mã phó bang chủ, Tứ Đại Trưởng lão. Tuyệt kĩ: Giáng Long Thập bát chưởng, Đả cẩu bổng pháp.')

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

        #############################     Add Data for I. Các bang phái chính      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ####################################     Create II. Một số bang phái khác      ######################################
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
            if namenode == u'Chương 2: Bang phái':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ####################################     Create II. Một số bang phái khác      ######################################

        ####################################     Rename II. Một số bang phái khác      ######################################
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
            if namenode == 'Unit':
                driver.find_element_by_xpath('//*[@id="button-2521"]').click()
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(Keys.DELETE * 4)
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'II. Một số bang phái khác')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     Rename II. Một số bang phái khác      ######################################

        time.sleep(0.1)
        time.sleep(0.1)
        #############################     Add Data for II. Một số bang phái khác      ###################################

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
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Thiên Sơn Linh Thứu Cung: Là phái do Thiên Sơn Đồng lão phái Tiêu dao sáng lập ở trên Tuyết Sơn tây vực. Cung Chủ: Thiên Sơn Đồng lão, Hư Trúc. Môn Hạ: Đặng bà bà, Dư bà bà, Mai, Lan, trúc, Cúc kiếm, 36 động chủ, 72 đảo chủ... Tuyệt kĩ: Thiên Sơn Lục Dương Chưởng, Thiên sơn chiết mai thủ, Sinh tử phù...')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Cô Tô Mộ Dung Gia: Là thế gia võ lâm, một hoàng tộc thất thế lưu vong nhiều đời, dân tộc Tiên ty nước Đại yên, ngụ cư ở yến Tử ổ vùng Cô Tô Thái hồ ở Giang nam, luôn tích chữ của cải nhân lực, lấy lòng võ Lâm, gây mâu thuẫn các nước để mưu phản hòng chiếm cứ giang sơn. Trang Chủ: Mộ dung Bác, Mộ Dung Phục. Môn Hạ: Bao Bất Đồng, Công dã càn, a Châu, a Bích... Tuyệt kĩ: Đấu Chuyển Tinh Di.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Cô Tô - Mạn đà Sơn trang: Là thế gia vọng tộc nổi tiếng ở Cô Tô về giàu có, ngang danh với nhà Mộ Dung, là thông gia với nhà Mộ Dung vì Mộ Dung Bác đã lấy con gái nhà Vương, Nhà vương tuy ban đầu chỉ là 1 nhà giàu nhưng có cô vợ góa Vương Phu nhân vốn là con gái của Vô Nhai Tử kế thừa Lang hoàng Ngọc Động là nơi giữ tàng thư gần như hoàn chỉnh của các môn phái cho nên đây có thể nói là nơi tàng tụ của tuyệt kĩ võ lâm các nhà các phái sau Lang Hoàng Phúc Địa của phái Tiêu Dao.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Tây hạ Nhất phẩm Đường: Là nơi nhà Tây Hạ quy tụ các cao thủ để xâm chiếm trung nguyên. Ngay trong Hoàng Cung Tây Hạ cũng có võ công trác tuyệt của phái Tiêu dao do Thái Phi Lý Thu Thủy mang về. Thủ lĩnh: Phạt Đông tướng quân Hách liên thiết Thụ. Cao thủ: Tứ Đại ác nhân, Lý Diên tông (Mộ dung Phục).... ngoài ra còn có quân đội.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Thổ Phồn: Là quốc gia láng giềng với Đại Tống và Đại Lý, đang nhăm nhe xâm chiếm các nơi. Chùa Đại tuyết sơn: là nơi ở của các Cao tăng võ công cao cường, họ cũng chuyên đi nghiêm tầm các võ học điển tịch của trung nguyên, Đại Lý.... để giúp nhà vua Thổ Phồn xâm chiếm trung Nguyên. Cao thủ: Quốc sư Cưu Ma Trí, Ba La Tinh, Triết La Tinh...')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Phái Tinh Túc: Do Đinh Xuân Thu lão quái là phản đồ phái Tiêu Dao sáng lập tại Tây Vực, sở trường chuyên dùng độc dược, tuy thế bang phái lỏng lẻo toàn là ô hợp. Môn hạ: Trích Tinh tử, A tử... Bảo bối: Thần mộc Vương đỉnh. Tuyệt kĩ: Hóa Công Đại Pháp.')

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

        #############################     Add Data for II. Một số bang phái khác      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        driver.switch_to_default_content()
        time.sleep(0.5)

        #################################     Create Tổng Kết      #####################################
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
            if namenode == u'Thiên Long Bát Bộ':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        #################################     Create Tổng Kết      #####################################

        #################################     Rename Tổng Kết      #####################################
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
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(
                    u'Tổng Kết')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #################################     Rename Tổng Kết      #####################################

        time.sleep(0.1)
        #############################     Add Data for Tổng Kết      ###################################

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
        time.sleep(0.5)
        driver.switch_to_default_content()
        time.sleep(0.5)
        driver.switch_to_frame(authoringFrame)
        frametext = driver.find_element_by_xpath(
            '//iframe[contains(@title, "Rich Text Area. Press ALT-F9 for menu. Press ALT-F10 for toolbar. Press ALT-0 for help")]')
        time.sleep(0.5)
        driver.switch_to_frame(frametext)
        time.sleep(0.5)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Kim Dung đã chỉnh sửa truyện này 3 lần, lần gần nhất là vào năm 2009[cần dẫn nguồn]. Có tổng cộng 50 hồi. Câu chuyện xoay quanh mối quan hệ phức tạp giữa nhiều nhân vật đến từ nhiều nước khác nhau: Kiều Phong, Đoàn Dự, Hư Trúc. Với tác phẩm này, Kim Dung muốn nói đến mối quan hệ nhân - quả giữa chính bản thân các nhân vật với gia đình, xã hội, dân tộc, đất nước. Câu truyện xảy ra vào thời Bắc Tống và còn bao gồm các cuộc chiến tranh giữa nhà Tống, Đại Lý, Đại Liêu, Thổ Phồn và Tây Hạ.')

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

        #############################     Add Data for Tổng Kết      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)


        ##################################      Save Package as rawdatahavequiz     ############################################
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
        lstTextBox[2].send_keys('rawdatahavequiz')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()
        time.sleep(5)
        ##################################      Export Package as rawdatahavequiz     ############################################


    def tearDown(self):
        self.driver.close()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()