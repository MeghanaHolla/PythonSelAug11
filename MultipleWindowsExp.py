from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,'userlogin')

driver.find_element_by_link_text("Click Here").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])

actualText = driver.find_element_by_css_selector("body > div > h3").text
if(actualText == "New Window"):
    print ("Pass")
else:
    print ("Fail")

driver.close()

driver.switch_to.window(windows[0])

driver.close()





