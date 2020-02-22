import asyncio
import discord
from subprocess import call
from discord.ext import commands
from cogs.checks import is_admin, check_admin, check_bot_or_admin


class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def escape_text(text):
        text = str(text)
        return discord.utils.escape_markdown(discord.utils.escape_mentions(text))
    
    @commands.command(aliases=["clear"])
    @is_admin()
    async def purge(self, ctx, limit: int):
        """Clears a given number of messages. Admins only."""
        await ctx.channel.purge(limit=limit+1)
        tmp = await ctx.send("Clearing the selected messages")
        await asyncio.sleep(4)
        await tmp.delete()


    @commands.command(aliases=["lock"])
    @commands.has_role(617476156148547619)
    async def lockdown(self, ctx, channels: commands.Greedy[discord.TextChannel]):
        """Lock message sending in the channel for everyone. Bot-admin only."""
        author = ctx.author
        if not channels:
            channels.append(ctx.channel)
        locked_down = []
        for c in channels:
            if c.overwrites_for(ctx.guild.default_role).send_messages is False:
                await ctx.send(f"🔒 {c.mention} is already locked down. Use `.unlock` to unlock.")
                continue
            try:
                await c.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
                await c.set_permissions(ctx.guild.roles['569977251236544521'], send_messages=False)
            except discord.errors.Forbidden:
                await ctx.send("💢 I don't have permission to do this.")
            await c.send("🔒 Channel locked down. Only the owner may speak.")
            locked_down.append(c)

    @commands.command(aliases=["ulock"])
    @commands.has_role(617476156148547619)
    async def unlock(self, ctx, channels: commands.Greedy[discord.TextChannel]):
        """Unlock a locked channel"""
        author = ctx.author
        if not channels:
            channels.append(ctx.channel)
        unlocked = []
        for c in channels:
            if c.overwrites_for(ctx.guild.default_role).send_messages is True:
                await ctx.send(f"🔓️ {c.mention} is already unlocked. Use `n!lockdown` to lock.")
                continue
            try:
                await c.set_permissions(ctx.guild.default_role, send_messages=True, read_messages=None)
            #    await c.set_permissions(ctx.guild.roles['569977251236544521'], send_messages=None)
            except discord.errors.Forbidden:
                await ctx.send("💢 I don't have permission to do this.")
            await c.send("🔓️ Channel unlocked.")
            unlocked.append(c)

    @commands.guild_only()
    @commands.command(hidden=True)
    async def userinfo(self, ctx, u: commands.Greedy[discord.Member]=None):
        """Prototype of a new userinfo"""

        if not u:
            u = ctx.author

        if not ctx.guild.get_member(u.id):
            u = await self.bot.fetch_user(u.id)
            guild_member = False
            role = None
            try:
                ban = await ctx.guild.fetch_ban(u)
            except discord.NotFound: #NotFound is raised if the user isn't banned
                ban = None
        else:
            ban = None
            guild_member = None
            u = ctx.guild.get_member(u.id)
            role = u.top_role.name
          
        embed = discord.Embed(title=f"Userinfo for {u}")
        embed.description=f"Name = {u.name}\nID = {u.id}\nDiscriminator = {u.discriminator}\nAvatar = {u.avatar}\nBot = {u.bot}\nCreated_at = {u.created_at}\nDisplay_name = {self.escape_text(u.display_name)}\n{f'Joined_at = {u.joined_at}' if guild_member is None else ''}\n{f'Status = {u.status}' if guild_member is None else ''}\n{f'Activity = {u.activity.name if u.activity else None}' if guild_member is None else ''}\nColour = {u.colour}\n{f'Top_role ={self.escape_text(role)}' if role is not None else ''}{f'**Banned**, reason: {ban.reason}' if ban is not None else ''}"
        embed.set_thumbnail(url=u.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(mod(bot))

