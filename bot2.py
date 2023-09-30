import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def weekend(ctx):
    await ctx.send(f'Hi aku {bot.user}, liburan dong ajak aku')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTE1NTA2MzkxMjY3NzUxOTQ2MA.G_mBmy.82Zzx8TRcvXY8ZJF3mX1dHMMyava9Npvv3oFWk")
