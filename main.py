from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

username ="your user name"

file = open("path of pass txt file")

file_data = file.read()


password = file_data

driver.get("https://www.facebook.com/")

driver.find_element_by_name("email").send_keys(username + Keys.RETURN)
driver.find_element_by_name("pass").send_keys(password + Keys.RETURN)

login = driver.find_elements_by_xpath("//*[@id={}]".format("u_0_2"))
login.click()


driver.quit()