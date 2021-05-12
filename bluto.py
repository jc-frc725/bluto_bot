# bluto.py

import os
import random
import responses
import requests
import bs4
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix = '?bluto ', case_Insensitve = True)
TOKEN = os.getenv('DISCORD_TOKEN')
dev = os.getenv('DEV_NAME')

@bot.event
async def on_ready():
  print('BlutoBot online as {0.user}'.format(bot))

# General commands
class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(help = '- Get a random emoji!')
  async def emojipls(self, ctx):
    await ctx.send(random.choice(response.emojis))
  
  @commands.command(help = '- Suggestions for what to eat.')
  async def eatwhat(self, ctx):
    await ctx.send(random.choice(responses.cuisine))

  @commands.command(help = '- Need some advice? Let Bluto tell you some.')
  async def advice(self, ctx):
    await ctx.send(random.choice(responses.advice))

  @commands.command(help = '- Get a random pic of me. Coming soon!')
  async def pic(self, ctx):
    await ctx.send(f'This feature is coming soon. Go bug {dev} to make it.')

  @commands.command(help = '- Give Bluto a stock symbol to get current its price.')
  async def stonks(self, ctx, arg):
    url = "https://finance.yahoo.com/quote/" + arg
    response = requests.get(url).content
    soup = bs4.BeautifulSoup(response, "html.parser")

    # below is the class selector for the actual stock price on YahooFinance
    price = soup.find(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    await ctx.send(f'{arg.upper()} is currently at ${price}.')

class Reminder(commands.cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def hello(self, ctx):
    await ctx.send('Hello Reminder. Curently WIP!')

bot.add_cog(General(bot))
bot.run(TOKEN)
