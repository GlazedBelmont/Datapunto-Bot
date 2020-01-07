import discord
import re
from discord.ext import commands

admin_roles = {"Bot-Admin", "Admin", "Test-Admin"}

def is_admin():
    async def predicate(ctx):
        if isinstance(ctx.channel, discord.abc.GuildChannel):
            return await check_admin(ctx) if not ctx.author == ctx.guild.owner else True
        else:
            return await check_admin(ctx)
    return commands.check(predicate)


async def check_admin(ctx):
    msg = ""
    for x in ctx.author.roles:
        msg += f"{x.name}\n"
        print(f'{x.name}')
    if x.name in admin_roles:
        return True
    else:
        return False
    return await ctx.send("You are not an admin.")

async def check_bot_or_admin(ctx, role, target: discord.member, action: str):
    if target.bot:
        who = "a bot"
    elif target == ctx.author:
        who = "yourself"
    elif role == "BotAdmin":
        if ctx.guild.get_role(617476156148547619) in target.roles:
            who = "a Bot-Admin"
    elif role == "Admin":
        if ctx.guild.get_role(627989593454804995) in target.roles:
            who = "an Admin"
    else:
        return False

    return await ctx.send(f"you cannot do the {action} command on {who}.")

async def on_reaction_add(reaction, user):
        if reaction.emoji == emote:
            if user == ctx.author:
                return True
            else:
                return False
        else:
            False