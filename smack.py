from redbot.core import commands
        
class Smack(commands.Cog):

    @commands.command()
    async def bonk(self, commands.Context):
        await ctx.send("ow!")
