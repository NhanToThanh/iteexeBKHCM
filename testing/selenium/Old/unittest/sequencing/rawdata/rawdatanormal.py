# -*- coding: utf-8 -*-
"""
sequencingwithmultioutput is responsible for creating the package for the testing
of the eXe's Sequencing Feature.

In this package:
- You can learn many different chapters after completing chapter 1
- After passing ANY quiz in chapter 1, you can study chapter 2 or chapter 3.

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


class DataNormal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_data_normal(self):
        driver = self.driver
        driver.get("localhost:51235")
        driver.maximize_window()

        ################################     Rename The Root Into sequencingwithanyquiz      ###############################

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
                    'sequencingnoquiz')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ################################     Rename The Root Into sequencingwithanyquiz      ###############################

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
            u'Tiêu Phong')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Hư Trúc')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đoàn Dự')
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


        #########################################     Create I. Tiêu Phong      ############################################
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
        #########################################     Create I. Tiêu Phong      ############################################

        #########################################     Rename I. Tiêu Phong      ############################################
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
                driver.find_element_by_xpath('//*[@id="messagebox-1001-testfield-inputEl"]').send_keys(u'I. Tiêu Phong')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #########################################     Rename I. Tiêu Phong      ############################################

        time.sleep(0.1)
        #####################################     Add Data for I. Tiêu Phong      ##########################################

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

        #####################################     Add Data for I. Tiêu Phong      ##########################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Create II. Hư Trúc      #########################################
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
        ######################################     Create II. Hư Trúc      #########################################

        ######################################     Rename II. Hư Trúc      #########################################
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
                    u'II. Hư Trúc')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ######################################     Rename II. Hư Trúc      #########################################

        time.sleep(0.1)
        ##################################     Add Data for II. Hư Trúc      #######################################

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
            u'Hư Trúc là một hòa thượng chùa Thiếu Lâm. Ngoại hình xấu trai nhưng tâm tính hiền lành, tốt bụng. Hư Trúc đã vô tình giải được một bàn cờ vây tên gọi "Trân Lung kỳ trận", 10 năm nay chưa ai giải được, vì thế nên đã được Vô Nhai Tử, chưởng môn của phái Tiêu Dao truyền 70 năm công lực cả đời của ông.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vô Nhai Tử muốn Hư Trúc dùng nội công của ông truyền cho đi giết Đinh Xuân Thu, nhưng Hư Trúc từ chối vì nghĩ mình là một hòa thượng, không thể giết người bừa bãi. Sau đó, ông truyền chức chưởng môn nhân và giao thiết chỉ hoàn cho Hư Trúc, nhưng Hư Trúc không dám nhận và cũng không muốn đầu nhập phái khác.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Vì thấy ông sau khi truyền cho mình 70 năm công lực cả đời, có vẻ như ông sắp chết, Hư Trúc muốn ông ra đi trong thanh thản nên Hư Trúc đã đồng ý làm chưởng môn nhân phái Tiêu Dao cũng như đồng ý đi giết Đinh Xuân Thu. Sau khi Hư Trúc đồng ý, Vô Nhai Tử quy tiên.')
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

        ##################################     Add Data for II. Hư Trúc      #######################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ######################################     Create III. Đoàn Dự      #########################################
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
        ######################################     Create III. Đoàn Dự      #########################################

        ######################################     Rename III. Đoàn Dự      #########################################
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
                    u'III. Đoàn Dự')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ######################################     Rename III. Đoàn Dự      #########################################

        time.sleep(0.1)
        ##################################     Add Data for III. Đoàn Dự     #######################################

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
            u'Đoàn Dự là một chàng trai khôi ngô tuấn tú, hoàng tử của nước Đại Lý. Tuy là con nhà võ nhưng không thích luyện tập võ nghệ mà chỉ thích ngao du sơn thủy. Tình cờ trong quá trình can thiệp để giải cứu Chung Linh cô nương, Đoàn Dự lọt vào một hang đá, thấy một bức tượng ngọc bích rất đẹp (mà anh gọi là Thần tiên tỷ tỷ).')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Sau khi vái lạy bức tượng 1000 cái, anh lấy được bí kíp về Bắc Minh thần công (món võ hút lấy nội công kẻ khác, nhưng không tiêu huỷ nội lực đối thủ như Hóa công đại pháp do Đinh Xuân Thu luyện sai Bắc Minh thần công) và Lăng ba vi bộ (món võ có thể uyển chuyển chạy nhanh và tránh né các đòn công kích khác), và Đoàn Dự cũng miễn nhiễm độc tố sau khi vô tình nuốt phải một con cóc cực độc có tên là Mãng cổ chu cáp.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Đồng thời Đoàn Dự cũng làm quen được Mộc Uyển Thanh, một cô gái xinh đẹp, võ công cao cường, nhưng tính tình đanh đá và lúc nào cũng che kín mặt. Mộc cô nương đem lòng yêu mến chàng công tử họ Đoàn, và trong lúc đánh thua Nam Hải Ngạc Thần (một trong tứ đại ác nhân), đã nguyện kết nghĩa vợ chồng với Đoàn Dự và cho Đoàn Dự xem mặt nàng.')
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

        ##################################     Add Data for III. Đoàn Dự      #######################################
        driver.switch_to_default_content()
        time.sleep(0.5)
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

        #################################     Create Chương 3: Một số võ công      #####################################
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
        #################################     Create Chương 3: Một số võ công      #####################################

        #################################     Rename Chương 3: Một số võ công      #####################################
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
                    u'Chương 3: Một số võ công')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        #################################     Rename Chương 3: Một số võ công      #####################################

        time.sleep(0.1)
        #############################     Add Data for Chương 3: Một số võ công      ###################################

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
            u'I. Tiêu Dao phái')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'II. Cái Bang')

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

        #############################     Add Data for Chương 3: Một số võ công      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)


        ####################################     Create I. Tiêu Dao phái      ######################################
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
            if namenode == u'Chương 3: Một số võ công':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ####################################     Create I. Tiêu Dao phái      ######################################

        ####################################     Rename I. Tiêu Dao phái      ######################################
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
                    u'I. Tiêu Dao phái')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     Rename I. Tiêu Dao phái      ######################################

        time.sleep(0.1)
        time.sleep(0.1)
        #############################     Add Data for I. Tiêu Dao phái      ###################################

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
            u'Trong Thiên Long Bát Bộ, Tiêu Dao là một trong những môn phái quan trọng nhất và có ảnh hưởng lớn tới cốt truyện. Mặc dù sự tồn tại của phái Tiêu Dao ít được người ngoài biết đến, nhưng thành viên của phái đều là những nhân vật nổi tiếng trong võ lâm, thậm chí tự lập môn hộ riêng như Tô Tinh Hà lập ra Lung Á môn, Đinh Xuân Thu lập ra phái Tinh Túc, Thiên Sơn Đồng Lão lập ra Linh Tụ cung, Lý Thu Thủy lập ra Tây Hạ Nhất Phẩm Đường.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Bắc Minh Thần Công là một trong những môn võ hàng đầu của phái Tiêu Dao với nội dung chủ yếu là lấy nội lực của người khác làm của mình. Nhiều đại hiệp hẳn sẽ bảo là công phu hút nội lực ở đâu chẳng có. Xin thưa rằng trong 15 tuyệt tác của Kim Dung chỉ có đúng 3 công phu hút nội lực nhưng cả hai Hoá Công Đại Pháp lẫn Hấp Tinh Đại Pháp đều chỉ là bản lỗi của Bắc Minh Thần Công, không đáng để liệt chung hàng. Nói cách khác, Bắc Minh là bộ võ công hút nội lực đầu tiên, duy nhất và bá nhất.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Bát Hoang Lục Hợp Duy Ngã Độc Tôn Công: Lần đầu tiên trong truyện kiếm hiệp có một môn võ công quái đản như thế này. Người luyện sẽ có một chu kỳ sống tuần hoàn, cứ cách 30 năm phải trùng sinh một lần. Tổng lượt sẽ có 9 - 10 lần như thế, sau mỗi lượt sẽ có một khoảng thời gian giãn cách bị mất hết công lực (giai đoạn tán công), chẳng hạn như Thiên Sơn Đồng Mỗ vừa xong chu kỳ thứ 3 năm 96 tuổi thì tán công hết 90 ngày. Sau khi phục hồi thì công lực đại tăng, lại có thể trường thọ (có thể sống đến gần 300 tuổi) và bất lão.')
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(Keys.ENTER)
        time.sleep(0.1)
        driver.find_element_by_xpath('//body[contains(@class, "mce-content-body ")]').send_keys(
            u'Tiểu Vô Tướng Công: Vô Tướng là không có hình hài, công phu này lấy nội công của mình để sao chép cách thức thi triển tất cả các tuyệt học trên thế gian với uy lực thậm chí còn mạnh hơn nguyên bản. Nếu như Đẩu Chuyển Tinh Di của Mộ Dung Gia hay Di Hoa Tiếp Mộc của Di Hoa Cung cùng lắm chỉ là lấy "gậy ông đập lưng ông" khiến địch thủ có thể chết dưới chính tuyệt chiêu của mình thì Tiểu Vô Tướng Công chỉ cần tu luyện nội lực, còn chiêu thức thích gì sao chép nấy.')
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

        #############################     Add Data for I. Tiêu Dao phái      ###################################
        driver.switch_to_default_content()
        time.sleep(0.5)

        ####################################     Create II. Cái Bang      ######################################
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
            if namenode == u'Chương 3: Một số võ công':
                time.sleep(0.1)
                node.click()
                time.sleep(0.1)
                driver.find_element_by_xpath('//*[@id="button-2519"]').click()
                stopvent = 10
        ####################################     Create II. Cái Bang      ######################################

        ####################################     Rename II. Cái Bang      ######################################
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
                    u'II. Cái Bang')
                driver.find_element_by_xpath('//*[@id="button-1005-btnInnerEl"]').click()
                stopvent = 10
        ####################################     Rename II. Cái Bang      ######################################

        time.sleep(0.1)
        time.sleep(0.1)
        #############################     Add Data for II. Cái Bang      ###################################

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
            u'Đả Cẩu Bổng Pháp, Giáng Long Thập Bát Chưởng: Nếu như đã quen thuộc với Cái Bang - môn phái được ca tụng là "Thiên Hạ Đệ Nhất" bang trong bối cảnh truyện kiếm hiệp Kim Dung, hẳn bạn cũng biết về Giáng Long Thập Bát Chưởng và Đả Cẩu Bổng Pháp - hai bộ tuyệt học võ công trấn phái mà chỉ chức vị Bang chủ Cái Bang các đời mới có phẩm chất được truyền thụ lại.Về phần uy lực, Đả Cẩu Bổng Pháp được cấu thành từ 36 chiêu thức, mỗi chiêu đều chứa nhiều thức biến hóa khác nhau tạo thành vô số đòn đánh tinh diệu. Khẩu quyết tâm pháp của bộ võ công này được thi triển theo đường lối "Tứ lạng bạt thiên cân" (Bốn lạng bạt ngàn cân), áp dụng theo 8 quyết: buộc, đập, trói, đâm, khều, dẫn, khoá, xoay. Còn đối với Giáng Long Thập Bát Chưởng lại thuộc về phần tâm pháp nội công, mạnh hay yếu tùy thuộc vào nội lực của người luyện nên chỉ cần tới 18 chiêu thức là đủ. Hai bộ này vốn được coi là võ học trấn phái quan trọng của Cái Bang, những bậc tiền bối đều cấm các đời Bang chủ Cái Bang truyền lại cho người ngoài, nhưng đến thời của lão ăn mày Hồng Thất Công thì gã lại phá lệ truyền dạy lại hai bộ võ học này cho Hoàng Dung, Quách Tĩnh và Dương Quá.')
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

        #############################     Add Data for II. Cái Bang      ###################################
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


        ##################################      Save Package as rawdatanormal     ############################################
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
        lstTextBox[2].send_keys('rawdatanormal')
        time.sleep(0.5)

        ### lstBtn is a Save button
        lstBtn = driver.find_elements_by_xpath(
            '//div[contains(@class, "x-btn x-box-item x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon")]')
        lstBtn[5].click()
        time.sleep(5)
        ##################################      Export Package as rawdatanormal     ############################################
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        time.sleep(1)

if __name__ == "__main__":
    unittest.main()