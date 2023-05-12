from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from config import Location

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://www.swiggy.com/")

Location_input = wait.until(
    EC.visibility_of_element_located
    ((By.ID, "location")))
Location_input.send_keys(Location)
select_location = wait.until(EC.visibility_of_element_located(
    ((By.CLASS_NAME, "_3lmRa"))))
select_location.click()

select_Restaurent = wait.until(EC.visibility_of_element_located(
    ((By.CLASS_NAME, "efp8s"))))
select_Restaurent.click()

Add_item1 = wait.until(EC.visibility_of_element_located(
    ((By.CLASS_NAME, "_1RPOp"))))
Add_item1.click()


select_option = wait.until(EC.visibility_of_element_located(
    ((By.CLASS_NAME, "_38xdN"))))
select_option.click()

# select_continue = wait.until(EC.visibility_of_element_located(
#     ((By.ID, "myElement"))))
# select_continue.click()
Add_item2 = wait.until(EC.visibility_of_element_located(
    ((By.CLASS_NAME, "__1RPOp"))))
Add_item2.click()
confirm_item = wait.until(EC.visibility_of_element_located(
    ((By.CLASS_NAME, "_38xdN"))))
confirm_item.click()
