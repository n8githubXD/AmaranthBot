import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class support(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="support", description="Сервер поддержки.")
    async def support(ctx):
        embed = disnake.Embed(title = "❓ | Сервер поддержки.", description = "https://discord.gg/GzgqYTPvKj", color = 0xFF4232)
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(support(bot))
    print(f"Ког {__name__} готов к работе.")