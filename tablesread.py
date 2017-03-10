import pytest
from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://letskodeit.teachable.com/p/practice")
driver.implicitly_wait(3)

elements = driver.find_elements_by_xpath("//table[@id='product']//td")
driver.implicitly_wait(3)

print(len(elements))

finalilist = [element.text for element in elements]

print(finalilist)
driver.quit()







