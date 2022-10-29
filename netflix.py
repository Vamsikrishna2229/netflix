import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest 
from time import sleep
import csv
import HtmlTestRunner

class netflix(unittest.TestCase):
       def test_sample(self):
            with open("testdata.csv","r") as csv_file:
                csv_reader=csv.reader(csv_file)
                for line in csv_reader:
                    self.driver=webdriver.Chrome()
                    self.driver.get("https://www.netflix.com/in/")
                    sleep(1)

                    signin=self.driver.find_element("xpath",'//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()
                    self.driver.get("https://www.netflix.com/in/login")
                    user=self.driver.find_element(By.ID,"id_userLoginId")
                    password=self.driver.find_element(By.ID,"id_password")
                    
                    user.send_keys(line[0])
                    password.send_keys(line[1])
                  
                    submit=self.driver.find_element("xpath",'//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
                    sleep(1)
                    self.driver.get("https://www.netflix.com/browse")
                    self.driver.quit()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='testcase_dir')) 


