import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Demo_JS():
    def Demo_javaScript(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        # driver.get("https://www.rcvacademy.com/")
        driver.execute_script(
            "window.open('https://www.rcvacademy.com/','_self');")
        demo_element = driver.execute_script(
            "document.getElementsByTagName('p')[2];")
        driver.execute_script("arguments[0].click();", demo_element)
        time.sleep(50)


DJS = Demo_JS()
DJS.Demo_javaScript()
