import disnake
from disnake.ext import commands
import random

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class magicball(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="magicball", description="Магический шар.")
    async def magicball(ctx, question):
         responses = [
             'Да.',
             'Нет.',
             'Не надо.',
             'Конечно.',
             'Возможно.',
             'Не уверен.',
             'Хм.',
             'Я не знаю.',
         ]
         fortune = random.choice(responses)
         embed = disnake.Embed(title = f"🤔 | {ctx.author.display_name} задал вопрос: {question}", description = f"**{fortune}**", color = 0xFF4232)
         await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(magicball(bot))
    print(f"Ког {__name__} готов к работе.")