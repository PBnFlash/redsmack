from redbot.core import commands

class Smack(commands.Cog):

    @commands.command()
    async def bonk(self, ctx):
        await ctx.send("ow!")
