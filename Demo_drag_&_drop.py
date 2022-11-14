from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time


class Demo_Sliders():
    def Sliders(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(
            By.XPATH, "//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.XPATH, "//div[@id='draggable']")
        elem2 = driver.find_element(By.XPATH, "//div[@id='droppable']")
        ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        time.sleep(4)


DS = Demo_Sliders()
DS.Sliders()
