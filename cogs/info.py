import main
import disnake
from disnake.ext import commands
import psutil

bot_ram = psutil.virtual_memory().percent

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class info(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name= "info", description= "Информация о боте.")
    async def info(self, ctx):
        embed = disnake.Embed(title = "❓ | Информация.", color = 0xFF4232)
        embed.add_field(name="Система.", value=f":notebook_with_decorative_cover: | **Версия бота:** 1.3.4\n💻 | **Кол-во ядер бота:** {psutil.cpu_count()}.\n💿 | **Использование озу:** {round(bot_ram)}\%")
        embed.add_field(name="Прочее.", value=f":earth_americas: | **Наш сайт:** https://amaranthdiscord.netlify.app/\n**📅 | Дата создания:** 29.09.22\n🐍 | **Версия Python:** 3.10\n👨‍💻 | **Разработчики:** n8#2556\n", inline=False)
        embed.set_footer(text=f"© 2022, n8#2556 · Права не защищены.", icon_url="https://cdn.discordapp.com/attachments/930784411543277619/1021417584249274489/avatar4.png")
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(info(bot))
    print(f"Ког {__name__} готов к работе.")