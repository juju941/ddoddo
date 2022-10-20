import discord
from discord.ext.commands import Bot

intents = discord.Intents.default()

# !로 시작하면 명령어로 인식
bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user}')

# !hello 명령어 처리
@bot.command()
async def hello(ctx):
  await ctx.reply('Hi, there!')

# !bye 명령어 처리
@bot.command()
async def bye(ctx):
  await ctx.reply('See you later!')

bot.run("NzkzMDc3NzY0NzA5NDE3MDEx.GE0ckE.2a1aXMthCNcCgxgFL8q2NBC5OnxUQEOFMzRnSY")