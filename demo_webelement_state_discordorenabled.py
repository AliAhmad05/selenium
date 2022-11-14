import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Demo_Element_State():
    def Demo_enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        driver.find_element(By.ID,'user_name').send_keys("Ali111")
        driver.find_element(By.NAME,'user_pass').send_keys("Ali123")
        time.sleep(2)
        demo_state = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo_state)
        
        
DemoState = Demo_Element_State()
DemoState.Demo_enable_disable()
