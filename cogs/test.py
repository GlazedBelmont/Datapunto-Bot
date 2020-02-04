import discord
import typing 
import datetime
import time
import re
import pyqrcode
import random

from pyqrcode import QRCode
from cogs.checks import is_admin, check_admin, check_bot_or_admin
from discord.ext import commands, menus

class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sdroot(self, ctx):

       print(f'Sugma')

       embed = discord.Embed()
       embed.set_image(url="https://i.imgur.com/pVS2Lc6.png")
       await ctx.send(embed=embed)

    @commands.command()
    async def dver(self, ctx):

        output = printf(discord.__version__)
        await ctx.send(f"{output}")

    @is_admin()
    @commands.command(aliases=["hidechannel"])
    async def hide(self,ctx,channels: commands.Greedy[discord.TextChannel]):
        """Hides a channel from everyone's sight. Bot-Admin only."""
        author = ctx.author
        if not channels:
            channels.append(ctx.channel)
        hidden = []
        for c in channels:
            if c.overwrites_for(ctx.guild.default_role).read_messages is False:
                await ctx.send(f"🙈️ {c.mention} is already hidden. Use `n!unhide` to unlock.")
                continue
            try:
                await c.set_permissions(ctx.guild.default_role, read_messages=False)
            except discord.errors.Forbidden:
                await ctx.send("💢 I don't have permission to do this.")
            await c.send("🙈️ Channel hidden.")
            hidden.append(c)

    @is_admin()
    @commands.command(aliases=["unhidechannel", "showchannel"])
    async def unhide(self,ctx,channels: commands.Greedy[discord.TextChannel]):
        """Unhides a channel from everyone's sight. Bot-Admin only."""
        author = ctx.author
        if not channels:
            channels.append(ctx.channel)
        unhidden = []
        for c in channels:
            if c.overwrites_for(ctx.guild.default_role).read_messages is None:
                await ctx.send(f"🧐️ {c.mention} is already unhidden. Use `n!hide` to hide.")
                continue
            try:
                await c.set_permissions(ctx.guild.default_role, read_messages=None)
            except discord.errors.Forbidden:
                await ctx.send("💢 I don't have permission to do this.")
            await c.send("🧐️ Channel unhidden.")
            unhidden.append(c)

    @commands.command()
    async def move(self,ctx,channels: commands.Greedy[discord.TextChannel], *, category: typing.Union[discord.CategoryChannel, discord.TextChannel]):

        if not channels:
            await ctx.send("Fuck you on about")
        if category == ctx.channel.category_id:
            await ctx.send(":excusemewtf:")
        else:
            await ctx.send("yeah that wont work, dude")


    @commands.guild_only()
    @commands.command()
    async def slowmode(self, ctx, time, channel: discord.TextChannel=None):
        """Apply a given slowmode time to a channel.
        
        The time format is identical to that used for timed kicks/bans/takehelps.
        It is not possible to set a slowmode longer than 6 hours.
        
        Staff only."""
        if not channel:
            channel = ctx.channel

        units = { # This bit is copied from kickban, removed days since it's not needed.
            "d": 86400,
            "h": 3600,
            "m": 60,
            "s": 1
        }
        seconds = 0
        match = re.findall("([0-9]+[smhd])", time)
        if not match:
            return await ctx.send("💢 I don't understand your time format.")
        for item in match:
            seconds += int(item[:-1]) * units[item[-1]]
        if seconds > 21600:
            return await ctx.send("💢 You can't slowmode a channel for longer than 6 hours!")
        try:
            await channel.edit(slowmode_delay=seconds)
        except discord.errors.Forbidden:
            return await ctx.send("💢 I don't have permission to do this.")
        msg = f"🕙 **Slowmode**: {ctx.author.mention} set a slowmode delay of {time} ({seconds}) in {ctx.channel.mention}"
        await self.bot.channels["modlogs"].send(msg)

    @is_admin()
    @commands.command()
    async def special(self, ctx):
        
        await ctx.send("You're specialllll!")

    @commands.command()
    async def listchans(self, ctx):
    
        await ctx.send("{guild.channels}")

    @commands.command()
    async def attach(self, ctx):
        if ctx.message.attachment:
            await ctx.send("That's not attached, right?")
        else:
            await ctx.send("attached or you're just bad at python, glazed")

    @commands.command()
    async def crash(self, ctx):
        if ctx.message.attachments:
            content += f.filename().endswith('.dmp')
            await ctx.channel.send("it works")
        else:
            await ctx.channel.send("shut")

    @commands.command()
    async def qrcode(self, ctx):
        link = "https://glazedbelmont.github.io/"
        url = pyqrcode.create(link)
        url.svg("glazedhax.svg", scale = 8)
        channel = ctx.channel
        file = discord.File("/home/glazed/DatapuntoBot/glazedhax.svg", filename="glazedhax.svg")
#        embed = discord.Embed()
#        embed.set_image(url="/home/glazedhax.svg")
        await channel.send_file()


    @commands.command()
    async def rolecheck(self, ctx):
        admin_roles = ['Bot-Admin', 'Admin', 'Test-Admin']
        userroles = (x.name for x in ctx.author.roles)
        msg = "```"
        for item in userroles:
            for item1 in admin_roles:
                if item == item1:
                    msg += f"\n{item}"
                    await ctx.send("Permission granted")
                    msg += "```"
                    await ctx.send(msg)
                    return
                else:
                    pass
        msg += "```"
        
        await ctx.send("You don't seem to have the required roles.")
 

def setup(bot):
    bot.add_cog(Test(bot))
