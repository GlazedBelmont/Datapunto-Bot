import discord
import typing
import io
from datetime import datetime

from discord.ext import commands
from cogs.checks import is_admin, check_admin, check_bot_or_admin


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @is_admin("Test-Admin")
    @commands.command()
    async def speak(self, ctx, channel: typing.Optional[discord.TextChannel] = None, *, inp):
        if channel is None:
            channel = ctx.channel
        await channel.send(self.bot.escape_text(inp))

    @commands.command(hidden=True)
    async def sendtyping(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        await channel.trigger_typing()

    @is_admin("Admin")
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

    @commands.command()
    async def serverinfo(self, ctx):
        #archived = discord.utils.find(lambda m: m.name == 'Archived', ctx.guild.categories)
        embed = discord.Embed(title=f"{ctx.guild.name}")
        embed.set_thumbnail(url=ctx.guild.icon_url_as(static_format='png'))
        embed.description = f"ID: {ctx.guild.id}\nCreation date: {ctx.guild.created_at}\nMembers: {ctx.guild.member_count}\nOwner: {ctx.guild.owner}\nChannels: {len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)}\n"
        await ctx.send(embed=embed)


    @commands.command()
    async def archive(self, ctx):

        log_t = f"Archive of {ctx.channel} (ID: {ctx.channel.id}) "\
                      f"made on {datetime.utcnow()}\n\n\n"
        async with ctx.typing():
            async for log in ctx.channel.history(limit=None):
                # .strftime('%X/%H:%M:%S') but no for now
                log_t += f"[{log.created_at}]: {log.author} - {log.clean_content}"
                if log.attachments:
                    for attach in log.attachments:
                        log_t += f"{attach.url}\n"
                else:
                    log_t += "\n"

        aiostring = io.StringIO()
        aiostring.write(log_t)
        aiostring.seek(0)
        aiofile = discord.File(aiostring, filename=f"{ctx.channel}_archive.txt")
        await ctx.send(file=aiofile)

       
def setup(bot):
    bot.add_cog(misc(bot))
