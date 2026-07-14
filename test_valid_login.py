from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_valid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    time.sleep(15)

    success_message = driver.find_element(By.TAG_NAME, "h1").text

    assert success_message == "Logged In Successfully"

    driver.quit()


