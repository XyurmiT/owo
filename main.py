import discord
from discord.ext import commands
from colorama import Fore
import asyncio
from webserver import keep_alive
import os


prefix = "$$"

keep_alive()

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.offline)
    print("Bot is ready!")




@bot.command()
async def helpowo(ctx):
    await asyncio.sleep(1)
    await ctx.message.delete()
    await ctx.send('**$$AutoOwO= Owo slots 5000 , owo flip 5000. $$stopautoOwO= Stops the bot. bybasses ban**')

@bot.command()
async def stopautoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('**AutoOwO is now Disabled 😊 $$ AutoOwo to enable it again!**')
    global dmcs
    dmcs = False


@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('**AutoOwO is now enabled enjoy 😊! Thanks for using this script.**')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)    
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(10)
            await ctx.send('owo h')
            await asyncio.sleep(10)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)
            await ctx.send('owo h')
            await asyncio.sleep(15)
            await ctx.send('owo b')
            await asyncio.sleep(10)
            await ctx.send ('owo flip 3000')
            await asyncio.sleep(10)
            await ctx.send('owo slots 3000')
            await asyncio.sleep(20)            
            print('break for 1 hour 30 mins')
            await asyncio.sleep(5400)
            

            

            




bot.run(os.getenv('token'), bot=False)