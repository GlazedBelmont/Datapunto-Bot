import discord

from discord.ext import commands


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f'Cog "{self.qualified_name}" loaded')


    @commands.command()
    @commands.has_role(617476156148547619)
    async def speak(self, ctx, channel: discord.TextChannel, *, inp):
        await channel.send(inp)

    @commands.command(hidden=True)
    async def sendtyping(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        await channel.trigger_typing()

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

def setup(bot):
    bot.add_cog(misc(bot))
