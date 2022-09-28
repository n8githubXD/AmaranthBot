import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class avatar(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="avatar", description="Аватар участника")
    async def avatar(ctx, member: disnake.Member  = None):
        if member == None:
            member = ctx.author
        embed = disnake.Embed(color = 0xFF4232, title = f"Аватар участника - {member.name}", description = f"[Нажмите чтобы скачать аватар]({member.avatar})")
        embed.set_image(url = member.avatar)
        await ctx.send(embed = embed)

def setup(bot:commands.Bot):
    bot.add_cog(avatar(bot))
    print(f"Ког {__name__} готов к работе.")