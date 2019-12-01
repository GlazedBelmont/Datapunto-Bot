from discord.ext import commands

class SubfolderSampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bar(self, ctx):
        '''Sends bar'''
        await ctx.send('foo')

def setup(bot):
    bot.add_cog(SubfolderSampleCog(bot))
