import disnake
from disnake.ext import commands
import main

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class nick(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="nick", description="Изменить ник участника.")
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: disnake.Member, *, nickname: str):
        await member.edit(nick=nickname)
        embed = disnake.Embed(title=":white_check_mark: | Ник изменен!", description=f"Новый никнейм **{member}** это - **{nickname}**!", color= 0xFF4232)
        await ctx.send(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(nick(bot))
    print(f"Ког {__name__} готов к работе.")