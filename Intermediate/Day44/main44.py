import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "example@com" # Your email
password = "passphrase" # Your passphrase

WANTED_PRICE = 90 # Put your wantedprice here
URL = "https://www.amazon.com/place your specific products url here"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
website = response.text


soup = BeautifulSoup(website, "html.parser")

price = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")
product_price = float(price.getText().split('$')[1])
if product_price < WANTED_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="example@example.com",
                            msg=f"Subject:Price Drop, Buy Now\n\n"
                                f"The products price you wanted has dropped to {product_price}$!")
        connection.close
