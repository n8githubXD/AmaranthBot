# import code
# import datetime
# from math import degrees
# from os import replace
# from unicodedata import name
# import disnake
# from disnake.ext import commands
# from memory_profiler import memory_usage
# import main
# import aiohttp
# import random
# import string


# bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/buy", status = disnake.Status.online))
# bot.remove_command("help")
# nate = bot.get_user(687959012687347751)

# class SlashCommands(commands.Cog):
#     def __init__(self, bot=commands.Bot):
#         self.bot = bot

#     @commands.slash_command(name= "help", description= "Все команды бота.")
#     async def help(self, *, ctx):
#         embed = disnake.Embed(title = "Команды.", description = "📄 | **Основные команды:**\n**info** - Информация о боте.\n**support** - Сервер поддержки.\n**server** - Информация о сервере.\n**buy** - Купить Amaranth+\n\n🎲 | **Развлечения:**\n**join** - Присоендинение бота к глс. каналу.\n**say** - Сообщение от имени бота.\n**meme** - Рандомный мем с Reddit.\n**roll** - Бросить кубик.\n**magicball** - Задать вопрос\n\n:hammer_pick: | **Модерация:**\n**slowmode** - Установить слоумод.\n**kick** - Кикнуть пользователя.\n**ban** - Забанить пользователя.\n\n:star: | **Premium:**\n**premium** - Информация о Amaranth+\n**code** - Куски кода бота.", color = 0xFF4232)
#         embed.set_footer(text="https://www.youtube.com/watch?v=LJk1HFfkgjs")
#         await ctx.send(embed=embed)
#         #AmaranthDB
#         print("AmaranthDB активирована!")
#         lines = ["1"]
#         with open(r"AmaranthDB/AmaranthDB_help_id.txt", "a") as file:
#             for  line in lines:
#                 file.write(f"On server {ctx.guild.name} the command help was activated by the user {ctx.author.send}." + '\n')
#         #AmaranthDB

#     @commands.slash_command(name= "info", description= "Информация о боте.")
#     async def info(self, ctx):
#         embed = disnake.Embed(title = "Информация.", description = f":notebook_with_decorative_cover: | **Версия бота:** 1.2.9\n:computer: | **Язык програмиирования:** Python\n :page_facing_up: | **Библиотека:** disnake 2.5.2\n\n:cd: | **Использовано памяти:**  {round(memory_usage()[0], 2)} Мб\n:floppy_disk: | **Размер бота:** {round(main.get_size() / 1024)} Кб \n\n:earth_americas: | **Наш сайт:** https://amaranthdiscord.netlify.app/\n**📅 | Дата создания:** 29.09.22", color = 0xFF4232)
#         await ctx.send(embed=embed)

#     @commands.slash_command(name="join", description="Присоендинится к голосовому каналу.")
#     async def join(ctx):
#         embed = disnake.Embed(title = "Бот присоединился к голосовому каналу!", description = f"Музыки не будет, а может будет", color = 0xFF4232)
#         await ctx.send(embed=embed)
#         channel = ctx.author.voice.channel
#         await channel.connect()

#     @commands.slash_command(name="say", description="Сказать что либо от имени бота.")
#     async def say(ctx, *, text, footer = ""):
#         embed = disnake.Embed(description = text.replace('\\n', '\n'), color = 0xFF4232)
#         embed.set_author(name = ctx.author.display_name, icon_url = ctx.author.display_avatar)
#         embed.set_footer(text=f"{footer}")
#         await ctx.send(embed = embed)

#     @commands.slash_command(name="slowmode", description="Слоумод.")
#     @commands.has_permissions(manage_channels=True)
#     async def slowmode(ctx, seconds: int):
#         await ctx.channel.edit(slowmode_delay=seconds)   
#         embed = disnake.Embed(title = "Слоумод.", description = f"Теперь медленный режим равен {seconds} сек.", color = 0xFF4232)
#         await ctx.send(embed=embed)
        
#     @commands.slash_command(name="kick", description="Кикнуть пользователя.")
#     @commands.has_permissions(kick_members=True)
#     async def kick(ctx, member: disnake.Member, *, reason=None):
#             if member.id == ctx.author.id:
#                 embed2 = disnake.Embed(title = "Вы не можете кикнуть себя!", description = f"Участник {member.mention} захотел кикнуть себя.", color = 0xFF4232)
#                 await ctx.send(embed=embed2)
#                 return
#             else:
#                 if reason==None:
#                     reason="Приична не указана."
#                 embed = disnake.Embed(title = "Кого-то кикнули.", description = f"Участник {member.mention} был кикнут по причине {reason}.", color = 0xFF4232)
#                 await ctx.send(embed=embed)
#                 await ctx.guild.kick(member)

#     @commands.slash_command(name="ban", description="Забанить пользователя.")
#     @commands.has_permissions(ban_members=True)
#     async def ban(ctx, member: disnake.Member, *, reason=None):
#             if member.id == ctx.author.id:
#                 embed2 = disnake.Embed(title = "Вы не можете забанить себя!", description = f"Участник {member.mention} захотел забанить себя.", color = 0xFF4232)
#                 await ctx.send(embed=embed2)
#                 return
#             else:
#                 if reason==None:
#                     reason="Приична не указана."
#                 embed = disnake.Embed(title = "Кого-то забанили.", description = f"Участник {member.mention} был забанен по причине {reason}.", color = 0xFF4232)
#                 await ctx.send(embed=embed)
#                 await ctx.guild.ban(member)

#     @commands.slash_command(name="support", description="Сервер поддержки.")
#     async def support(ctx):
#         embed = disnake.Embed(title = "Сервер поддержки.", description = "https://discord.gg/GzgqYTPvKj", color = 0xFF4232)
#         await ctx.send(embed=embed)

#     @commands.slash_command(name="server", description="Информация о сервере.")
#     async def server(ctx):
#         embed = disnake.Embed(title = f"{ctx.guild.name}", color = 0xFF4232)
#         embed.set_thumbnail(url=f"{ctx.guild.icon}")
#         embed.add_field(name="Владелец:", value=f"{ctx.guild.owner}", inline=True)
#         embed.add_field(name="ID:", value=f"{ctx.guild.id}", inline=True)
#         embed.add_field(name="Участников:", value=f"{ctx.guild.member_count}", inline=True)
#         embed.add_field(name="Уровень проверки:", value=f"{ctx.guild.verification_level}", inline=True)
#         embed.set_footer(text=f"Создан: {ctx.guild.created_at}")
#         await ctx.send(embed=embed)
        
#     #========================================================================================================================================

#     @commands.slash_command(name="premium", description="Премиум команда №1.")
#     async def premium(ctx):
#             if ctx.author.id == 687959012687347751 or ctx.author.id == 676137590285402117:
#                 embed2 = disnake.Embed(title = "Это премиум-команда!", description = "Содержимое данной команды, находится в ЛС пользователя, купившего Amaranth+", color = 0xFF4232)
#                 embed = disnake.Embed(title = "Привет!", description = "Если ты это видишь, то ты купил Amaranth+, большое спасибо.\n\nВот твои возможности: доступ к некоторым кускам исходного кода бота, тестовые функции, эксклюзивная информация и премиум команды!", color = 0xFFFFFF)
#                 await ctx.author.send(embed=embed)
#                 await ctx.send(embed=embed2)

#     @commands.slash_command(name="code", description="Куски кода бота.")
#     async def code(ctx):
#             if ctx.author.id == 687959012687347751 or ctx.author.id == 676137590285402117 or ctx.author.id == 692374412376145940:
#                 embed2 = disnake.Embed(title = "Это премиум-команда!", description = "Содержимое данной команды, находится в ЛС пользователя, купившего Amaranth+", color = 0xFF4232)
#                 embed = disnake.Embed(title = "Исходный код:", description = "**Команда support:**\n```py\n@commands.slash_command(name=""support"", description=""Сервер поддержки."")\nasync def support(ctx):\nembed = disnake.Embed(title = ""Сервер поддержки."", description = ""https://discord.gg/GzgqYTPvKj"", color = 0xFFFFFF)\nawait ctx.send(embed=embed)```", color = 0xFFFFFF)
#                 await ctx.author.send(embed=embed)
#                 await ctx.send(embed=embed2)

#     @commands.slash_command(name="buy", description="Покупка Amaranth+.")
#     async def buy(ctx):
#                 embed2 = disnake.Embed(title = "Купить Amaranth+", description = "Инструкция как купить Amaranth+ находится в ЛС.", color = 0xFF4232)
#                 embed = disnake.Embed(title = "Купить Amaranth+", description = "**Шаг 1**: Кинуть обмен в Steam на сумму 20+ рублей. https://steamcommunity.com/tradeoffer/new/?partner=1195228060&token=0cVhqsGb\n\n**Шаг 2**: Написать n8#2556 о своем трейде, он начислит вам Amaranth+\n\nОплата ежемесячно, можем вернуть вам деньги.", color = 0xFFFFFF)
#                 await ctx.author.send(embed=embed)
#                 await ctx.send(embed=embed2)

#     #==========================================================================================================================================
#     @commands.slash_command(name="meme", description="Мем.")
#     async def meme(ctx):
#         embed = disnake.Embed(title="", description="", color = 0xFF4232)
#         async with aiohttp.ClientSession() as cs:
#             async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
#                 res = await r.json()
#                 embed.set_image(url=res['data']['children'] [random.randint(1, 25)]['data']['url'])
#                 await ctx.send(embed=embed)

#     @commands.slash_command(name="roll", description="Бросить кубик.")
#     async def roll(ctx):
#         roll = random.randint(1, 6)
#         embed = disnake.Embed(title = f"{ctx.author.display_name} бросает кубик...", description = f"Вам выпало {roll}", color = 0xFF4232)
#         await ctx.send(embed=embed)

#     @commands.slash_command(name="magicball", description="Магический шар.")
#     async def magicball(ctx, question):
#         responses = [
#             'Да.',
#             'Нет.',
#             'Не надо.',
#             'Конечно.',
#             'Возможно.',
#             'Не уверен.',
#             'Хм.',
#             'Я не знаю.',
#         ]
#         fortune = random.choice(responses)
#         embed = disnake.Embed(title = f"{ctx.author.display_name} задал вопрос: {question}", description = f"**{fortune}**", color = 0xFF4232)
#         await ctx.send(embed=embed)

#         # embed = disnake.Embed(title = f"Понг!", description = f"Задержка бота: {round.bot.latency * 1000}ms", color = 0xFF4232)
#         # await ctx.send(embed=embed)


# def setup(bot:commands.Bot):
#     bot.add_cog(SlashCommands(bot))
#     print(f"Ког {__name__} готов к работе.")