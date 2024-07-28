import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

load_dotenv()

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def run(self, *args, **kwargs):
        super().run(os.getenv("token"))
    
    
bot = Bot(command_prefix='!', intents=discord.Intents.all())