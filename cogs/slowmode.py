import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class slowmode(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="slowmode", description="Слоумод.")
    @commands.has_permissions(manage_channels=True)
    async def slowmode(ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)   
        embed = disnake.Embed(title = "⌛ | Слоумод.", description = f"Теперь медленный режим равен {seconds} сек.", color = 0xFF4232)
        await ctx.send(embed=embed)
    
def setup(bot:commands.Bot):
    bot.add_cog(slowmode(bot))
    print(f"Ког {__name__} готов к работе.")