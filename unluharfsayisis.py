
def metin(cumle,sayi=0):
    harf="aeıioöuüAEIİOÖUÜ"

    for karakter in cumle :
        if karakter in harf :
            sayi+=1
    return(sayi)   #hizalara dikkat et

cumle=input("lütfen cümlenizi giriniz : ")
print("cümlenizdeki sesli harf sayısı:{}".format(metin(cumle)))