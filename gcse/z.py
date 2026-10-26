from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("-headless")

driver = webdriver.Firefox(options=options)

driver.get("https://www.aqa.org.uk/find-past-papers-and-mark-schemes")

print("\nINPUTS")
for n, element in enumerate(driver.find_elements("tag name", "input")):
    print(n, element.get_attribute("outerHTML"))

print("\nBUTTONS")
for n, element in enumerate(driver.find_elements("tag name", "button")):
    print(n, element.get_attribute("outerHTML"))

print("\nSELECTS")
for n, element in enumerate(driver.find_elements("tag name", "select")):
    print(n, element.get_attribute("outerHTML"))

print("\nLINKS CONTAINING SEARCH")
for element in driver.find_elements("tag name", "a"):
    text = element.text.strip()
    if "search" in text.lower():
        print(text, element.get_attribute("href"))

driver.quit()

