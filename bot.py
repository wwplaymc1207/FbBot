import discord
from discord.ext import commands
import json
import random
import time
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='w!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    await bot.change_presence(activity=discord.Game(name=f'w!help'))

bot.remove_command('help')
@bot.command()
async def help(ctx):
    help = discord.Embed(title="指令说明", color=0xffff8a)
    help.set_author(name="凋凋的可爱机器人", icon_url="https://cdn.discordapp.com/avatars/902425049108193280/d7fdedddf2b86e74ccdab706940d0b77.png?size=80")
    help.add_field(name="Help \nAdhelp \nPing \nDice", value="** **")
    await ctx.send(embed=help)

@bot.command()
async def load(ctx, extension):
    myID = 826714957517291552
    if ctx.author.id == myID:
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f"已加载完毕 {extension} 了哦哥哥~")

@bot.command()
async def unload(ctx, extension):
    myID = 826714957517291552
    if ctx.author.id == myID:
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f"已取消加载完毕 {extension} 了哦哥哥~")

@bot.command()
async def reload(ctx, extension):
    myID = 826714957517291552
    if ctx.author.id == myID:
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f"已重新加载完毕 {extension} 了哦哥哥~")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("你没输入参数哦哥哥~")
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("没有这个指令哦哥哥~")
    elif isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("你没权限使用这个指令哦哥哥~")
    elif isinstance(error, commands.errors.MissingRole):
        await ctx.send("你没指定身分组使用这个指令哦哥哥~")
    else:
        await ctx.send("完蛋了系统发生错误qwq")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
