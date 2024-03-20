def harf_mi(karakter):
    "Karakterin Türkçe bir harf olup olmadığını kontrol eder."
    turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyzçğıöşü"
    return karakter.lower() in turk_alfabesi

def kucuk_harfe_cevir(harf):
    "Verilen harfi küçük harfe çevirir."
    return harf.lower()

def frekans_ve_yuzde_hesapla(metin):
    "Metindeki harflerin frekansını ve yüzde oranını hesaplar."
    metin = ''.join(kucuk_harfe_cevir(harf) for harf in metin if harf_mi(harf))
    frekans = {}
    toplam_harfler = len(metin)

    for harf in metin:
        frekans[harf] = frekans.get(harf, 0) + 1

    for harf in frekans:
        frekans[harf] = (frekans[harf], (frekans[harf] / toplam_harfler) * 100)

    return frekans

def kullanici_bilgileri_getir():
    ad = "Semih Arda Güleç"
    okul_numarasi = "211213005"
    varsayilan_mesaj = "Yaşanmadan geçen yıllar utansın"
    return ad, okul_numarasi, varsayilan_mesaj
