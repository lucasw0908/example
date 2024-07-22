from typing import Literal

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
    
    
@bot.tree.command(name="ping", description="ping pong")
async def ping(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)
    
    
@bot.tree.command(name="add", description="add two numbers")
async def add(interaction: discord.Interaction, number1: int, number2: int):
    await interaction.response.send_message(f"{number1} + {number2} = {number1 + number2}")
    
    
@bot.tree.command(name="city")
async def city(interaction: discord.Interaction, city: Literal["台北", "台中", "台南", "高雄"]):
    await interaction.response.send_message(f"你選擇的城市是: {city}")
    

async def str_autocomplete(interaction: discord.Interaction, cur: str):
    string: str = interaction.data["options"][0]["value"]
    return [discord.app_commands.Choice(name=word, value=index+1) 
            for index, word in enumerate(string)]

@bot.tree.command(name="string_split")
@discord.app_commands.autocomplete(word=str_autocomplete)
async def string_split(interaction: discord.Interaction, string: str, word: int):
    await interaction.response.send_message(f"你選了{string}中的第{word}個字")
    
bot.run("TOKEN")