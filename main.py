import random
keyword =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
jumlah = int(input("Mau buat berapa password yang mau dihasilkan? "))
for i in range (jumlah) :
    password += random.choice(keyword)
print (password)
