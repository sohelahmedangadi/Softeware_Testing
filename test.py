# test_math_utils.py
import pytest
from calculate import add, div, user_name  # Import the function you want to test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_add():
    # Arrange & Act
    result = add(10, 2)
    
    # Assert (uses Python's built-in assert statement)
    assert result == 12

def test_div():
    assert div(10, 2) == 5

@pytest.mark.parametrize("name", [
        "sohail",
        "Jon",
        "Kit",
        "Dinash"
    ])
def test_user_name(name):
    assert user_name(name) == True
    
def test_google_search():
    driver = webdriver.Chrome()

    driver.get("https://google.com")

    assert "Google" in driver.title

    driver.quit()

    

