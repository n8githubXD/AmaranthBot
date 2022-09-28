import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class ping(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name= "ping", description= "Задержка бота.")
    async def ping(self, ctx):
        embed = disnake.Embed(title = "🏓 | Понг!", description = f"Задержка бота: **{round(self.bot.latency * 1000)}ms**", color = 0xFF4232)
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(ping(bot))
    print(f"Ког {__name__} готов к работе.")