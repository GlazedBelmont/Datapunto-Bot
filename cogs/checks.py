import asyncio
import discord
import re
from discord.ext import commands

admin_roles = ['Bot-Admin', 'Admin', 'Test-Admin']

def is_admin():
    async def predicate(ctx):
        if isinstance(ctx.channel, discord.abc.GuildChannel):
            return await check_admin(ctx)  if not ctx.author == ctx.guild.owner or if not ctx.author == 308260538637484032 else True
        else:
            return await check_admin(ctx)
    return commands.check(predicate)


async def check_admin(ctx):
    userroles = (x.name for x in ctx.author.roles)
    for item in userroles:
        for item1 in admin_roles:
            if item == item1:
                return True
            else:
                pass
    
    await ctx.send(f"You don't have the permission to run ```{ctx.command.qualified_name}```")
    return False

    

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


async def intprompt(self, message, *, timeout=60.0, delete_after=True, author_id=None):
    fmt = f'{message}\n\nAdd \N{WHITE HEAVY CHECK MARK} to confirm or \N{CROSS MARK} to cancel.'

    author_id = author_id 
    msg = await self.send(fmt)

    confirm = None

    def react_check(payload):
        nonlocal confirm

        if payload.message_id != msg.id or payload.user_id != author_id:
            return False
        
        codepoint = str(payload.emoji)

        if codepoint == '\N{WHITE HEAVY CHECK MARK}':
            confirm = True
            return True
        elif codepoint == '\N{CROSS MARK}':
            confirm = False
            return True

        return False

    for emoji in ('\N{WHITE HEAVY CHECK MARK}', '\N{CROSS MARK}'):
        await msg.add_reaction(emoji)

    try:
        await self.bot.wait_for('raw_reaction_add', react_check=react_check, timeout=timeout)
    except asyncio.TimeoutError:
        confirm = None

    try:
        if delete_after:
            await msg.delete()
    finally:
        return confirm
