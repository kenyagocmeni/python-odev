import metin_isleme

def main():
    while True:
        print("1. Metin gir")
        print("2. Kullanıcı bilgilerini gör")
        print("3. Çıkış")
        secim = input("Seçiminizi yapın (1/2/3): ")

        if secim == '1':
            kullanici_girisi = input("Bir metin girin: ")
            frekanslar = metin_isleme.frekans_ve_yuzde_hesapla(kullanici_girisi)
            for harf, (frekans, yuzde) in frekanslar.items():
                print(f"'{harf}': {frekans} kullanım ({yuzde:.2f}%)")
        elif secim == '2':
            ad, okul_numarasi, varsayilan_mesaj = metin_isleme.kullanici_bilgileri_getir()
            print(ad)
            print(okul_numarasi)
            print(varsayilan_mesaj)
        elif secim == '3':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 tuşlarından birini seçin.")

if __name__ == "__main__":
    main()
