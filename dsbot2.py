from discord.ext import commands
from numbers import Integral
import discord
import math
import random

token = "MTA2Mjg0NDIzMTc0MTM2MjE4Ng.GUbpV9.qMgj7Fe-7UZqaoo4723LLROOs7bkTKzSrPjpH8"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def suma(ctx, num1: str, num2: str):
    try:
        num1 = int(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except ValueError:
        num2 = float(num2)
    resultado = num1 + num2
    if isinstance(num1, Integral) and isinstance(num2, Integral):
        await ctx.send(f"{int(num1)} + {int(num2)} = {int(resultado)}")
    else:
        await ctx.send(f"{num1} + {num2} = {resultado}")
   
@bot.command()
async def resta(ctx, num1: str, num2: str):
    try:
        num1 = int(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except ValueError:
        num2 = float(num2)
    resultado = num1 - num2
    if isinstance(num1, Integral) and isinstance(num2, Integral):
        await ctx.send(f"{int(num1)} - {int(num2)} = {int(resultado)}")
    else:
        await ctx.send(f"{num1} - {num2} = {resultado}")
        
@bot.command()
async def multiplicacion(ctx, num1: str, num2: str):
    try:
        num1 = int(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = int(num2)
    except ValueError:
        num2 = float(num2)
    resultado = num1 * num2
    if isinstance(num1, Integral) and isinstance(num2, Integral):
        await ctx.send(f"{int(num1)} x {int(num2)} = {int(resultado)}")
    else:
        await ctx.send(f"{num1} x {num2} = {resultado}")
        
@bot.command()
async def division(ctx, num1: str, num2: str):
    try:
        num1 = float(num1)
    except ValueError:
        num1 = float(num1)
    try:
        num2 = float(num2)
    except ValueError:
        num2 = float(num2)
    if num2 != 0:
        resultado = num1 / num2
        if isinstance(num1, Integral) and isinstance(num2, Integral) and resultado.is_integer():
            await ctx.send(f"{float(num1)} / {float(num2)} = {int(resultado)}")
        else:
            await ctx.send(f"{num1} / {num2} = {resultado}")
    else:
        await ctx.send("No se puede dividir para 0")
        
@bot.command()
async def raiz(ctx, num: str):
    try:
        num = float(num)
    except ValueError:
        num = float(num)
    resultado = math.sqrt(num)
    if isinstance(num, Integral) and resultado.is_integer():
        await ctx.send(f"La raíz cuadrada de {int(num)} es {int(resultado)}")
    else:
        await ctx.send(f"La raíz cuadrada de {num} es {resultado}")

@bot.command()
async def hola(ctx):
    respuestas = ["¡Hola, {}! ¿Cómo estás?", "¡Saludos, {}! ¿Cómo te va?", "¡Hola de nuevo, {}! ¿Qué hay de nuevo?", "¡Hola, {}! ¿Qué tal tu día?", "¡Hola, {}! ¿Programamos algo hoy?"]
    respuesta_elegida = random.choice(respuestas)
    await ctx.send(respuesta_elegida.format(ctx.author.mention))

@bot.command()
async def elimina(ctx, cantidad: int):
    deleted_messages = []
    async for message in ctx.channel.history(limit=cantidad):
        deleted_messages.append(message.content)
        await message.delete()
    await ctx.send(f"Los siguiente mensajes fueron eliminados: {deleted_messages}")    
bot.run(token)
