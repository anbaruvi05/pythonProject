# Trash page methods
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Trash_Page():
    # Trash Page Click Action
    click_on_trash_button = "//*[@class='trash']/child::a"
    select_on_drop_down_button = "//*[@id='bulk-action-selector-top']"
    select_all_check_box = "//*[@id='cb-select-all-1']"
    click_on_apply_on_trash_page = "//*[@id='doaction']"

    def __init__(self, driver):
        self.driver = driver

    def click_trash_button(self):
        self.driver.find_element_by_xpath(self.click_on_trash_button).click()
    def select_delete_drop_down(self):
        delete_drop = self.driver.find_element_by_xpath(self.select_on_drop_down_button)
        delete_button = Select(delete_drop)
        delete_button.select_by_value("delete")
        self.driver.find_element_by_xpath(self.select_all_check_box).click()
        self.driver.find_element_by_xpath(self.click_on_apply_on_trash_page).click()

