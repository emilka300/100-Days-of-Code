import requests
from datetime import datetime as dt
from datetime import timedelta as td
from twilio.rest import Client


# DATA FOR STOCK
STOCK_Endpoint = "https://www.alphavantage.co/query"
STOCK_API_KEY = ""
STOCK = "TSLA"

# DATA FOR NEWS
NEWS_Endpoint = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""
COMPANY_NAME = "Tesla Inc"

# TWILIO CREDITS
account_sid = "AC772e9e810dbcf11fc158abe681fa6f74"
auth_token = ""


def sign(percent):
    if percent > 0:
        return "🔺"
    else:
        return "🔻"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_Endpoint, params=stock_parameters)
response.raise_for_status()
stock = response.json()

stock_price = stock['Time Series (Daily)']
# last two available days
yesterday = list(stock_price.keys())[0]
the_day_before_yesterday = list(stock_price.keys())[1]
price_yesterday = float(stock_price[yesterday]["4. close"])
price_the_day_before_yesterday = float(stock_price[the_day_before_yesterday]["4. close"])

delta = price_yesterday - price_the_day_before_yesterday

percentage_delta = round((delta / price_yesterday)*100)

if abs(percentage_delta) > 5:

    date = (dt.today() + td(days=-2)).strftime('%Y-%m-%d')

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    news_parameters = {
        "q": COMPANY_NAME,
        "from": date,
        "pageSize": "3",
        "page": "1",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(NEWS_Endpoint, params=news_parameters)
    response.raise_for_status()
    news = response.json()
    articles = news["articles"]

    text_message = ""

    # DIFFERENT APPROACH
    # text_message = [f"TSLA: {delta_sign}{percentage_delta}%\nHeadline:{article['title']}\nBrief:
    # {article['description']}\n\n" for article in articles]

    for article in articles:
        title = article['title']
        description = article['description']
        delta_sign = sign(percentage_delta)
        text_message = text_message + f"TSLA: {delta_sign}{percentage_delta}%\nHeadline:{title}\nBrief:{description}\n\n"

    print(text_message)

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=text_message,
        from_='+18652384852',
        to='+48731170519')

    print(message.status)
else:
    print("Too small delta.")

