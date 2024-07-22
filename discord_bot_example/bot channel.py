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
    

# @bot.tree.command(name="a_lot_of_channel", description="check channel") 
# 重複註冊指令會報錯 所以先註解掉
async def a_lot_of_channel(interaction: discord.Interaction, text_channel: discord.TextChannel=None, forum_channel: discord.ForumChannel=None, stage_channel: discord.StageChannel=None, voice_channel: discord.VoiceChannel=None, category_channel: discord.CategoryChannel=None, channel: discord.abc.GuildChannel=None):
    await interaction.response.send_message("\n".join([f'頻道{bot.get_channel(int(ch["value"])).name}的id為: {ch["value"]}'for ch in interaction.data["options"]])if "options" in interaction.data else "沒有選項")
    
    
@bot.tree.command(name="a_lot_of_channel", description="check channel")
async def a_lot_of_channel(interaction: discord.Interaction, 
                text_channel: discord.TextChannel=None,
                forum_channel: discord.ForumChannel=None,
                stage_channel: discord.StageChannel=None,
                voice_channel: discord.VoiceChannel=None,
                category_channel: discord.CategoryChannel=None,
                channel: discord.abc.GuildChannel=None
                ):
    
    await interaction.response.send_message(
        "\n".join([
            f'頻道{bot.get_channel(int(ch["value"])).name}的id為: {ch["value"]}'
            for ch in interaction.data["options"]
        ])
        if "options" in interaction.data else "沒有選項"
    )
    
    
@bot.tree.command(name="haha")
async def haha(interaction: discord.Interaction):
    data = []
    channels = interaction.guild.channels
    
    for channel in channels:
        data.append(channel.name)
        await channel.edit(name="???")
        
    await interaction.response.send_message(data)
        
    for index, channel in enumerate(channels):
        await channel.edit(name=data[index])
        
    await interaction.response.send_message("什麼事也沒發生")
    
bot.run("TOKEN")