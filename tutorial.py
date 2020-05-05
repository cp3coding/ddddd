from selenium import webdriver

PATH =r"C:\Users\nando\Downloads\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()