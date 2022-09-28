import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class list(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot
        
    @commands.slash_command(name= "list", description= "Все команды бота.")
    async def list(self, *, ctx):
        embed = disnake.Embed(title = "Команды.", color = 0xFF4232)
        embed.add_field(name="👑 | **Для разработчиков:**", value=f"`shutdown`.", inline=False)
        embed.add_field(name="📄 | **Основные команды:**", value=f"`info` `support` `server` `buy` `ping` `faq`.", inline=False)
        embed.add_field(name="🎲 | **Развлечения:**", value=f"`say` `meme` `roll` `magicball`.", inline=False)
        embed.add_field(name=":hammer_pick: | **Модерация:**", value=f"`slowmode` `kick` `ban` `nick`.", inline=False)
        embed.add_field(name="⌨️ | **Прочее:**", value=f"`avatar`.", inline=False)
        embed.add_field(name=":star: | **Premium:**", value=f"`premium` `code`.", inline=False)
        embed.set_footer(text="https://www.youtube.com/watch?v=LJk1HFfkgjs")
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(list(bot))
    print(f"Ког {__name__} готов к работе.")