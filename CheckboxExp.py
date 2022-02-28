from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(30)


driver.find_element_by_link_text("Checkboxes").click()

isCheckboxSelected = driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(1)").is_selected()
if isCheckboxSelected == False:
    driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(1)").click()
else:
    print("Check box already selected")


isCheckboxSelected = driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(3)").is_selected()
if isCheckboxSelected == True:
    driver.find_element_by_css_selector("#checkboxes > input[type=checkbox]:nth-child(3)").click()
else:
    print("Check box not selected")