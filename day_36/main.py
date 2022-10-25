import requests
from datetime import datetime, date
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
today = str(date.today())
ALPHA_API_KEY = "GESN5JUVIMCDLQHE"
NEWS_API_KEY = "9fa7eb7ac20a4100b422385178f1c06e"
TWILIO_SID = "ACbdc01d6f087d97efa5973b7034493ac2"
TWILIO_AUTH_ID = "87220c184a7b2d0e2f7af940c677761d"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_API_KEY}"
r = requests.get(url)
data_json = r.json()

time_series = data_json["Time Series (Daily)"]

data_list = [value for(key, value) in time_series.items()]
current_data = data_list[0]["4. close"]
previous_data = data_list[1]["4. close"]
price_difference = float(current_data) - float(previous_data)
movement_display = None
if price_difference > 0:
    movement_display= "💹"
else:
    movement_display= "🔻"


different_percentage = round((price_difference * float(current_data)) / 100)

if abs(different_percentage) > 3:
    params = {
        "q": COMPANY_NAME,
        "from": today,
        "to": today,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY

    }
    news_url = "https://newsapi.org/v2/everything"
    news_request = requests.get(news_url, params=params)
    news_data = news_request.json()["articles"]
    top_three_articles = news_data[:3]
    articles = [f"{STOCK}: {movement_display}{different_percentage}%\n Headline: {article['title']}.\n {article['description']} \n{article['url']}" for article in top_three_articles]


client = Client(TWILIO_SID, TWILIO_AUTH_ID)

for article in articles:
    message = client.messages.create(body= article,from_='+14246227317',to='+26776710242' )



