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
    
    
@bot.tree.command(name="get_guild_info", description="取得伺服器資訊")
@commands.guild_only()
async def get_guild_info(interaction: discord.Interaction):
    await interaction.response.send_message("\n".join([
        f"伺服器名稱: {interaction.guild.name}",
        f"伺服器擁有者: {interaction.guild.owner.name}",
        f"伺服器人數: {interaction.guild.member_count}",
        f"頻道數: {len(interaction.guild.channels)}",
        f"身分組數: {len(interaction.guild.roles)}"
        ]))
    
    
async def emoji_autocomplete(interaction: discord.Interaction, cur: str):
    emojis = interaction.guild.emojis
    output = [discord.app_commands.Choice(name=e.name, value=str(e.id)) for e in emojis]
    if cur not in [e.name for e in emojis]:
        return output[:25]
    index = [e.name for e in emojis].index(cur)
        
    return output[index:index+25]


@bot.tree.command(name="create_channel", description="創建頻道")
@commands.guild_only()
async def create_channel(interaction: discord.Interaction, name: str, type: Literal["text", "voice", "forum", "stage"]):
    
    if name in [channel.name for channel in interaction.guild.channels]:
        await interaction.response.send_message("頻道已存在")
        return
    
    await interaction.guild._create_channel(name=name, channel_type=discord.ChannelType[type])
    await interaction.response.send_message(f"已創建頻道: {name}")
    
    
@bot.tree.command(name="get_emoji", description="get emoji image")
@commands.guild_only()
@discord.app_commands.autocomplete(emoji=emoji_autocomplete)
async def get_emoji(interaction: discord.Interaction, emoji: str):
    
    for e in interaction.guild.emojis:
        if str(e.id) == emoji:
            await interaction.response.send_message(file=await e.to_file()) 

bot.run("TOKEN")