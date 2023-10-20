import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def cara_mengurangi_sampah_dirumah(ctx):
    await ctx.send('''
- Memisahkan Sampah Sesuai Jenisnya
- Melakukan Zero Waste
- Membuat Pupuk dari Sampah Organik
- Membersihkan Tempat Sampah Setiap Hari
- Melakukan Daur Ulang Pada Sampah Anorganik
                   ''')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def coy(ctx, count_coy = 5):
    await ctx.send("coy" * count_coy)

@bot.command()
async def mem(ctx):
    with open('M2L1/Slide4.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")
