
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Comment: Automatically Download the chrome driver, no need to update it manually every time
driver = webdriver.Chrome(ChromeDriverManager().install()) #Implementation with chrome driver manager

#os_path = "C:\\browserdrivers\\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=os_path)   #Gives path of the driver to run the website for testing
driver.get("https://rcvacademy.com")    #opens the chromium browser

driver.maximize_window()    #It will maximize the window

print("Ali's Test" , driver.title)  #print the title of the website

driver.close()  #It will close the current Browser
#driver.quit()  #It will close all the associated browsers that are open



