#Teleminder -  A telegram bot to remind you to take your meds.

## How it works
Once a day, it sends you a message remembering to take your med at one specific time.

    - If you take it, you will receive a random cat gif.

    - If you take it late, it will send you a random sad or angry cat.

    - If you don't take it, it will remind you again in half hour.


#How to set up

Requirements: have python installed

1. [create a new telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) and get your TOKEN.

2. Talk to the bot and make the following query in order to get your CHAT_ID:
```
https://api.telegram.org/bot**E<TOKEN>**E/getUpdates
```

3. Change bot.py variables TOKEN and CHAT_ID:
```
TOKEN = 'TOKEN'
CHAT_ID = 123456
```

4. Install requirements
```
pip install -r requirements.txt
```

5- Run
```
python teleminder.py
```


