import code
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class code(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="code", description="Куски кода бота.")
    async def code(ctx):
            if ctx.author.id == 687959012687347751 or ctx.author.id == 676137590285402117 or ctx.author.id == 692374412376145940 or ctx.author.id == 986135048543686686:
                embed2 = disnake.Embed(title = "🎁 | Это премиум-команда!", description = "Содержимое данной команды, находится в ЛС пользователя, купившего Amaranth+", color = 0xFF4232)
                embed = disnake.Embed(title = "💻 | Исходный код:", description = "**Команда support:**\n```py\n@commands.slash_command(name=""support"", description=""Сервер поддержки."")\nasync def support(ctx):\nembed = disnake.Embed(title = ""Сервер поддержки."", description = ""https://discord.gg/GzgqYTPvKj"", color = 0xFFFFFF)\nawait ctx.send(embed=embed)```", color = 0xFFFFFF)
                await ctx.author.send(embed=embed)
                await ctx.send(embed=embed2)

def setup(bot:commands.Bot):
    bot.add_cog(code(bot))
    print(f"Ког {__name__} готов к работе.")