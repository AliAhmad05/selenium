#from __init__ import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

class Demo_Mouse_Hover():
    def D_Mouse_Hover(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        more_button = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        achains = ActionChains(driver)
        achains.move_to_element(more_button).perform()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_cabs']").click()
        time.sleep(5)
        #ActionChains(driver).move_to_element(driver.find
        # achains.context_click().perform()
        
        
Mouse_Hover = Demo_Mouse_Hover()
Mouse_Hover.D_Mouse_Hover()