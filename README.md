# Telegraph Daily
A python script that sends me daily top headlines with the help of github actions.

This script creates a telegra.ph page with the news recieved from [newsapi.org](newsapi.org) every time it is executed and sends the link to the telegraph page via telegram bot api.

Here is a [link to a sample page](https://telegra.ph/Telegraph-Today-09-30) that this script creates.<br>
See the logs.txt for latest page created by this script.

<!-- How To Set-up -->
## How to set-up
### 1. Get API Access Tokens and Keys. <br>
* **Telegram Bot API**<br> Follow [this guide](https://core.telegram.org/bots#creating-a-new-bot) to get a telegram bot api token.
* **Telegraph API**<br> You can create a telegraph account by using telegraph api python module.<br> Or you can copy and paste this link with a new `short_name` and `author_name` in your browser, and copy `access_token` from there. `https://api.telegra.ph/createAccount?short_name=Sandbox&author_name=Anonymous`
* **NewsAPI.org API Key**<br> Register on newsapi.org to get your api key.
* **Chat-ID**<br> As this script does not reply to bot commands but rather sends a message automatically, you need to get the chat id for your telegram account for this to work. To get it follow this [link.](https://www.alphr.com/find-chat-id-telegram/)

### 2. Set-up github secrets
To access the api keys we need to store them in environment variables. While using github actions to run your scripts these environment variables are called github actions secrets.
To set-up a secret goto, `Settings > Secrets > Actions > New repository secret` and save -
* Telegram Bot API key as `TELEGRAM_API_KEY`
* Telgraph access token as `TELEGRAPH_TOKEN`
* NewsAPI API key as `NEWS_API`
* and Chat ID as `CHAT_ID`

### 3. Finalising
Now, the script is ready to run.<br>
To change the timing of github actions, edit .github/workflows/main.yml and change `- cron * * * * * *`.<br>
To change the localisation and category of news, edit main.py and change `top_headlines = newsapi.get_top_headlines(language='en',country='in')`.

Thank You, for visiting my repo.
