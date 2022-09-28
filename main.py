import disnake
from disnake.ext import commands, tasks
from threading import Thread
from memory_profiler import memory_usage
import asyncio

print("░█████╗░███╗░░░███╗░█████╗░██████╗░░█████╗░███╗░░██╗████████╗██╗░░██╗\n██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██║░░██║\n███████║██╔████╔██║███████║██████╔╝███████║██╔██╗██║░░░██║░░░███████║\n██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══██║\n██║░░██║██║░╚═╝░██║██║░░██║██║░░██║██║░░██║██║░╚███║░░░██║░░░██║░░██║\n╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝")

bot = commands.Bot(command_prefix="+", intents= disnake.Intents.all(), activity= disnake.Game("/list", status = disnake.Status.online))

@bot.event
async def on_ready() -> None:
    status_task.start()

@tasks.loop()
async def status_task() -> None:
    await bot.change_presence(activity= disnake.Game("/list", status = disnake.Status.online))
    await asyncio.sleep(12)
    await bot.change_presence(activity= disnake.Game("/faq", status = disnake.Status.online))
    await asyncio.sleep(12)
    await bot.change_presence(activity= disnake.Game("Hello!", status = disnake.Status.online))
    await asyncio.sleep(12)
    await bot.change_presence(activity= disnake.Game("1.3.4!", status = disnake.Status.online))

bot.load_extension("cogs.ban")
bot.load_extension("cogs.buy")
bot.load_extension("cogs.code")
bot.load_extension("cogs.list")
bot.load_extension("cogs.info")
bot.load_extension("cogs.kick")
bot.load_extension("cogs.meme")
bot.load_extension("cogs.premium")
bot.load_extension("cogs.roll")
bot.load_extension("cogs.say")
bot.load_extension("cogs.server")
bot.load_extension("cogs.slowmode")
bot.load_extension("cogs.support")
bot.load_extension("cogs.events")
bot.load_extension("cogs.magicball")
bot.load_extension("cogs.ping")
bot.load_extension("cogs.faq")
bot.load_extension("cogs.avatar")
bot.load_extension("cogs.nick")
bot.load_extension("cogs.shutdown")


bot.run()