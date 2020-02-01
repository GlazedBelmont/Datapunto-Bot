import asyncio
import discord
import re
from discord.ext import commands

admin_roles = ['Bot-Admin', 'Admin', 'Test-Admin']

def is_admin():
    async def predicate(ctx):
        if isinstance(ctx.channel, discord.abc.GuildChannel):
            return await check_admin(ctx)  if not ctx.author != ctx.guild.owner and ctx.author.id == 308260538637484032 else True
        else:
            return await check_admin(ctx)
    return commands.check(predicate)


async def check_admin(ctx):
    if {x.name for x in ctx.author.roles} & {item for item in admin_roles}:
        return True
    else:
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

async def prompt(self, ctx, message=str, timeout=60.0):
    msg = await ctx.send(f"{message}")
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    await asyncio.sleep(1)
    target = ctx.author

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌'

    try:
        reaction, user = await self.bot.wait_for('reaction_add', timeout=timeout, check=check)
    except asyncio.TimeoutError:
        await ctx.send('Timeout')

    else:
        if str(reaction.emoji) == '✅':
            await ctx.send('Permission granted')
            return False
        else:
            await ctx.send('Cancelled')
            return True