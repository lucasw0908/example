from datetime import datetime

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
    

@bot.tree.command(name="get_avatar", description="get someone's avatar")
async def get_avatar(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"{user.mention}的頭像: {user.avatar.url}")
    
    
@bot.tree.command(name="user_info", description="get someone's info")
async def user_info(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message(f"\n".join([
        f"名稱: {user.name}",
        f"ID: {user.id}",
        f"創建時間: {user.created_at}",
        f"是否為機器人: {user.bot}",
        f"是否為系統帳號: {user.system}",
        f"是否為活躍開發者: {user.public_flags.active_developer}",
    ]))
    

@bot.tree.command(name="role", description="add role to someone")
async def role(interaction: discord.Interaction, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await interaction.response.send_message(f"{member.mention}已獲得{role.mention}身分組")
    
    
@bot.tree.command(name="ban", description="ban someone")
async def ban(interaction: discord.Interaction, member: discord.Member):
    await member.ban()
    await interaction.response.send_message(f"我們摯愛的 {member.name}，於西元{datetime.now().strftime("%Y年%m月#d號")}，轟轟烈烈的死了。我們痛徹心扉，就僅僅一眨眼的時間，天人永隔。 {member.name}掙扎著走完了一段顛簸旅程，它彷彿在沉睡中做了一個美夢，夢醒了，留下陪伴我們成長過程中的點點滴滴，留下我們永恆的追思與感恩。")
    
bot.run("TOKEN")