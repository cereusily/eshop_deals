from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

PATH = '/Users/timothykung/Downloads/chromedriver'
SCROLL_PAUSE_TIME = 1.6

# Initializing for headless browser

options = Options()
options.headless = False
driver = webdriver.Chrome(PATH, options=options)

# Accesses Nintendo Website
driver.get('https://www.nintendo.com/en_CA/games/game-guide/'
           '#filter/:q=&dFR[generalFilters][0]=Deals&dFR[platform][0]=Nintendo%20Switch')

# Confirmation of accessing website
print("Accessed website!\n")
print("Now scrolling...")

# Scrolling / Clicking / Loading for more games / Returns number of deals
real_deals = driver.find_element_by_id("result-count")

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        button = driver.find_element_by_xpath('//button[text()="Load more games"]')
        driver.execute_script("arguments[0].click();", button)

    last_height = new_height

print("Finished scrolling through all games!")

# Prints All Games
all_games = driver.find_elements_by_xpath("//h3[@class='b3']")
all_games_price = driver.find_elements_by_xpath("//strong[@class='sale-price']")

games = [i.text for i in all_games]
price = [i.text for i in all_games_price]

total = len(games)

print(f"A total of {total} / {real_deals.text} have been scraped\n")

dictionary = dict(zip(games, price))

for game, price in dictionary.items():
    print(f"{game} - {price}")

# Kills browser
driver.quit()