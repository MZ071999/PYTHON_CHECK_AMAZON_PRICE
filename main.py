import time

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Calming-Package-Irritated-skincare-soothing/dp/B072KK81R5/"
TARGET_PRICE = 100.00

def check_site():
    global URL

    headers = {
        "User-Agent": "Defined"
    }

    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    amazon_web = response.text

    soup = BeautifulSoup(amazon_web, "html.parser")

    price_tag = soup.select_one(selector=".a-price span")
    if price_tag is None:
        return None
    else:
        price = price_tag.getText().strip("$")
        return float(price)

get_price = check_site()
loop = True
counter = 0

# using a while loop to make get request to amazon
# because one get request doesn't always return value from Amazon
while loop is True and counter < 20 and get_price is None:
    counter += 1
    print(f"Try {counter} counter, returned: {get_price}")
    time.sleep(2)
    get_price = check_site()

if get_price < TARGET_PRICE:
    alert = f"The product price has been lowered to {get_price}"




