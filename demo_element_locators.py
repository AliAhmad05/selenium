import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Demo_Find_Element_By_ID_And_Name():
    def Demo_Locate_By_ID(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        
        driver.find_element(By.CSS_SELECTOR,'#login-input').send_keys('test@test.com')
        time.sleep(1)
        
findbyid = Demo_Find_Element_By_ID_And_Name()
findbyid.Demo_Locate_By_ID()

