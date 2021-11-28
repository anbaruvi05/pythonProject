from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Post_Page():

    post_page_button_xpath="(//*[@class='wp-menu-name'])[2]"
    bulk_drop_down_button_xpath="//*[@name='action']"
    select_all_button_xpath="//*[@id='cb-select-all-1']"
    click_on_apply_xpath="//*[@id='doaction']"





    def __init__(self, driver):
        self.driver = driver

    def click_on_post_button(self):
        self.driver.find_element_by_xpath(self.post_page_button_xpath).click()

    def select_bulk_drop_down(self):
        move_to_trash=self.driver.find_element_by_xpath(self.bulk_drop_down_button_xpath)
        drop_to_trash=Select(move_to_trash)
        drop_to_trash.select_by_value("trash")


    def select_all_button(self):
        self.driver.find_element_by_xpath(self.select_all_button_xpath).click()

    def click_on_apply(self):
        self.driver.find_element_by_xpath(self.click_on_apply_xpath).click()
