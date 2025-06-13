

personelsozluk = {}
personelliste = []
sayac = 0
kontrol = 0
with open("stafflist.txt", "r") as dosya:  # programa başlamadan önce dosyayı okuyup bilgileri listeye atar
    everi = dosya.readlines()
    j = 0
    for i in everi:
        liste = i[:-1].split("-")  # listeyi indislerine ayırıp personellistesine aktarır
        personelliste.append({})
        personelliste[j]["isim"] = liste[0]
        personelliste[j]["soyisim"] = liste[1]
        personelliste[j]["yaş"] = liste[2]
        personelliste[j]["pozisyon"] = liste[3]
        personelliste[j]["maaş"] = liste[4]
        personelliste[j]["izindurum"] = liste[5]
        j += 1
id = len(personelliste)


# işlemlerin yapıldığı anamenu fonksiyonu
def anamenu():
    print("-----ŞİRKET OTOMASYONU-----")
    print("1-Personel ekleme")
    print("2-Personel silme")
    print("3-Personel güncelleme")
    print("4-Personel arama")
    print("5-Personel maaş hesabı")
    print("6-Personel izin")
    print("7-Çıkış")
    secim = input("\nbir secim yapınız:")
    if secim == "7":
        print("program kapatılıyor...")
        exit()
    elif secim == "1":
        personelekle()
    elif secim == "2":
        personelsilme()
    elif secim == "3":
        personelguncelle()
    elif secim == "4":
        personelarama()
    elif secim == "5":
        maashesap()
    elif secim == "6":
        personelizin()
    else:
        print("hatalı seçim yaptınız tekrar deneyin...")
        anamenu()


# ekleme fonksiyonu
def personelekle():
    global sayac
    global personelliste
    global id
    id += 1
    sayac += 1
    isim = input("personel isim giriniz:").lower()
    soyisim = input("personel soyisim giriniz:").lower()
    yas = input("yas giriniz:")
    pozisyon = input("personel işini giriniz:").lower()
    try:
        maas = int(input("maas giriniz:"))
    except ValueError:
        print("lütfen bir sayi giriniz.tekrar deneyin!")
        personelekle()
    try:  # bilgileri sözlüğe atar sonra sözlüğü listeye atar
        personelsozluk = {"isim": isim, "soyisim": soyisim, "yaş": yas, "pozisyon": pozisyon, "maaş": str(maas),
                          "izindurum": "calisiyor"}
        personelliste.append(personelsozluk)
        print("personel başarıyla eklendi!")
    except UnboundLocalError:
        return 0
    try:
        with open("stafflist.txt", "a") as dosya:
            dosya.write(
                personelliste[id]["isim"] + "-" + personelliste[id]["soyisim"] + "-" + personelliste[id]["yaş"] + "-" +
                personelliste[id]["pozisyon"] + "-" + str(personelliste[id]["maaş"]) + "-" + personelliste[id][
                    "izindurum"] + "\n")
        anamenu()
    except IndexError:
        id -= 1
        with open("stafflist.txt", "a") as dosya:
            dosya.write(
                personelliste[id]["isim"] + "-" + personelliste[id]["soyisim"] + "-" + personelliste[id]["yaş"] + "-" +
                personelliste[id]["pozisyon"] + "-" + str(personelliste[id]["maaş"]) + "-" + personelliste[id][
                    "izindurum"] + "\n")
        anamenu()


# silme fonksiyonu
def personelsilme():
    global kontrol
    kontrol = 0
    silmekontrol = 0
    id = 0
    s_isim = input("silinecek personelin ismini giriniz:")  # girilen isme göre silme işlemi yapılır
    while True:
        if len(personelliste) == kontrol:
            break
        if personelliste[kontrol]["isim"] == s_isim.lower():
            personelliste.pop(kontrol)
            print("personel silindi!")
            silmekontrol = 0
            break
        else:
            kontrol += 1
            silmekontrol = 1
    if silmekontrol == 1:
        print("personel bulunamadı tekrar deneyin...")
        personelsilme()
    with open("stafflist.txt",
              "w") as dosya:  # silme işlemi yapıldıktan sonra bilgileri en baştan dosyaya yazdırır
        while True:
            if len(personelliste) == id:
                break
            dosya.write(
                personelliste[id]["isim"] + "-" + personelliste[id]["soyisim"] + "-" + personelliste[id]["yaş"] + "-" +
                personelliste[id]["pozisyon"] + "-" + str(personelliste[id]["maaş"]) + "-" + personelliste[id][
                    "izindurum"] + "\n")
            id += 1
    anamenu()


# güncelleme fonksiyonu
def personelguncelle():
    global kontrol
    kontrol = 0
    gkontrol = 0
    id = 0
    g_isim = input("güncellenecek personelin ismini giriniz:")  # isme göre güncellencek kişiyi belirler
    while True:
        if len(personelliste) == kontrol:
            break
        if personelliste[kontrol]["isim"] == g_isim.lower():
            yeni_isim = input("yeni isim giriniz:").lower()
            yeni_soyisim = input("yeni soyisim giriniz:").lower()
            yeni_yas = input("yeni yaş giriniz:")
            yeni_pozisyon = input("yeni pozisyon giriniz:").lower()
            try:
                yeni_maas = int(input("yeni maaş giriniz:"))
            except ValueError:
                print("lütfen bir sayı giriniz.tekrar deneyiniz...")
                personelguncelle()
            personelliste[kontrol]["isim"] = yeni_isim
            personelliste[kontrol]["soyisim"] = yeni_soyisim
            personelliste[kontrol]["yaş"] = yeni_yas
            personelliste[kontrol]["pozisyon"] = yeni_pozisyon
            personelliste[kontrol]["maaş"] = yeni_maas
            print("personel guncellendi!")
            gkontrol = 0
            break
        else:
            kontrol += 1
            gkontrol = 1
    if gkontrol == 1:
        print("böyle bir personel bulunamamıştır tekrar deneyiniz...")
        personelguncelle()
    try:
        with open("stafflist.txt",
                  "w") as dosya:  # güncelleme işlemi bittikten sonra bilgileri en baştan dosyaya yazar
            while True:
                if len(personelliste) == id:
                    break
                dosya.write(personelliste[id]["isim"] + "-" + personelliste[id]["soyisim"] + "-" + personelliste[id][
                    "yaş"] + "-" + personelliste[id]["pozisyon"] + "-" + str(personelliste[id]["maaş"]) + "-" +
                            personelliste[id]["izindurum"] + "\n")
                id += 1
    except UnboundLocalError:
        anamenu()
    anamenu()


# arama fonksiyonu
def personelarama():
    a_isim = input("aranan personelin ismini giriniz:")  # personeli ismine göre bulur ve ekrana yazdırır
    global kontrol
    kontrol = 0
    aramakontrol = 0
    while True:
        if len(personelliste) == kontrol:
            break
        if personelliste[kontrol]["isim"] == a_isim.lower():
            print("personel bulundu")
            print("isim={}\nsoyisim={}\nyaş={}\npozisyon={}\nmaaşı={}\nizindurumu={}".format(
                personelliste[kontrol]["isim"], personelliste[kontrol]["soyisim"], personelliste[kontrol]["yaş"],
                personelliste[kontrol]["pozisyon"], personelliste[kontrol]["maaş"],
                personelliste[kontrol]["izindurum"]))
            aramakontrol = 0
            break
        else:
            kontrol += 1
            aramakontrol = 1
    if aramakontrol == 1:
        print("personel bulunamadı tekrar deneyin...")
        personelarama()
    anamenu()


# maaş hesaplama fonksiyonu
def maashesap():
    global kontrol
    kontrol = 0
    gkontrol = 0
    id = 0
    h_isim = input("maaşı hesaplanacak personelin ismini giriniz:")  # isime göre personeli bulur
    while True:
        if len(personelliste) == kontrol:
            break
        if personelliste[kontrol]["isim"] == h_isim.lower():
            print(
                "maaşınız çocuk sayısına(%10) ve mesai saatine göre zamlanmaktadır(%3)")  # maaşı cocuk sayısına ve mesai saatine göre zamlı olarak verilir
            maas = input("maaşınızı giriniz:")
            if maas != str(personelliste[kontrol]["maaş"]):
                print("personelin maaşı girilen değerle eşleşmedi.tekrar deneyiniz...")
                maashesap()
            csayisi = int(input("cocuk sayısını giriniz:"))
            msaati = int(input("günlük mesai saatinizi giriniz:"))
            yenimaas = csayisi * (int(maas) * 0.1) + msaati * (int(maas) * 0.03) + int(maas)
            yenimaas = int(yenimaas)
            print("maaşınız hesaplandı!")
            personelliste[kontrol]["maaş"] = yenimaas
            gkontrol = 0
            break
        else:
            kontrol += 1
            gkontrol = 1
    if gkontrol == 1:
        print("bu isimde kayıtlı bir personel yok tekrar deneyiniz...")
        maashesap()
    try:
        with open("stafflist.txt",
                  "w") as dosya:  # maaş hesaplandıktan sonra bilgiler dosyaya en baştan yazdırılır
            while True:
                if len(personelliste) == id:
                    break
                dosya.write(personelliste[id]["isim"] + "-" + personelliste[id]["soyisim"] + "-" + personelliste[id][
                    "yaş"] + "-" + personelliste[id]["pozisyon"] + "-" + str(personelliste[id]["maaş"]) + "-" +
                            personelliste[id]["izindurum"] + "\n")
                id += 1
    except UnboundLocalError:
        anamenu()
    anamenu()


# izin alma fonksiyonu
def personelizin():
    global kontrol
    kontrol = 0
    gkontrol = 0
    id = 0
    i_isim = input("izin alacak personelin ismini giriniz:")  # isme göre izin alacak personel belirlenir

    def izinfonk(i_isim):
        id = 0
        global kontrol
        while True:
            if len(personelliste) == kontrol:
                break
            if personelliste[kontrol]["isim"] == i_isim.lower():
                print("30 gün izin hakkınız bulunmaktadır!")
                izinsayisi = int(input("kaç gün izin almak istersiniz:"))
                if int(izinsayisi) > 30:
                    print(
                        "alınabilecek izin sayısını aştınız tekrar deneyin!")  # verilen izin hakkını aşmadığı kontrol edilir
                    izinfonk(i_isim)
                else:
                    print("izin başarıyla alınmıştır!")
                    personelliste[kontrol]["izindurum"] = str(izinsayisi) + " gun izinli"
                gkontrol = 0
                break
            else:
                kontrol += 1
                gkontrol = 1
        if gkontrol == 1:
            print("bu isimde kayıtlı bir personel yok tekrar deneyiniz...")
            personelizin()
        try:
            with open("stafflist.txt", "w") as dosya:  # izin alındıktan sonra dosyaya yazdırır
                while True:
                    if len(personelliste) == id:
                        break
                    dosya.write(
                        personelliste[id]["isim"] + "-" + personelliste[id]["soyisim"] + "-" + personelliste[id][
                            "yaş"] + "-" + personelliste[id]["pozisyon"] + "-" + str(personelliste[id]["maaş"]) + "-" +
                        personelliste[id]["izindurum"] + "\n")
                    id += 1
        except UnboundLocalError:
            anamenu()

    izinfonk(i_isim)
    anamenu()


anamenu()
