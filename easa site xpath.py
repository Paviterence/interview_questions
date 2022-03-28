#EASA WEBSITE XPATH PRACTICE
#xpath practice EASA WEBSITE
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.part66easa.com/")
time.sleep(2)
driver.find_element(By.XPATH,'//a[text()="Download Question Papers"]').click()
print("1.",driver.title)
time.sleep(2)
driver.back()
print("2.",driver.title)
driver.find_element(By.XPATH,'//a[text()="Part66 Online Test "]').click()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,'//a[contains(text(),"Books")]').click()
print("3.",driver.title)
time.sleep(2)
driver.back()#NAVIGATION COMMANDS
driver.find_element(By.XPATH,'//a[contains(text(),"des")]').click()
print("4.",driver.title)
time.sleep(5)
driver.back()
driver.find_element(By.XPATH,'//span[contains(text(),"MODULE 01")]').click()
print("5.",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,'//span[contains(text(),"MODULE 04")]').click()
print("6.",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,'//span[text()="MODULE 05"]').click()
print("7.",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,'//span[contains(text(),"MODULE 06")]').click()
print("8.",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,'//span[contains(text(),"MODULE 10")]').click()
print("9.",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,'//span[contains(text(),"9")]').click()
print("10.",driver.title)
time.sleep(2)
driver.find_element(By.XPATH,'(//span[contains(text(),"DOWNLOAD ")])[1]').click()
print("11.",driver.title)
driver.back()
driver.find_element(By.XPATH,'(//span[contains(text(),"DOWNLOAD ")])[2]').click()
print("12.",driver.title)
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,'(//span[contains(text(),"DOWNLOAD ")])[3]').click()
time.sleep(2)
print("13.",driver.title)
driver.back()
driver.close()