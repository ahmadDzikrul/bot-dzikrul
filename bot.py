import discord
from bot_logic import gen_pass

# uji coba edit file di github
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')
    print(gen_pass(10))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTE1NTA2MzkxMjY3NzUxOTQ2MA.G_mBmy.82Zzx8TRcvXY8ZJF3mX1dHMMyava9Npvv3oFWk")
