import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://en-gb.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_id("email").send_keys("ironnnn124batman@rediffmail.com")

driver.find_element_by_id("pass").send_keys("pass12345")

driver.find_element_by_name("login").click()
time.sleep(5)
actual_Err_msg = driver.find_element_by_css_selector("#email_container > div._9ay7").text

expected_Err_Msg = "The email address you entered isn't connected to an account. Find your account and log in."

if(actual_Err_msg == expected_Err_Msg):
    print("Test case Passed")
else:
    print("Test case Failed")

driver.close()
