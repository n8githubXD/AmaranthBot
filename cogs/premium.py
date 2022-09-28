import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class premium(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="premium", description="Премиум команда №1.")
    async def premium(ctx):
            if ctx.author.id == 687959012687347751 or ctx.author.id == 676137590285402117 or ctx.author.id == 986135048543686686:
                embed2 = disnake.Embed(title = "🛒 | Это премиум-команда!", description = "Содержимое данной команды, находится в ЛС пользователя, купившего Amaranth+", color = 0xFF4232)
                embed = disnake.Embed(title = "👋 | Привет!", description = "Если ты это видишь, то ты купил Amaranth+, большое спасибо.\n\nВот твои возможности: доступ к некоторым кускам исходного кода бота, тестовые функции, эксклюзивная информация и премиум команды!", color = 0xFFFFFF)
                await ctx.author.send(embed=embed)
                await ctx.send(embed=embed2)

def setup(bot:commands.Bot):
    bot.add_cog(premium(bot))
    print(f"Ког {__name__} готов к работе.")