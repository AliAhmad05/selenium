import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class Demo_Select_Drop_Down_Menu():
    def Demo_drop_down(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/form/signup/freetrial-elf-v2/?d=70130000000EqoP")
        driver.find_element(By.NAME,'UserFirstName').send_keys('Ali')
        driver.find_element(By.NAME,'UserLastName').send_keys('Ahmad')
        driver.find_element(By.NAME,'UserTitle').send_keys('SQA')
        time.sleep(1)
        driver.find_element(By.XPATH,"//a[@data-page-cntrl='next']").click()
        time.sleep(2)
        drop_down = driver.find_element(By.NAME,'CompanyCountry')
        dd = Select(drop_down)
        dd.select_by_index(1)
        time.sleep(1)
        dd.select_by_value("PK")
        time.sleep(3)
        dd.select_by_visible_text("United States")
        time.sleep(4)
        
drop_down = Demo_Select_Drop_Down_Menu()
drop_down.Demo_drop_down()
