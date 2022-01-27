
import random

def isim_olustur():
    ad=["ahmet","abdullah","ali"]
    soyad=["kır","hararetli","şapşallar"]
#fonksiyon içerisinden dışarıya değer döndürürken return kullanılır
    return "{} {}" .format(random.choice(ad),random.choice(soyad))

print("-"*5)

for i in range(7):
    print(isim_olustur())
    #fonksiyon oldugu için parsntez koyacağız sonuna

print("-"*5)