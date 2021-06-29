import discord
from discord.utils import get
from discord.ext.commands import Bot
from dotenv import load_dotenv
from itertools import cycle
import os


load_dotenv()  

TOKEN = os.environ.get('DISCORD_TOKEN')

bot = Bot(command_prefix='.')





bot.load_extension("helper_cogs.course_cog")
bot.run(TOKEN)