import disnake
from disnake.ext import commands
import random

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class roll(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="roll", description="Бросить кубик.")
    async def roll(ctx):
        roll = random.randint(1, 6)
        embed = disnake.Embed(title = f"🎲 | {ctx.author.display_name} бросает кубик...", description = f"Вам выпало {roll}", color = 0xFF4232)
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(roll(bot))
    print(f"Ког {__name__} готов к работе.")