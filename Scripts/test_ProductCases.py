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

    def test07_AddProduct(self):
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        #Validation
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    
    def test08_RemoveProduct(self):
        self.driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="remove-sauce-labs-backpack"]').click()
        #Validation
        time.sleep(1)
        assert self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')

    def test09_SortProductByNameAToZ(self):
        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[1]').click()
        time.sleep(1)
        firstItem = self.driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
        self.assertEqual(firstItem, 'Sauce Labs Backpack')
    
    def test10_SortProductByNameZToA(self):
        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[2]').click()
        time.sleep(1)
        firstItem = self.driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div').text
        self.assertEqual(firstItem, 'Test.allTheThings() T-Shirt (Red)')

    def test11_SortProductByPriceLowToHigh(self):
        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]').click()
        time.sleep(1)
        firstItem = self.driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text
        time.sleep(1)
        self.assertIn(firstItem, '$7.99')   

    def test12_SortProductByPriceHighToLow(self):
        self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[4]').click()
        time.sleep(1)
        firstItem = self.driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text
        self.assertIn(firstItem, '$49.99')  


    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()