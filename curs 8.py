from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#deschidem un browser chrome
chrome = webdriver.Chrome()
chrome.maximize_window()
#punem siteul pe care sa navigheze selenium
chrome.get('https://formy-project.herokuapp.com/form')
sleep(1)

#cautam text fieldul first name dupa id si introducem un text
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys("tiberiu")
sleep(2)

#cautam text fieldul last name dupa clasa si salvam intr-o lista toate elementele gasite si introducem un text
last_name = chrome.find_elements(By.CLASS_NAME, 'form-control')
last_name[1].send_keys('Serban')
sleep(2)

#cautam text fieldul job title dupa id folosind css selectorul si introducem un text
chrome.find_element(By.CSS_SELECTOR, "input#job-title").send_keys("ing")
sleep(2)

#cautam radio button dupa id folosind expath si dam click pe el
chrome.find_element(By.XPATH, '//input[@id="radio-button-1"]').click()
sleep(2)

#cautam radio button dupa id folosind css selector si dam click pe el
check = chrome.find_element(By.CSS_SELECTOR, "input#checkbox-1")
print(check)
check.click()
sleep(2)

#metoda care primeste ca si parametru idul fieldului si care implementeaza o cautare dinamica a elementelor din pagina
#folosind xpath
def form_input(id_value):
    input = chrome.find_element(By.XPATH, f'//input[@id="{id_value}"]')
    input.click()

form_input("checkbox-1")
form_input("checkbox-2")
form_input("checkbox-3")
sleep(2)

#cautare button submit dupa partial link text a linkului si dam click pe el
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Submit').click()
sleep(2)