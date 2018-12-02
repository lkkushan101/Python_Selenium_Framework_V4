from Pages.HomePage import Home
from Pages.RegistrationPage import Register
from Utility.ReadExcel import readExcel
from Utility.ScreenShotUtility import takeScreenShot
from Utility.SpeechReporting import speechReporting
from selenium.webdriver.chrome.options import Options
import unittest
import json
from selenium import webdriver
import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTest(unittest.TestCase):
    @allure.story('Test Automation Solution - Kushan Amarasiri')
    @allure.feature('Test - Auomation Framework in Python')
    @allure.testcase("Registration Test Case")
    def setUp(self):

       with pytest.allure.step("Launch site"):
         if readExcel('./Data/data.xlsx','Browser_Conf','A2') == "Yes":
             chrome_options = Options()
             chrome_options.add_argument("--headless")
             self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
         else:
             self.driver = webdriver.Chrome(ChromeDriverManager().install())




    def test_search_in_python_org(self):

        with open('./Data/data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        str1 = readExcel('./Data/data.xlsx','Sheet1','A2')

        driver.get(str1)
        speechReporting("Navigated to the web site")
        scr = takeScreenShot('sc2.png', self.driver)
        driver.save_screenshot('./ScreenShots/sc1.png')
        driver.set_page_load_timeout(20)
        m = Home(driver)
        m.getRegister().click()
        r = Register(driver)
        r.setFirstName(readExcel('./Data/data.xlsx', 'Sheet1', 'B2'))
        r.setLastName(readExcel('./Data/data.xlsx', 'Sheet1', 'C2'))
        r.setPhone(readExcel('./Data/data.xlsx', 'Sheet1', 'G2'))
        r.setCountry(readExcel('./Data/data.xlsx', 'Sheet1', 'D2'))
        r.setEmail(readExcel('./Data/data.xlsx', 'Sheet1', 'H2'))
        r.setUserName(readExcel('./Data/data.xlsx', 'Sheet1', 'E2'))
        r.setPassword(readExcel('./Data/data.xlsx', 'Sheet1', 'I2'))
        r.setConfirmPassword(readExcel('./Data/data.xlsx', 'Sheet1', 'I2'))
        scr = takeScreenShot('sc3.png', self.driver)
        speechReporting("Data entered and registration completed")
        r.submitRegistration()
        if __name__ == "__main__":
            unittest.main()

