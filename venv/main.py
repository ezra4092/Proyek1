from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def main():
    return '<h2>Beberapa fakta mengenai kecanduan teknologi <a href="/random_fact">Klik disini!</a></h2>  <h2>Ayo buat kata sandi! <a href="/pass">Klik disini</a></h2>'
    

@app.route("/random_fact")
def random_fact() :
    facts_list = [
        'Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati.',
        'Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka.',
        'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
        'Kecanduan teknologi dapat mempengaruhi pola tidur, menyebabkan gangguan tidur seperti insomnia karena terlalu banyak waktu dihabiskan di depan layar.',
        'Kecanduan teknologi dapat merusak hubungan interpersonal karena kurangnya perhatian terhadap orang-orang di sekitar mereka.'
    ]
    return f'<p>{random.choice(facts_list)}</p>'
    
@app.route("/pass")
def password () :
    keyword =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range (8) :
        password += random.choice(keyword)
    return password

app.run(debug=True)
