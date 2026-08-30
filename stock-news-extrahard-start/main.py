

##https://www.alphavantage.co
##https://newsapi.org
## https://www.twilio.com





import requests 
import os 
from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir,"main.py")
# Send mails directly python .\stock-news-extrahard-start\stock-news-extrahard-start\main.py

#setting up env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
COMPANY_NAME = os.getenv("COMPANY_NAME")
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")
COMPANY_SYMBOL = os.getenv("COMPANY_SYMBOL")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


newsapi = NewsApiClient(api_key=API_KEY_NEWS)
all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                        language='en',
                                        sort_by='relevancy',
                                        )
sources = newsapi.get_sources()
new_articles = all_articles['articles'][0:3]



url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={COMPANY_SYMBOL}&apikey={API_KEY_STOCKS}'
response = requests.get(url)

data = response.json()
date = '2026-07-31'
# the dates need to be changed according to today/yesterday 
# Some days markets are closed - dates must work +- based. --NO ERRORS induced 
days = list(data['Time Series (Daily)'].keys())

latest_day = days[0]
previous_Day = days[1]


day_price = float(data['Time Series (Daily)'][latest_day]['4. close'])
daybefore_price = float(data['Time Series (Daily)'][previous_Day]['4. close'])
Change_price = round(((day_price-daybefore_price)/daybefore_price)*100,2)


message = f"TSLA:🔺{Change_price}" if Change_price>0 else f"TSLA:🔻{Change_price}"



# Can i take In import messages from the whatsapp terminal and give them stock price and relevant articles. 







client = Client(ACCOUNT_SID, AUTH_TOKEN)


message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=f"{message}\n",
  to='whatsapp:+917506950841'
)

print(message.sid)
print(message)

for article in new_articles:
    body = f"Title: {article['title']}\nDescription: {article['description']}\nUrl : {article['url']}"
    client = Client(ACCOUNT_SID, AUTH_TOKEN)


    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"{body}\n",
    to='whatsapp:+917506950841'
    )

    print(message.sid)
    print(message)
    
    
