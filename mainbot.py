import discord
import random
import os
import requests
from discord.ext import commands
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
guess_game = None
artikan = None
translator = Translator()    

bahasa = [
    {"nama": "Bahasa Inggris", "kode": "en"},
    {"nama": "Bahasa Indonesia", "kode": "id"},
    {"nama": "Bahasa Jepang", "kode": "ja"},
    {"nama": "Bahasa Spanyol", "kode": "es"},
    {"nama": "Bahasa Prancis", "kode": "fr"},
    {"nama": "Bahasa Jerman", "kode": "de"},
    {"nama": "Bahasa Cina (Mandarin)", "kode": "zh"},
    {"nama": "Bahasa Arab", "kode": "ar"},
    {"nama": "Bahasa Korea", "kode": "ko"},
    {"nama": "Bahasa Rusia", "kode": "ru"},
    {"nama": "Bahasa Italia", "kode": "it"},
    {"nama": "Bahasa Belanda", "kode": "nl"},
    {"nama": "Bahasa Portugis", "kode": "pt"},
    {"nama": "Bahasa Turki", "kode": "tr"},
    {"nama": "Bahasa Thailand", "kode": "th"}
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pwd(ctx):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    pass_length = 8  # Atur panjang kata sandi sesuai keinginan Anda
    
    for _ in range(pass_length):
        password += random.choice(elements)
        
    await ctx.send("Password :")
    await ctx.send(password)

@bot.command()
async def guess(ctx):
    global guess_game
    guess_game = random.randint(1, 15)
    await ctx.send("Tebak angka 1 sampai 15, jawab dengan $answer")

@bot.command()
async def answer(ctx, number):
    if guess_game == int(number):
        await ctx.send("Selamat Anda benar!")
    else:
        await ctx.send("Jawaban salah, silahkan coba lagi.")

@bot.command()
async def translate(ctx):
    message = "Kode Bahasa:\n"
    for bahasa_item in bahasa:
        message += f"{bahasa_item['nama']}: {bahasa_item['kode']}\n"
    await ctx.send(message)
    
    await ctx.send("Cara untuk translate")
    await ctx.send("$ask [kode bahasa asal] [kode bahasa tujuan] [teks yang akan diterjemahkan]")

@bot.command()
async def ask(ctx, lang_from, lang_to, *, text):
    try:
        # Terjemahkan teks dari bahasa asal ke bahasa tujuan
        translation = translator.translate(text, src=lang_from, dest=lang_to)
        
        # Kirim hasil terjemahan ke server
        await ctx.send(f"**{lang_from}**:\n{text}\n\n**{lang_to}**:\n{translation.text}")
    except Exception as e:
        await ctx.send(f"Terjadi kesalahan saat melakukan terjemahan: {e}")

@bot.command()
async def meme(ctx):
    daftar_gambar = os.listdir('images')
    gambar = random.choice(daftar_gambar)
    with open(f'images/{gambar}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
bot.run('MASUKAN TOKEN BOT KAMU DISINI!')
