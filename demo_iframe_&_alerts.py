import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert


class Demo_Alerts():
    def alerts(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert2")
        time.sleep(1)

        driver.switch_to.frame("iframeResult")
        driver.find_element(
            By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        
        #Alert(driver).accept()
        time.sleep(2)


DA = Demo_Alerts()
DA.alerts()
