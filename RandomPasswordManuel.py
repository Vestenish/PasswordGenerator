import random

giriş_mesajı = (input("Lütfen karıştırmak istediğiniz şifryi giriniz --->"))

şifre = giriş_mesajı
list(şifre)
yeni_şifre = list(şifre)


random.shuffle(yeni_şifre)
print("".join(yeni_şifre))
