from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
parent_handle = None


def Yatra():
    driver.get("https://www.yatra.com/")
    parent_handle = driver.current_window_handle
    print(parent_handle)

def find_element_by_XPATH(element_name):
    driver.find_element(By.XPATH, element_name).click()
