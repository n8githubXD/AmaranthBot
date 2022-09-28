import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class server(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot
        
    @commands.slash_command(name="server", description="Информация о сервере.")
    async def server(ctx):
        embed = disnake.Embed(title = f"{ctx.guild.name}", color = 0xFF4232)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1010870575511638018/1021054027821236285/unknown.png")
        embed.add_field(name="Владелец:", value=f"{ctx.guild.owner}", inline=True)
        embed.add_field(name="ID:", value=f"{ctx.guild.id}", inline=True)
        embed.add_field(name="Участников:", value=f"{ctx.guild.member_count}", inline=True)
        embed.add_field(name="Уровень проверки:", value=f"{ctx.guild.verification_level}", inline=True)
        embed.set_footer(text=f"Создан: {ctx.guild.created_at}")
        await ctx.send(embed=embed)
    
def setup(bot:commands.Bot):
    bot.add_cog(server(bot))
    print(f"Ког {__name__} готов к работе.")