import time
import unittest
from selenium import webdriver
import logging
import sys
sys.path.append("C:/Users/ANBARUVI/PycharmProjects/pythonProject")
from pageObject.GXI_WebPage import GXi_Login
from pageObject.PostPage import Post_Page
from pageObject.TrashPage import Trash_Page
from pageObject.CategoryPage import Category_Page
from selenium.webdriver import ActionChains

class Login_PageTest(unittest.TestCase):
    Url="https://gxiglobal.com/wp-login.php?loggedout=true&wp_lang=en_US"
    username="naveen"
    password="galaxyXInnovations@21"

    logging.basicConfig(filename="C:/Users/ANBARUVI/PycharmProjects/pythonProject/Logger/login.log",
                        format="%(asctime)s: %(levelname)s: %(message)s:",level=logging.DEBUG
                        )

    logging.info("Launch the Chrome Browser")
    driver = webdriver.Chrome(
        executable_path="C:/Users/ANBARUVI/PycharmProjects/pythonProject/drivers/chromedriver.exe")
    @classmethod
    def setUpClass(cls):
        logging.info("Launch GXI_Webapplication URL")
        cls.driver.get(cls.Url)
        cls.driver.maximize_window()

    @classmethod
    def test_login_page(self):
        lp=GXi_Login(self.driver)
        logging.info("User enter the User_Name")
        lp.getUserName(self.username)
        lp.getPassword(self.password)
        lp.clickLogin()

    @classmethod
    def test_post_page(self):
        pp=Post_Page(self.driver)
        pp.click_on_post_button()
        time.sleep(10)
        pp.select_bulk_drop_down()
        pp.select_all_button()
        pp.click_on_apply()

    @classmethod
    def test_trash_page(self):
        tp=Trash_Page(self.driver)
        tp.click_trash_button()
        tp.select_delete_drop_down()

    @classmethod
    def tearDownClass(cls):
        logging.info("Browser closed")
        cls.driver.close()
        
