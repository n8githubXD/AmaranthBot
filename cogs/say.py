import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class say(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="say", description="Сказать что либо от имени бота.")
    async def say(ctx, *, text, footer = ""):
        embed = disnake.Embed(description = text.replace('\\n', '\n'), color = 0xFF4232)
        embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.display_avatar)
        embed.set_footer(text=f"{footer}")
        await ctx.send(embed = embed)

def setup(bot:commands.Bot):
    bot.add_cog(say(bot))
    print(f"Ког {__name__} готов к работе.")