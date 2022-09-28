import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

class kick(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.slash_command(name="kick", description="Кикнуть пользователя.")
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: disnake.Member, *, reason=None):
            if member.id == ctx.author.id:
                embed2 = disnake.Embed(title = "Вы не можете кикнуть себя!", description = f"Участник {member.mention} захотел кикнуть себя.", color = 0xFF4232)
                await ctx.send(embed=embed2)
                return
            else:
                if reason==None:
                    reason="Приична не указана."
                embed = disnake.Embed(title = "Кого-то кикнули.", description = f"Участник {member.mention} был кикнут по причине {reason}.", color = 0xFF4232)
                await ctx.send(embed=embed)
                await ctx.guild.kick(member)

def setup(bot:commands.Bot):
    bot.add_cog(kick(bot))
    print(f"Ког {__name__} готов к работе.")