import numbers
sonuc =0
x=-1

for i in range(0,99):
    print("çıkmak için 0 a basın")
    sayi=int(input("sayı giriniz : "))

    x+=1
    if sayi==0:
        break
print("sayı adedi {} ".format(x))


islem=int(input("hangi işlemi yapmak istiyorsunuz \n toplama 1\nçarpma 2\n\nçıkarma 3\nbölme 4\n"))

if (islem==1) :

    for sayi in i :
        sonuc+=sayi


elif (islem ==2) :
     for x in i :
        sonuc*=sayi
elif (islem==3):
     for x in i :
        sonuc-=sayi
else :
     for x in i :
        sonuc/=sayi
        break

print("sonuc : {}".format(sonuc))