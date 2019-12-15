import discord

from discord.ext import commands


def is_trusted(role):
    async def predicate(ctx):
        if isinstance(ctx.channel, discord.abc.GuildChannel):
            return await check_trusted(ctx, role) if not ctx.author == ctx.guild.owner else True
        else:
            return await check_trusted(ctx)
    return commands.check(predicate)

async def check_trusted():
    BotAdmin = ctx.guild.get_role(617476156148547619)
    if BotAdmin in ctx.author.roles:
        return True
    Trusted = ctx.guild.get_role(618228078442971146)
    if Trusted in ctx.author.roles:
        return True
    else:
        return False
