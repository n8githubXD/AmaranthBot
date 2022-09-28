import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class faq(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="faq", description="Ответы на вопросы.")
    async def faq(ctx):
        embed = disnake.Embed(title = "❓ | FAQ.", color = 0xFF4232)
        embed.add_field(name="Почему бот не отвечает на команды?", value=f"Возможно из-за того что бот выключен, у вас нет прав на выполнение команды, команда сломана, вы не правильно её используете или бот перезагружается.")
        embed.add_field(name="Почему команда `/list`, а не `/help`", value=f"Я не знаю.", inline=False)
        embed.add_field(name="У вас есть сервер поддержки?", value=f"`/support`.", inline=False)
        embed.add_field(name="Почему бот выключен?", value=f"Хостинг, либо мы работаем.", inline=False)
        embed.set_footer(text=f"© 2022, n8#2556 · Права не защищены.", icon_url="https://cdn.discordapp.com/attachments/930784411543277619/1021417584249274489/avatar4.png")
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(faq(bot))
    print(f"Ког {__name__} готов к работе.")