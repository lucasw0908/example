import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    slash_commands = await bot.tree.sync()
    print("\n".join([f"已註冊: {sc.name}"for sc in slash_commands]))
    print(f"{bot.user} logged in!")
    

@bot.tree.command(name="hello", description="hello world")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, World!")

bot.run("TOKEN")