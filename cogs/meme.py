import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class meme(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="meme", description="Не работает.")
    async def meme(ctx):
        embed = disnake.Embed(title = "❌ | Эта комадна не работает.", description = "Скоро мы это исправим.", color = 0xFF4232)
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(meme(bot))
    print(f"Ког {__name__} готов к работе.")