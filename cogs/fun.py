from discord.ext import commands
import discord
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=20.0, type=commands.BucketType.channel)
    async def blobaww(self, ctx):
        msg = "You thought I couldn't <:blobaww:569934894952611851>\nwell I can <:blobaww:569934894952611851> all I want, this is my server after all.\n<:blobaww:569934894952611851> <:blobaww:569934894952611851> <:blobaww:569934894952611851>"
        await ctx.send(msg)

    @commands.command()
    @commands.cooldown(rate=1, per=20.0, type=commands.BucketType.channel)
    async def ily(self, ctx):
        blob_list = ['<:blobaww:569934894952611851>', '<:spinaww:665971646154276917>', '<:shiftaww:665971517800185879>' ]
        await ctx.send(f"I love you too {ctx.author.mention}{random.choice(blob_list)}")
def setup(bot):
    bot.add_cog(Fun(bot))

