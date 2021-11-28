import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver import ActionChains
class Category_Page():

    repeat_post_click="(//*[@class='wp-menu-name'])[2]"
    page_post_click = "(//*[@class='wp-menu-name'])[4]"
    click_on_category_xpath="//a[@href='edit-tags.php?taxonomy=category']"
    category_drop_down_button_xpath="//*[@id='bulk-action-selector-top']"
    select_all_checkbox_xpath="//*[@id='cb-select-all-1']"
    click_on_category_apply_xpath="//*[@id='doaction']"

    #logout methods
    logout_move_xpath="(//*[@class='ab-item'])[35]"
    logout_button="//*[@id='wp-admin-bar-logout']"



    def __init__(self, driver):
        self.driver=driver

    def category_page(self):
       #wait= WebDriverWait(driver,10).until(EC.element_to_be_clickable(self.click_on_category_xpath))
        self.driver.find_element_by_xpath(self.page_post_click).click()
        self.driver.find_element_by_xpath(self.repeat_post_click).click()
        self.driver.find_element_by_xpath(self.click_on_category_xpath).click()
    def select_drop_down(self):
        drop_category=self.driver.find_element_by_xpath(self.category_drop_down_button_xpath)
        drop=Select(drop_category)
        drop.select_by_value("delete")
        self.driver.find_element_by_xpath(self.click_on_category_apply_xpath).click()

    def signout(self):
        move_to_logout=self.driver.find_element_by_xpath(self.logout_move_xpath)
        ac = ActionChains(self.driver)
        ac.move_to_element(move_to_logout).perform()
        self.driver.find_element_by_xpath(self.logout_button).click()



