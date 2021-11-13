import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='w!')

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata=json.load(jfile)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(905220048090714162)
    await channel.send(f'{member} 欢迎加入FBSMP!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(905220048090714162)
    await channel.send(f'{member} 离开了FBSMP!qwq')
bot.run(jdata['token'])
