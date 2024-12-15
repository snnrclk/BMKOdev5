# Bankamatik uygulaması
# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# Çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.


kartSifresi = "1957"
bakiye = 1000
denemeHakki = 3
ekHesap = 1500 
print("X Bankasına Hoş Geldiniz ")
kartIslemDurumu = True
islemDurumu = True

while islemDurumu:
    girilenSifre = input("Kart Şifrenizi Giriniz: ")
    if girilenSifre != kartSifresi:
        print("Yanlış şifre girdiniz. Lütfen Tekrar deneyiniz.")
        denemeHakki -=1
        print(denemeHakki, "deneme hakkınız kaldı.")
        if denemeHakki == 0:
            print("Kartınız bloklandı. Lütfen banka ile görüşünüz.")
            islemDurumu = False

    else:
        print("Giriş yapıldı.")
        print("""
        Yapılacak İşlemi Seçiniz
        ---------------------------
        1- Para Çekme
        2- Para Yatırma
        3- Bakiye Sorgulama
        4- Çıkış
        ---------------------------
        """)
        while kartIslemDurumu: 
            print("---------------------------------")
            islemNo = input("İşlem numarasını giriniz: ")
            if islemNo == "1":
                cekilecekMiktar = int(input("Çekilecek Miktar: "))
                if cekilecekMiktar > bakiye:
                    print("Yetersiz bakiye. ")
                    toplam = bakiye + ekHesap
                    if (toplam >= cekilecekMiktar):
                        ekHesapKullanimi = input('Ek hesap kullanılsın mı? (Evet/Hayir)')
                        if ekHesapKullanimi == 'Evet':
                            print('Paranızı alabilirsiniz. ')
                    else:
                        print('')
                        

                else:
                    bakiye -= cekilecekMiktar
                    print("İşlem gerçekleşti.")
            
                    

            elif islemNo == "2":
                yatirilacakMiktar = int(input("Yatırılacak Miktar: "))
                bakiye += yatirilacakMiktar
                print("İşlem gerçekleşti. ")

            elif islemNo == "3":
                print("Toplam Bakiye: ",bakiye,"₺") # Alt gr + T

            elif islemNo == "4": 
                print("Çıkış yapıldı. ")
                print("Lütfen giriş yapınız. ")
                break
    break
                
                
