import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='?',intents = discord.Intents.all() )

for i in range(len(cogs)):
  cogs[i].setup(client)




client.run("OTAwNjEwMDE4OTkzMzkzNzE0.YXD0cQ.vI5nu4AJ3HYOnL9-GASkJL66OjY")