import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class shutdown(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="shutdown", description="Выключить бота.")
    async def shutdown(self, ctx):
        if ctx.author.id == 687959012687347751:
            embed = disnake.Embed(title="Выключение...", description="Пока! :wave:", color=0xFF4232)
            await ctx.send(embed=embed)
            await self.bot.close()

def setup(bot:commands.Bot):
    bot.add_cog(shutdown(bot))
    print(f"Ког {__name__} готов к работе.")