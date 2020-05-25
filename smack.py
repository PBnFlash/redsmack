from redbot.core import commands

class Smack(commands.Cog):

    @commands.command()
    async def smack(self, ctx):
        await ctx.send("ow!")
