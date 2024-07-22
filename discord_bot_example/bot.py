import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} logged in!")
    
@bot.command(name="hello")
async def hello(ctx: commands.context.Context):
    await ctx.send("Hello, World!")

bot.run("TOKEN")