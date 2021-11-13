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
    await bot.change_presence(activity=discord.Game(name=f'w!help | 已被邀请至 {len(bot.guilds)} 个服务器'))

bot.remove_command('help')
@bot.command()
async def help(ctx):
    help = discord.Embed(title="指令说明", color=0xffff8a)
    help.set_author(name="凋凋的可爱机器人", icon_url="https://cdn.discordapp.com/avatars/902425049108193280/d7fdedddf2b86e74ccdab706940d0b77.png?size=80")
    help.add_field(name="Help \nAdhelp \nPing \nDice", value="** **")
    await ctx.send(embed=help)

@bot.command()
async def load(self, ctx, extension):
    myID = 826714957517291552
    if ctx.author.id == myID:
        self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f"{extension} 已加载完毕哥哥~")

@bot.command()
async def unload(self, ctx, extension):
    myID = 826714957517291552
    if ctx.author.id == myID:
        self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f"{extension} 已取消加载完毕哥哥~")

@bot.command()
async def reload(self, ctx, extension):
    myID = 826714957517291552
    if ctx.author.id == myID:
        self.bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f"{extension} 已重新加载完毕哥哥~")

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
