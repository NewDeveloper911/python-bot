import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)
    
@client.command()
async def slaphard(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = " and ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))
  
@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.command()
async def hello(ctx):
    await ctx.send("Hi there, " + str(ctx.author) + " of the " + str(ctx.guild) + ".")
    
@client.command()
async def info(ctx):
    embed = discord.Embed(
        title = "Introduction to Slither and its commands",
        descriptiion = "Slither is a bot made by @wakandawarrior to spice up and try to aid all of those involved in this server. If you have any ideas as to how I may be improved, please talk to him",
        colour = discord.Colour(int("0dfaab", 16))
    )
    
    embed.set_footer(text="Created by an absolute novice")
    embed.set_image(url='https://cdn.discordapp.com/avatars/684973286438076437/11d7951e4e89d4b97b7f93b641770917.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/750429563028242512/2642f6de2a014e54f1ef29ccdfa9a1a3.png')
    embed.set_author(name='Nana', icon_url='https://cdn.discordapp.com/avatars/684973286438076437/11d7951e4e89d4b97b7f93b641770917.png')
    embed.add_field(name='!slaphard',value='Use slaphard to intentionally target a person or more with the wrath of your hand.    For example, !slaphard @crocodilefag @wakandawarrior someone must face my wrath', inline=False)
    embed.add_field(name='!slap', value='!slap is used to randomly targeta single person.A reason why also needs to be included. For example, !slap you stole my virignity', inline=False) 
    
    await ctx.send(embed=embed)
    
@client.command()
async def add_roles(ctx):
    member = ctx.message.author
    role = discord.utils.get(member.guild.roles, name="The crocodile hunter")
    await discord.Member.add_roles(member, role)
    
client.run("NzUwNDI5NTYzMDI4MjQyNTEy.X06Z_g.G1hAF3E1chz8xghibATUGEqJKmA")