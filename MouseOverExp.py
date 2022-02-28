from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.maximize_window()
driver.implicitly_wait(30)

acctSignIn = driver.find_element_by_id("nav-link-accountList")
mouseOver = ActionChains(driver)
mouseOver.move_to_element(acctSignIn).perform()

driver.find_element_by_link_text("Orders").click()