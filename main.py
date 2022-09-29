from newsapi import NewsApiClient
from telebot import TeleBot
from telegraph import Telegraph
from datetime import datetime
import os

# set-up env variables
auth_token = os.environ['TELEGRAPH_TOKEN']
chat_id = os.environ['CHAT_ID']
api_key = os.environ['TELEGRAM_API_KEY']
news_api_key = os.environ['NEWS_API']

# create html content for telegraph page
newsapi = NewsApiClient(api_key=news_api_key)
top_headlines = newsapi.get_top_headlines(language='en',country='in')
page_content = ''
for article in top_headlines['articles']:
    title = f'<h3>{article["title"]}</h3>\n'
    date = f'<blockquote>{article["publishedAt"].replace("T"," ").replace("Z"," UTC")}</blockquote>\n'
    description = f'<p><b>{article["description"]}</b></p>\n'
    img = f'<img src=\"{article["urlToImage"]}\"></img>\n'
    content = f'<p>{article["content"].split("[")[0] if article["content"] != None else ""}<a href=\"{article["url"]}\">click here</a></p>\n'
    page_content += title+date+description+img+content+'<hr></hr>\n'

# create a telegraph page
tg = Telegraph(auth_token)
url = tg.create_page('Telegraph Today',html_content=page_content)

# send it via telegram
bot = TeleBot(api_key)
bot.send_message(chat_id,url)

#log the newspapers
with open('newslogs.txt','a') as file:
    file.writelines(f'{str(datetime.now())} - {url}\n')