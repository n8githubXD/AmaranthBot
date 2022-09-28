import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class buy(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="buy", description="Покупка Amaranth+.")
    async def buy(ctx):
                embed2 = disnake.Embed(title = "🛒 | Купить Amaranth+", description = "Инструкция как купить Amaranth+ находится в ЛС.", color = 0xFF4232)
                embed = disnake.Embed(title = "🛒 | Купить Amaranth+", description = "**Шаг 1**: Кинуть обмен в Steam на сумму 20+ рублей. https://steamcommunity.com/tradeoffer/new/?partner=1195228060&token=0cVhqsGb\n\n**Шаг 2**: Написать n8#2556 о своем трейде, он начислит вам Amaranth+\n\nОплата ежемесячно, можем вернуть вам деньги.", color = 0xFFFFFF)
                await ctx.author.send(embed=embed)
                await ctx.send(embed=embed2)
                
def setup(bot:commands.Bot):
    bot.add_cog(buy(bot))
    print(f"Ког {__name__} готов к работе.")