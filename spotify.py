from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

def generate_random_number():
    return random.randint(0, 2)

# Create an empty list to store webdriver instances
browsers = []

acccounts =[["arishi560@gmail.com", "Fuck11@Society"],
            ["anujchandel96@gmail.com", "Anuj@13579"],
            ["acethyking@gmail.com", "Psycacid@1233"],
            ["nalwa.sachin73@gmail.com", "Sachin1@Nalwa"],
            ["nishant.ecell@gmail.com", "Sacetas@123"],
            ["ujjwalthakur98056@gmail.com", "Ujjwal@123"],
            ["natthusingh862@gmail.com", "Natthu@123"],
            ["impawanyt@gmail.com", "AcidLSD@777"]
            ]


# Create 10 webdriver instances and store them in the list
for _ in range(len(acccounts)):
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(5)
    browsers.append(browser)

    browser.get("https://accounts.spotify.com/en/login")
    time.sleep(1)

    # Find the input field with the ID 'login-username' and enter the email
    username_field = browser.find_element(By.ID, "login-username")
    username_field.send_keys(acccounts[_][0])

    time.sleep(1)

    # Find the input field with the ID 'login-password' and enter the password
    password_field = browser.find_element(By.ID, "login-password")
    password_field.send_keys(acccounts[_][1])

    # Find the button with the ID 'login-button' and click it
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    time.sleep(1)

# Navigate to the login page in each window
for browser in browsers:
    # # Print the page title
    print("Page title after login:", browser.title)

    page_title = browser.title

    if 'Status' in page_title:
        # Find the button with data-testid="web-player-link" and click it
        web_player_button = browser.find_element(By.CSS_SELECTOR, '[data-testid="web-player-link"]')
        web_player_button.click()

        # Wait for a short period to ensure the click is processed
        time.sleep(1)

        # song_list = ["https://open.spotify.com/track/7aKywPZNhse8LA3HO4RNFz",
        #              "https://open.spotify.com/track/4cdvvqALVYdMkZcDDu5mnv",
        #              "https://open.spotify.com/track/5TiqduzRDF16Yeqbyz5v5g"
        #              ]
        
        # random_index = generate_random_number()

        # Redirect to the search page
        browser.get("https://open.spotify.com/artist/1HoCGglcF7U4NyKW3NbRrM")

        # Wait for the search page to load
        time.sleep(3)

        # Simulate pressing the space bar
        body = browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.SPACE)
    

# Keep the browsers open until the user presses Enter
input("Press Enter to close the browsers...")
for browser in browsers:
    browser.quit()