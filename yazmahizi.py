
import time
import datetime

print("3")
time.sleep(0.1)

print("2")
time.sleep(0.1)
print("1")
time.sleep(0.1)

zaman=datetime.datetime.now()

metin=input("metin giriniz : ")

zaman2=datetime.datetime.now()

yazim_hizi=zaman2-zaman
saniye=round(yazim_hizi.total_seconds(),2)
zaman3=round(len(metin)/saniye,  1)

print("toplam zaman  : {}".format(saniye))
print("{} harf başina geçen saniye".format(zaman3))