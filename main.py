import discord
from discord.ext import commands
from bot_token import TOKEN
from bot_logic import predict_image

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
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def detect(ctx):
    
    if ctx.message.attachments: #eleman varsa True
        await ctx.send("Algılama başladı")
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            filepath = f"M7L1/images/{filename}"
            await attachment.save(filepath) #f-string
            name, score = predict_image(filepath, "M7L1/keras_model.h5", "M7L1/labels.txt")
            await ctx.send(name, score)
    else:
      await ctx.send("Lütfen komutla birlikte fotoğraf ekleyin")

bot.run(TOKEN)