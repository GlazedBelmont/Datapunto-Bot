import asyncio
import discord
import re
from discord.ext import commands

admin_roles = {'GlaZy': 0, 'Bot-Admin': 1, 'Admin': 2, 'Test-Admin': 3} # Aight look, I know Kurisu uses that too but it's a good way to check

def is_admin(role=None):
    async def predicate(ctx):
        if isinstance(ctx.channel, discord.abc.GuildChannel):
            return await check_admin(ctx, role)  if not ctx.author == ctx.guild.owner and ctx.author.id != 308260538637484032 else True
        else:
            return await check_admin(ctx, role)
    return commands.check(predicate)


#async def check_admin(ctx, role):
#    if {x.name for x in ctx.author.roles} & {item for item in admin_roles}:
#        return True
#    else:
#        return False

async def check_admin(ctx, role):
    try:
        admin_role_check = list({role.name for role in ctx.author.roles} & {x for x in admin_roles})[0] # only returns the first match which will be the highest admin rank the user has
        if role is None: # global admin check basically
            return True
        if admin_roles[admin_role_check] <= admin_roles[role]: # Are you the correct rank
            return True
        else:
            return False
    except IndexError: # You don't have one of the admin roles
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