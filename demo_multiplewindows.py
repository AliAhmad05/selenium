import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Demo_Multiple_Windows():
    def Multiple_Window(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(
            By.XPATH, "//img[@alt='Upto 13% OFF (max. Rs.10,000) + No Cost EMI on 3 or 6 months']").click()
        # time.sleep(2)
        all_handles = driver.window_handles
        print("All Handles 1 : %s", all_handles)
        
        
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(
                    By.XPATH, "//a[@href='https://www.yatra.com/offer/details/zestmoney-offers']//span[@class='wfull offer-content anim']//img[@class='respnsiv-img']").click()
                all_handles = driver.window_handles
                print("All Handles 2 : %s", all_handles)
                all_handles.remove(handle)
                print("All Handles 3 : %s", all_handles)
                # time.sleep(4)
                #driver.close()
                # time.sleep(1)
                break
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(
                    By.XPATH, "//input[@id='Emailrs']").send_keys('123')
                time.sleep(5)
                break
                
                
        # driver.switch_to.window(parent_handle)
        # driver.find_element(
        #     By.XPATH, "//img[@alt='Upto 13% OFF (max. Rs.10,000) + No Cost EMI on 3 or 6 months']").click()
        # time.sleep(5)
        # print("All Handles: %s", all_handles)


DMW = Demo_Multiple_Windows()
DMW.Multiple_Window()
