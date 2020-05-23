import asyncio
import discord
from subprocess import call
from discord.ext import commands
from cogs.checks import is_admin, prompt


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_eval_result = None
        self.previous_eval_code = None



    @is_admin("Bot-Admin")
    @commands.command(aliases = ['reboot', 'restart'])
    async def close(self, ctx):
        """Reboots the bot"""
        await ctx.channel.send("Ah shit, here we go again")
        await self.bot.close()

#    @commands.command(hidden=True)
#    @commands.has_role(575834911425167414)
#    async def fullclose(self, ctx):
#        await self.bot.async_call_shell("")

    @is_admin("GlaZy")
    @commands.command()
    async def guildleave(self, ctx, serverid: int):
        """Leaves a server"""
        server = self.bot.get_guild(serverid)
        await ctx.send(f"{server}")

        if server not in self.bot.guilds:
            await ctx.send("I'm not even in this server apparently")
            return
        else:
            if serverid is None:
                server = self.bot.get_guild(ctx.guild.id)

        if server != self.bot.get_guild(554178232531025940) and server != self.bot.get_guild(632566001980145675):
            await ctx.send(f"I'll be leaving {server}")

            if await prompt(self, ctx, "Continue?"):
                return
            await ctx.send(f"I have left {server}")
            await server.leave()
                
        else:
            await ctx.send(f"I cannot leave `{server}`\nIt's my home <:blobaww:569934894952611851>")
        
    @commands.command()
    async def prompttest(self, ctx):
        """Self explanatory"""
        if await prompt(self, ctx, "Am I a good bot?"):
            return
        await ctx.send("<:blobaww:569934894952611851>")

    @is_admin("Admin")
    @commands.command(hidden=True)
    async def invite(self, ctx, duration:int=0, uses:int=0, *, reason=""):
        """Generates an invite link
            - Duration (int)
            - Maximum uses (int)
            - Reason (str)"""
        msg = ""
        if duration == 0:
            duration = 0
        if uses == 0:
            uses = 0

        msg += str(await ctx.channel.create_invite(reason=reason,max_age=duration, max_uses=uses, temporary=False, unique=False))
        if reason is "":
            msg += "\nPlease add a reason next time"
        else:
            msg += f"\n{reason}"

        await ctx.send(msg)

    @is_admin("Bot-Admin")
    @commands.command(hidden=True)
#    @commands.has_role(575834911425167414)
    async def give(self, ctx, roles: commands.Greedy[discord.Role], *, users: discord.User):
        """Gives the specified role to a user(s)"""
        members = []

#        if len(roles) > 1:
#            for role in roles:
#                await users.add_roles(role)
#        else:
#            await users.add_roles(roles)
#            members.append(users.name)

        members.sort(key=str.casefold)
        msg = f"``The following roles:\n"

        if len(roles) > 1:
            for role in roles:
                await users.add_roles(role)
                msg += f"- {role.name}\n"
        else:
            await users.add_roles(roles)
            msg += f"- {roles}\n"

        msg += f"have been given to the following users:\n"
        for member in members:
            msg += f"{member}\n"
        else:
            msg += f"{users.name}"
        msg += "``"

        await ctx.send(msg)

            
        
def setup(bot):
    bot.add_cog(admin(bot))
