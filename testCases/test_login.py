from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestLogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_home_page_title(self, driver):
        self.logger.info("Started Home page title test")
        self.driver = driver
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, driver):
        self.logger.info("Started Login Test")
        self.driver = driver
        self.driver.get(self.baseURL)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setUserName(self.username)
        self.loginPage.setPassword(self.password)
        self.loginPage.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False
