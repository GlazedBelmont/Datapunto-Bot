import discord

from discord.ext import commands
from cogs.checks import is_admin, check_admin, check_bot_or_admin


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @is_admin()
    @commands.command()
    async def speak(self, ctx, channel: discord.TextChannel, *, inp):
        await channel.send(inp)

    @commands.command(hidden=True)
    async def sendtyping(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        await channel.trigger_typing()

    @is_admin()
    @commands.command(hidden=True)
    async def dm(self, ctx, member: discord.Member, *, inp):
        try:
            await member.send(inp)
        except (discord.HTTPException, discord.Forbidden):
            await ctx.send("Failed to send dm!")

    @commands.command(hidden=True)
    async def BotAdmin(self, ctx):
        BotAdmin = ctx.guild.get_role(617476156148547619)
        if BotAdmin in ctx.author.roles:
            await ctx.send("Yeah Boi")
        else:
            await ctx.send("Nope")

    @commands.command()
    async def myroles(self, ctx):
        msg = "```peepee\nRoles:\n"
        userroles = (x.name for x in ctx.author.roles)
        for item in userroles:
            msg += f"{item}\n"
        msg += "```"
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(misc(bot))
