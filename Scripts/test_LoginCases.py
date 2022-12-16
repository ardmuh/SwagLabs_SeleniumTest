import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.saucedemo.com/"

class LoginCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test01_SuccesfulyLogin(self):
        #Step
        self.driver.get(url)
        time.sleep(1)
        userName = self.driver.find_element(By.ID, 'user-name')
        userName.send_keys("standard_user")
        time.sleep(0.5)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        #Validation
        response = self.driver.find_element(By.XPATH, "//span[@class='title']").text
        self.assertEqual(response, 'PRODUCTS')

    def test02_FailedLoginWithEmptyUsernameAndPassword(self):
        #Step
        self.driver.get(url)
        time.sleep(1)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        #Validation
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Username is required')

    def test03_FailedLoginWithInvalidPassword(self):
        #Step
        self.driver.get(url)
        time.sleep(1)
        userName = self.driver.find_element(By.ID, 'user-name')
        userName.send_keys("standard_user")
        time.sleep(0.5)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("invalid-pass")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        #Validation
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Username and password do not match any user in this service')

    def test04_FailedLoginWithEmptyUsername(self):
        #Step
        self.driver.get(url)
        time.sleep(1)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        #Validation
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Username is required')
    
    def test05_FailedLoginWithEmptyPassword(self):
        #Step
        self.driver.get(url)
        time.sleep(1)
        user_name = self.driver.find_element(By.ID, 'user-name')
        user_name.send_keys("standard_user")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        #Validation
        response= self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(response, 'Epic sadface: Password is required')

    def test06_SuccesfulyLogout(self):
        #Step
        self.driver.get(url)
        time.sleep(1)
        userName = self.driver.find_element(By.ID, 'user-name')
        userName.send_keys("standard_user")
        time.sleep(0.5)
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys("secret_sauce")
        time.sleep(0.5)
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        time.sleep(0.5)
        self.driver.find_element(By.ID,"logout_sidebar_link").click()

        #Validation
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]')
        

    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()