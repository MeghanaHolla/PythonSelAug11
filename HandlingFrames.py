from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()
driver.implicitly_wait(30)

driver.switch_to.frame("classFrame")

driver.find_element_by_link_text("INDEX").click()

driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Actions").click()