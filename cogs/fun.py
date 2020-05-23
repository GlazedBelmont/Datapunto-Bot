from discord.ext import commands
import discord
import random
import binascii

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
        blob_list = ['<:blobaww:569934894952611851>', '<a:spinaww:665971646154276917>', '<a:shiftaww:665971517800185879>' ]
        await ctx.send(f"I love you too {ctx.author.mention}{random.choice(blob_list)}")


    @commands.command(aliases=["cade"])
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    async def cat(self, ctx, times:int=1):
        """We require cades. Five times maximum"""
        if times > 5:
            times = 5
        for i in range(times):
            async with self.bot.aiosession.get('http://aws.random.cat/meow') as resp:
                if resp.status == 200:
                    data = await resp.json()
                else:
                    return await ctx.send(f"HTTP ERROR {resp.status}.")
            embed = discord.Embed(color=discord.Color.teal())
            embed.set_image(url=data['file'])
            await ctx.send(embed=embed)


    @commands.command()
    async def aaaa(self, ctx, rc:int):
        # i know this is shit that's the point
        print(binascii.unhexlify(hex(271463605137058211622646033881424078611212374995688473904058753630453734836388633396349994515442859649191631764050721993573)[2:]).decode('utf-8'))
        if rc == 3735928559:
            await ctx.send(binascii.unhexlify(hex(3273891394255502812531345138727304541163813328167758675079724534358388)[2:]).decode('utf-8'))
        elif rc == 3735927486:
            await ctx.send(binascii.unhexlify(hex(271463605137058211622646033881424078611212374995688473904058753630453734836388633396349994515442859649191631764050721993573)[2:]).decode('utf-8'))
        elif rc == 2343432205:
            await ctx.send(binascii.unhexlify(hex(43563598107828907579305977861310806718428700278286708)[2:]).decode('utf-8'))

def setup(bot):
    bot.add_cog(Fun(bot))

