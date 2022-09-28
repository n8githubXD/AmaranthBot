import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class events(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Бот включен")

    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        embed = disnake.Embed(title = "👋 | Привет, спасибо что добавил меня на сервер!", description = f"・Мой префикс -  \"/\".\n・Для того чтобы посмотреть список команд используйте **list**.", color = 0xFF4232)
        embed.set_footer(text="Хорошего использования!")
        await ctx.owner.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(events(bot))
    print(f"Ког {__name__} готов к работе.")