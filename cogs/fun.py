from discord.ext import commands
import discord

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f'Cog "{self.qualified_name}" loaded')


    @commands.command(aliases=['nemoji'])
    async def nitroemoji(self, ctx, emojiname):
        """Posts either an animated emoji or non-animated emoji if found"""
        emoji = discord.utils.get(self.bot.emojis, name=emojiname)
        if emoji:
            await ctx.send(emoji)
        else:
            return await ctx.send("No Emote Found!")

def setup(bot):
    bot.add_cog(Fun(bot))

