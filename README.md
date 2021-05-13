# bluto_bot

A simple Discord bot made using discordpy.
Its primary function is the 'stonks' command, which expects a stock symbol to give back its current price.

## Usage
In Discord:

```?bluto [command]```

Example:

![bluto_example](images/blutobot_example.png)

## Installation
1. Navigate to root directory
2. Activate Python virtual environment (More info here: https://docs.microsoft.com/en-us/windows/python/web-frameworks#create-a-virtual-environment)
3. Run ```pip install -r requirements.txt```
4. Setup and create Discord bot and permissions. I used this guide https://dev.to/p014ri5/making-and-deploying-discord-bot-with-python-4hep
5. Create a .env file with your own DISCORD_TOKEN (refer to bluto.py for TOKEN reference)
6. While in virtual environment, run ```python3 bluto.py```
   
