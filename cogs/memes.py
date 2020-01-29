import discord
from discord.ext import commands
import random
import math

class Memes(commands.Cog):
    def __init__(self, bot):
        """Approved™ memes"""
        self.bot = bot

    async def _meme(self, ctx, msg, directed: bool = False, imagelink=None):
        author = ctx.author
        if isinstance(ctx.channel, discord.abc.GuildChannel):
            await ctx.message.delete()
            try:
                await ctx.author.send("Meme commands are disabled in this channel, or your privileges have been revoked.")
            except discord.errors.Forbidden:
                await ctx.send(f"{ctx.author.mention} Meme commands are disabled in this channel, or your privileges have been revoked.")
        elif imagelink != None:  
            title = f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}"        
            embed = discord.Embed(title=title, color=discord.Color.default())
            embed.set_image(url=imagelink)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{self.bot.escape_text(ctx.author.display_name) + ':' if not directed else ''} {msg}")

    @commands.command()
    async def listmemes(self, ctx):
        """Lists meme commands"""
        embed = discord.Embed(description="\n")
        embed.description += ", ".join([x.name for x in self.get_commands() if x != self.listmemes])
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def astar(self, ctx):
        """Here's a star just for you."""
        await ctx.send(f"{ctx.author.display_name}: https://i.imgur.com/vUrBPZr.png")

    @commands.command(name="bean", hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def bean(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        await ctx.send(f"{member.mention} is now beaned <:beanart2:603774263836540958>")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def cryofreeze(self,ctx):
        """Cryofreezes a user"""
        await ctx.send(f"<:cryo:589257077789294606><:freeze:589257125226872843>")

    @commands.command(hidden=True, aliases=['inori'])
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def hifumi1(self, ctx):
        """Disappointment"""
        await ctx.send(f"{ctx.author.display_name}: https://i.imgur.com/jTTHQLs.gifv")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def knuckles(self, ctx):
        # It's just as bad
        re_list = ['to frii gaems', 'to bricc', 'to get frii gaems', 'to build sxos',
                   'to play backup games', 'to get unban', 'to get reinx games',
                   'to build atmos', 'to brick my 3ds bc ebay scammed me', 'to plz help me'] 
        whenlifegetsatyou = ['?!?!?', '?!?!', '.', '!!!!', '!!', '!']
        await ctx.send(f"Do you know da wae {random.choice(re_list)}{random.choice(whenlifegetsatyou)}")

    @commands.command(name="neo-ban", aliases=['neoban'], hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def neoban(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author

        await ctx.send(f"{member.mention} is now neo-banned!")


    @commands.command(name="succ", aliases=['suck'], hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def succ(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author

        await ctx.send(f"{member.mention} was sucked!\n **YOU REALLY SUCK ,DON'T YOU!**")


    @commands.command(name="slap",hidden=True)
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def slap(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        embed = discord.Embed()
        embed.set_image(url="https://i.imgur.com/TEnF9UN.gif?noredirect")
        await ctx.send(f"{member.mention} was slapped!", embed=embed)

    @commands.command(aliases=['discordcopypasta'])
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.channel)
    async def discordcopypaste(self, ctx, member: discord.Member=None):
        """Generates a discord copypaste
        
        If no arguments are passed, it uses the author of the command.
        
        If you fall for this, you should give yourself a solid facepalm."""
        if member is None:
            member = ctx.author
        org_msg = f"Look out for a Discord user by the name of \"{member.name}\" with"\
                  f" the tag #{member.discriminator}. "\
                  "He is going around sending friend requests to random Discord users,"\
                  " and those who accept his friend requests will have their accounts "\
                  "DDoSed and their groups exposed with the members inside it "\
                  "becoming a victim aswell. Spread the word and send "\
                  "this to as many discord servers as you can. "\
                  "If you see this user, DO NOT accept his friend "\
                  "request and immediately block him. Our team is "\
                  "currently working very hard to remove this user from our database,"\
                  " please stay safe."

        await ctx.send(org_msg)
       
    def c_to_f(self, c):
        return math.floor(9.0 / 5.0 * c + 32)

    def c_to_k(self, c):
        return math.floor(c + 273.15)

    @commands.command(hidden=True, name="warm")
    async def warm(self, ctx, user: discord.Member):
        celsius = random.randint(15, 100)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await ctx.send(f"{user.mention} warmed."
                       f" User is now {celsius}°C "
                       f"({fahrenheit}°F, {kelvin}K).")

    @commands.command(hidden=True, name="chill", aliases=["cool"])
    async def chill(self, ctx, user: discord.Member):
        celsius = random.randint(-50, 15)
        fahrenheit = self.c_to_f(celsius)
        kelvin = self.c_to_k(celsius)
        await ctx.send(f"{user.mention} chilled."
                       f" User is now {celsius}°C "
                       f"({fahrenheit}°F, {kelvin}K).")

    @commands.command(hidden=True, name="bam")
    async def bam_member(self, ctx, target: discord.Member):
        """Bams a user owo"""
        safe_name = await commands.clean_content().convert(ctx, str(target))
        await ctx.send(f"{safe_name} is ̶n͢ow b̕&̡.̷ 👍̡")

    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    async def screams(self, ctx):
        """Memes."""
        await self._meme(ctx, "lalalala", imagelink="http://i.imgur.com/j0Dkv2Z.png")
    
    @commands.command(hidden=True)
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
    async def headpat(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
        await ctx.send(f'{member.mention} <:blobpat:671470684756508672>')

def setup(bot):
    bot.add_cog(Memes(bot))
