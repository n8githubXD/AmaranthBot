import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class ban(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="ban", description="Забанить пользователя.")
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: disnake.Member, *, reason=None):
            if member.id == ctx.author.id:
                embed2 = disnake.Embed(title = "❌ | Вы не можете забанить себя!", description = f"Участник {member.mention} захотел забанить себя.", color = 0xFF4232)
                await ctx.send(embed=embed2)
                return
            else:
                if reason==None:
                    reason="Приична не указана."
                embed = disnake.Embed(title = "🔨 | Кого-то забанили.", description = f"Участник {member.mention} был забанен по причине {reason}.", color = 0xFF4232)
                await ctx.send(embed=embed)
                await ctx.guild.ban(member)

def setup(bot:commands.Bot):
    bot.add_cog(ban(bot))
    print(f"Ког {__name__} готов к работе.")