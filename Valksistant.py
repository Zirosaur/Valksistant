import discord
from discord.ext import commands

# Ganti 'YOUR_BOT_TOKEN' dengan token bot Anda
TOKEN = 'MTI2ODg2OTI4Mjc5NjkyOTAyNA.GuWgAJ.R9SFPex698fQCJAc_nEeEWboexZmzmRtsFZ-3Y'

# Setup bot dengan prefix untuk perintah
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} telah siap!')

@bot.command()
async def hello(ctx):
    await ctx.send('Halo! Saya adalah bot.')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Menjalankan bot
bot.run(TOKEN)
