import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.saucedemo.com/"

class ProductsCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
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

    def test13_CheckoutWithoutItems(self):
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(1)
        checkout = self.driver.find_element(By.XPATH, '//*[@id="checkout"]').is_displayed()
        self.assertFalse(checkout) 

    def test14_CheckoutWithValidCredential(self):
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'first-name').send_keys('Am')
        self.driver.find_element(By.ID, 'last-name').send_keys('Tester')
        self.driver.find_element(By.ID, 'postal-code').send_keys('123456')
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'continue').click()
        time.sleep(0.5)
        self.driver.find_element(By.ID, 'finish').click()

        validation = self.driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/img').is_displayed()
        self.assertTrue(validation)       

    def test15_CheckoutWithEmpyCredential(self):
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        self.driver.find_element(By.ID, 'continue').click()
        response = self.driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3').text
        self.assertEqual(response, 'Error: First Name is required')
        
    def test15_CancelCheckout(self):
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        self.driver.find_element(By.ID, 'cancel').click()
        response = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]').text
        self.assertEqual(response, 'YOUR CART')

    def test16_ContinueShopping(self):
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="continue-shopping"]').click()
        response = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
        self.assertEqual(response, 'PRODUCTS')


    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()