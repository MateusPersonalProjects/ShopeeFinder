import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import smtplib
import lxml


def scrape_website(url):

    all_data = []

    count_pages = 0
    pages_total = 0

    all_titles = []
    all_locations = []
    all_links = []
    all_prices = []

    # ------------------ Set Chrome Options and Webdriver --------------------------- #
    chrome_options = Options()
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('user-data-dir=C:\\Users\\amate\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # ----------------------- Get Data from Shopee ----------------------------- #
    delay = 5
    while count_pages <= pages_total:
        # Getting the url
        driver.get(f"{url}={count_pages}")

        WebDriverWait(driver, delay)

        sleep(5)

        # -------------- Scroll through the page so it can load --------------------- #
        y = 1000
        for timer in range(0, 9):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 1000
            sleep(1)

        # -------------- Check if there is something in the website -------------------- #
        item_check = driver.find_elements(By.CSS_SELECTOR, ".shopee-search-item-result__items")

        if item_check:

            # ---------------- Get the html from the page and pass it to the bs4 --------------------------- #
            html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            soup = BeautifulSoup(html, "lxml")

            # Get the number of pages
            pages_total = int(soup.find(name="span", class_="shopee-mini-page-controller__total").text) - 1

            # Get titles
            p_titles = soup.find_all(name="div", class_="Cve6sh")
            for title in p_titles:
                all_titles.append(title.text)

            # Get Location
            p_location = soup.find_all(name="div", class_="zGGwiV")
            for location in p_location:
                all_locations.append(location.text)

            # Get Prices
            price_elements = driver.find_elements(By.CSS_SELECTOR, "div .shopee-search-item-result__item")
            for price_element in price_elements:
                price = price_element.find_element(By.CSS_SELECTOR, ".ZEgDH9")
                all_prices.append(price.text)

            # Get links
            p_links = driver.find_elements(By.CSS_SELECTOR, "div .shopee-search-item-result__item a")
            for link in p_links:
                all_links.append(link.get_attribute("href"))

            # Add to the count of pages then it goes to the next one
            count_pages += 1

        else:
            break

    # -------------------------- Store the data in ALL_DATA variable ---------------------- #
    for num in range(0, len(all_titles)):
        format_type = {
            "title": all_titles[num],
            "location": all_locations[num],
            "price": all_prices[num],
            "url": all_links[num],
        }
        all_data.append(format_type)

    driver.quit()

    return all_data

