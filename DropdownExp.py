from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://en-gb.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_link_text("Create New Account").click()

monthDD = driver.find_element_by_id("month")
dd = Select(monthDD)
#dd.select_by_visible_text("May")
dd.select_by_value("10")