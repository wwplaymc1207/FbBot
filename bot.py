import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='w!')

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

bot.run('OTAyNDI1MDQ5MTA4MTkzMjgw.YXeO0Q.RByYawRkHoRPh1oC5aKdnvs4wDA')
