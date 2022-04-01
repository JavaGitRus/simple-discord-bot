import discord
from discord.ext import commands

TOKEN = 'ТОКЕН'
bot = commands.Bot(command_prefix='/')
client = commands.Bot( command_prefix="/" )


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

bot.run(TOKEN)

#Где ТОКЕН нужно получить секретный токен.
#Инструкция : https://habr.com/ru/post/511454/
#Сам бот очень простой пишем в чат /test Сообщение