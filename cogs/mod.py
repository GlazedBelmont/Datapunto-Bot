import asyncio
import discord
from discord.ext import commands

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=["clear"])
    @commands.has_role(617476156148547619)
    async def purge(self, ctx, limit: int):
        """Clears a given number of messages. Staff only."""
        await ctx.channel.purge(limit=limit+1)
        tmp = await ctx.send("Cleared the selected messages")
        await asyncio.sleep(4)
        await tmp.delete()


    @commands.command(aliases=["lock"])
    @commands.has_role(617476156148547619)
    async def lockdown(self, ctx, channels: commands.Greedy[discord.TextChannel]):
        """Lock message sending in the channel for everyone. Owners only."""
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
                await c.set_permissions(ctx.guild.default_role, send_messages=None, read_messages=None)
                await c.set_permissions(ctx.guild.roles['569977251236544521'], send_messages=None)
            except discord.errors.Forbidden:
                await ctx.send("💢 I don't have permission to do this.")
            await c.send("🔓️ Channel unlocked.")
            unlocked.append(c)

def setup(bot):
    bot.add_cog(mod(bot))

