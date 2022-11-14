import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Demo_Auto_Suggest():
    def Demo_Auto_Suggest_Menu(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        #driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        driver.get("https://www.yatra.com/")
        depart_from = driver.find_element(By.ID, 'BE_flight_origin_city')
        depart_from.click()
        depart_from.send_keys(Keys.CONTROL + "a")
        time.sleep(3)
        depart_from.send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        depart_from.send_keys("Mumbai")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)
        going_to = driver.find_element(By.ID, 'BE_flight_arrival_city')
        time.sleep(1)
        going_to.send_keys("New York")
        time.sleep(1)
        going_to.send_keys(Keys.ENTER)
        time.sleep(3)
        # time.sleep(5)
        # search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # print(len(search_results))
        # for results in search_results:
        #     print(results.text)
        #     if "New York (JFK)" in results.text:
        #         results.click()
        #         #time.sleep(5)
        #         break
        # time.sleep(5)
        
        calender = driver.find_element(By.XPATH, "//label[@for='BE_flight_origin_date']")
        calender.click()
        time.sleep(2)
        # driver.find_element(By.XPATH, "//td[@id='02/12/2022']").click()
        # time.sleep(4)

        all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date")=="30/11/2022":
                date.click()
                time.sleep(4)
                break

Auto_Suggest = Demo_Auto_Suggest()
Auto_Suggest.Demo_Auto_Suggest_Menu()
