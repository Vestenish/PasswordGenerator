import random, string

while True:
    giriş_mesajı = input("Hangi şifre türünü belirlemek istersiniz? Seçenekler : Harf , Harf_Rakam, Hepsi\n").strip().capitalize()
    if giriş_mesajı in ["Harf", "Harf_rakam", "Hepsi"]:
        break
    else:
     print("Seçeneklerden birini seçiniz.")

şifre_uzunluğu = int(input("Şifrenin uzunluğunu giriniz -->"))

Harf = string.ascii_uppercase + string.ascii_lowercase
Harf_Rakam = string.digits + string.ascii_letters
Hepsi = string.ascii_letters + string.digits + string.punctuation

if giriş_mesajı == "Harf":
    Karakter_Havuzu = Harf
elif giriş_mesajı == "Harf_rakam":
    Karakter_Havuzu = Harf_Rakam
else:
    Karakter_Havuzu = Hepsi

yeni_şifre = ''.join(random.choices(Karakter_Havuzu, k=şifre_uzunluğu))
print("Yeni şifreniz -->", yeni_şifre)