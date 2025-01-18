from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import requests
import webbrowser
import random
import pytz
import time
import os
import keyboard
from colorama import Fore
from pystyle import Center, Colors, Colorate
import time

# Set the title of the console window
os.system(f"title Kichi779 - Spotify Streaming bot v1 ")

# URL of the GitHub repository
url = "https://github.com/Kichi779/Spotify-Streaming-Bot/"

# Function to check for updates by comparing local and remote version files
def check_for_updates():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/version.txt")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            print(Colors.red, Center.XCenter("A new version is available. Please download the latest version from GitHub"))
            time.sleep(2)
            webbrowser.open(url)
            return False
        return True
    except:
        return True

# Function to print announcements from the GitHub repository
def print_announcement():
    try:
        r = requests.get("https://raw.githubusercontent.com/Kichi779/Spotify-Streaming-Bot/main/announcement.txt", headers={"Cache-Control": "no-cache"})
        announcement = r.content.decode('utf-8').strip()
        return announcement
    except:
        print("Could not retrieve announcement from GitHub.\n")

# List of supported timezones
supported_timezones = pytz.all_timezones

# Function to set a random timezone for the browser session
def set_random_timezone(driver):
    random_timezone = random.choice(supported_timezones)
    driver.execute_cdp_cmd("Emulation.setTimezoneOverride", {"timezoneId": random_timezone})

# Function to set a fake geolocation for the browser session
def set_fake_geolocation(driver, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": 100
    }
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)

# Main function to run the Spotify streaming bot
def main():
    if not check_for_updates():
        return
    announcement = print_announcement()
    print(Colorate.Vertical(Colors.white_to_green, Center.XCenter("""
           
                       ▄█   ▄█▄  ▄█    ▄████████    ▄█    █▄     ▄█  
                       ███ ▄███▀ ███   ███    ███   ███    ███   ███  
                       ███▐██▀   ███▌  ███    █▀    ███    ███   ███▌ 
                      ▄█████▀    ███▌  ███         ▄███▄▄▄▄███▄▄ ███▌ 
                     ▀▀█████▄    ███▌  ███        ▀▀███▀▀▀▀███▀  ███▌ 
                       ███▐██▄   ███   ███    █▄    ███    ███   ███  
                       ███ ▀███▄ ███   ███    ███   ███    ███   ███  
                       ███   ▀█▀ █▀    ████████▀    ███    █▀    █▀   
                       ▀                                             
 Improvements can be made to the code. If you're getting an error, visit my discord.  
                             Github  github.com/kichi779
                             Discord discord.gg/3Wp3amnNr3 """)))
    print("")
    print(Colors.red, Center.XCenter("ANNOUNCEMENT"))
    print(Colors.yellow, Center.XCenter(f"{announcement}"))
    print("")

    # List of user agents to mimic different browsers
    user_agents = [
    # Chrome (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

    # Chrome (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",

    # Firefox (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",

    # Firefox (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.4; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:93.0) Gecko/20100101 Firefox/93.0",

    # Safari (Mac)
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",

    # Opera (Windows)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 OPR/80.0.4170.61"
    ]
    
    # List of supported languages to mimic different locales
    supported_languages = [
    "en-US", "en-GB", "en-CA", "en-AU", "en-NZ", "fr-FR", "fr-CA", "fr-BE", "fr-CH", "fr-LU",
    "de-DE", "de-AT", "de-CH", "de-LU", "es-ES", "es-MX", "es-AR", "es-CL", "es-CO", "es-PE",
    "it-IT", "it-CH", "ja-JP", "ko-KR", "pt-BR", "pt-PT", "ru-RU", "tr-TR", "nl-NL", "nl-BE",
    "sv-SE", "da-DK", "no-NO"
    ]

    # Paths to Chrome and ChromeDriver
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    # Select a random user agent
    random_user_agent = random.choice(user_agents)

    # Read accounts from the accounts.txt file
    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    proxies = []

    # Ask the user if they want to use proxies
    use_proxy = input(Colorate.Vertical(Colors.green_to_blue, "Do you want to use proxies? (y/n):"))

    if use_proxy.lower() == 'y':
        print(Colors.red, Center.XCenter("The proxy system will be added after 50 stars. I continue to process without a proxy"))
        with open('proxy.txt', 'r') as file:
            proxies = file.readlines()
        time.sleep(3)

    # Ask the user for the Spotify song URL
    spotify_song = input(Colorate.Vertical(Colors.green_to_blue, "Enter the Spotify song URL (e.g https://open.spotify.com/track/5hFkGfx038V0LhqI0Uff2J?si=bf290dcc9a994c36):"))

    drivers = []

    # Random delays to mimic human behavior
    delay = random.uniform(2, 6)
    delay2 = random.uniform(5, 14)

    # Loop through each account and start the streaming process
    for account in accounts:

        # Select a random language
        random_language = random.choice(supported_languages)

        # Set Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ["enable-automation", 'enable-logging'])
        chrome_options.add_argument('--disable-logging')
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("--lang=en-US,en;q=0.9")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument(f"--user-agent={random_user_agent}")
        chrome_options.add_argument(f"--lang={random_language}")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_experimental_option('prefs', {
            'profile.default_content_setting_values.notifications': 2
        })

        # Initialize the Chrome driver
        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

        # Split the account into username and password
        username, password = account.strip().split(':')

        try:
            # Open the Spotify login page
            driver.get("https://www.spotify.com/us/login/")

            # Find and fill the username and password fields
            username_input = driver.find_element(By.CSS_SELECTOR, "input#login-username")
            password_input = driver.find_element(By.CSS_SELECTOR, "input#login-password")

            username_input.send_keys(username)
            password_input.send_keys(password)

            # Click the login button
            driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']").click()

            time.sleep(delay)

            # Open the specified Spotify song
            driver.get(spotify_song)

            driver.maximize_window()

            # Press the escape key to close any pop-ups
            keyboard.press_and_release('esc')

            time.sleep(10)

            try:
                # Accept cookies if the prompt appears
                cookie = driver.find_element(By.XPATH, "//button[text()='Accept Cookies']")
                cookie.click()
            except NoSuchElementException:
                try:
                    button = driver.find_element(By.XPATH, "//button[contains(@class,'onetrust-close-btn-handler onetrust-close-btn-ui')]")
                    button.click()
                except NoSuchElementException:
                    time.sleep(delay2)

            # Find and click the play button
            playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
            playmusic = driver.find_element(By.XPATH, playmusic_xpath)
            playmusic.click()

            time.sleep(1)

            print(Colors.green, "Username: {} - Listening process has started.".format(username))

        except Exception as e:
            print(Colors.red, "An error occurred in the bot system:", str(e))

        # Set a random timezone for the browser session
        set_random_timezone(driver)
        
        # Set a fake geolocation for the browser session
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        set_fake_geolocation(driver, latitude, longitude)

        drivers.append(driver)

        time.sleep(5)

    print(Colors.blue, "Stream operations are completed. You can stop all transactions by closing the program.")

    while True:
        pass

if __name__ == "__main__":
    main()


# ==========================================
# Copyright 2023 Kichi779

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==========================================
