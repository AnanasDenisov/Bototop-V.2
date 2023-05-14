import discord
from bot_logic import *

intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$orel/reshka'):
        import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

#Место с подкидыванием кубика
def cube():
    cube = random.randint(1, 6)
    if cube == 1:
        print(cube)

    if cube == 2:
        print(cube)

    if cube == 3:
        print(cube)

    if cube == 4:
        print(cube)

    if cube == 5:
        print(cube)

    if cube == 6:
        print(cube)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"
        
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Я не понимаю такую команду!")

client.run(settings["TOKEN"])
