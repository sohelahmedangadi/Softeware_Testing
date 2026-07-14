from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ----------------------------
# Test Data
# ----------------------------
URL = "https://www.saucedemo.com/"
EXPECTED_TITLE = "Swag Labs"

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# ----------------------------
# Launch Browser
# ----------------------------
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open Website
    driver.get(URL)

    # ----------------------------
    # Test Case 1: Verify Page Title
    # ----------------------------
    actual_title = driver.title

    if actual_title == EXPECTED_TITLE:
        print("✅ Title Verification Passed")
    else:
        print("❌ Title Verification Failed")
        print("Expected:", EXPECTED_TITLE)
        print("Actual:", actual_title)

    # ----------------------------
    # Test Case 2: Login
    # ----------------------------
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    loginBtn = driver.find_element(By.ID, "login-button")

    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    loginBtn.click()

    # Wait until the Products page loads
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

    # Verify Login
    page_title = driver.find_element(By.CLASS_NAME, "title").text

    if page_title == "Products":
        print("✅ Login Successful")
    else:
        print("❌ Login Failed")

except Exception as e:
    print("❌ Test Failed")
    print("Error:", e)

finally:
    driver.quit()