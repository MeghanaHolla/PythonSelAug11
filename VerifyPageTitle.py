from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Training\Selenium\Drivers\chromedriver.exe")
driver.get("https://en-gb.facebook.com/")
actualTitle = driver.title
expectedTitle = "Facebook – log in or sign up"

if(actualTitle == expectedTitle):
    print("Test Case Passed")
else:
    print("Test Case Failed")

driver.close()