
from datetime import datetime, timedelta
import requests
from twilio.rest import Client

# Environment Variables
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_id = "Your api id"
news_api_id = 'Your api id'
account_sid = 'your account sid'
auth_token = 'your auth_token'

#  Getting Date format for Yesterday Ready
today = datetime.today()

yesterday = today - timedelta(days=1)
yesterday = yesterday.__str__()
yesterday_date = yesterday[:10]
two_days_before = today - timedelta(days=2)
two_days_before = two_days_before.__str__()
two_days_before_date = two_days_before[:10]

opening_time_yesterday = f"{yesterday_date} 05:00:00"
opening_time_two = f"{two_days_before_date} 05:00:00"


# Request to News Api
def get_news(myperc ):
    articles = []
    news_parameters = {
        'q': 'Tesla',
        'from': two_days_before_date,
        'sortBy': 'popularity',
        'apiKey': news_api_id
    }

    url = ('https://newsapi.org/v2/everything?')
    news_r = requests.get(url, news_parameters)
    news_r.raise_for_status()
    news = news_r.json()
    for num in range(3):
        articles.append(
            f'TSLA: {myperc}\n'f'Headline: {news["articles"][num]["title"]}.\nBrief: {news["articles"][num]["description"]}.')
    return articles

# Request to Stock Api
stock_parameters = {
    "function":'TIME_SERIES_INTRADAY',
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_api_id
}

url = 'https://www.alphavantage.co/query?'
r = requests.get(url, params=stock_parameters)
r.raise_for_status()
data = r.json()

timestamps_of_day = data["Time Series (60min)"]
price_stock_opening_yesterday = float(data["Time Series (60min)"][f"{opening_time_yesterday}"]["1. open"])
price_stock_opening_two = float(data["Time Series (60min)"][f"{opening_time_two}"]["1. open"])

print(price_stock_opening_yesterday, price_stock_opening_two)

myperc = round((price_stock_opening_yesterday / price_stock_opening_two) * 100) - 100
if myperc < 0:
    myperc = f"⬇{myperc}%"
else:
    myperc = f"⬆{myperc}%"

if price_stock_opening_two * 0.99 > price_stock_opening_yesterday > price_stock_opening_two * 1.01:
    print("Shouldn't get News")
else:
    articles_today = get_news(myperc)
    # print(articles_today)
    client = Client(account_sid, auth_token)
    for article in articles_today:
        message = client.messages \
            .create(body=f"{article}", from_="+17623025600", to="+306987508001")
        # print(message.status)


