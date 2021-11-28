class GXi_Login():

    useremail_id="user_login"
    userpassword_id="user_pass"
    click_login_id="wp-submit"


    def __init__(self, driver):
        self.driver = driver

    def getUserName(self,username):
        self.driver.find_element_by_id(self.useremail_id).send_keys(username)

    def getPassword(self,password):
        self.driver.find_element_by_id(self.userpassword_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.click_login_id).click()
""""
    def takeScreenshot(self):
        self.driver.save_screenshot("C:/Users/ANBARUVI/PycharmProjects/pythonProject3/Screenshots/login_test.png")
"""
