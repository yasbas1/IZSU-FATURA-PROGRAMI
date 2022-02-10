CTV=0.39
KATI_ATIK_UCRETI=13
KATI_ATIK_BERTARAF_UCRETI=2.54
baska_abone="e"
genel_fatura=0
konut_sayisi=0
isyeri_sayisi=0
resmi_daire_sayisi=0
organize_sanayi_sayisi=0
tarim_sayisi=0
konut_su=0 #Konutların harcadığı toplam su miktarını bulmak için kulllanılır.
isyeri_su=0
resmi_daire_su=0
organize_sanayi_su=0
tarim_su=0
toplam_hane_sayisi=0
kademe1_sayisi=0
kademe2_sayisi=0
kademe3_sayisi=0
aylik_kadame1_su_toplam=0 #En son istatistiklerdeki aylık değerleri 30 gün üzerinden bulmak içindir.
aylik_kadame2_su_toplam=0
aylik_kadame3_su_toplam=0
tarim50_sayisi=0
genel_ozel_durum_kisi_sayisi=0
genel_engelli_sayisi=0
aylik_konut_tuketim_toplam=0
aylik_konut_tuketim_ucreti_toplam=0
aylik_isyeri_tuketim_toplam=0
aylik_isyeri_tuketim_ucreti_toplam=0
aylik_resmi_tuketim_ucreti_toplam=0
aylik_resmi_tuketim_toplam=0
aylik_organize_tuketim_ucreti_toplam=0
aylik_organize_tuketim_toplam=0
aylik_tarim_tuketim_ucreti_toplam=0
aylik_tarim_tuketim_toplam=0
aylik_tuketim=0
aylik_su_tuketim=0
genel_ctv=0
genel_kta=0
genel_ktba=0
genel_kdv=0
max_resmi_daire=-1
ton100_ve_tl500=0
konut_toplam_su_tuketim_ucreti=0
konut_toplam_atik_su_ucreti=0
isyeri_toplam_su_tuketim_ucreti = 0
isyeri_toplam_atik_su_ucreti = 0
resmi_daire_toplam_su_tuketim_ucreti=0
organize_sanayi_toplam_su_tuketim_ucreti=0
tarim_toplam_su_tuketim_ucreti=0
resmi_daire_toplam_atik_su_ucreti=0
organize_sanayi_toplam_atik_su_ucreti=0
tarim_toplam_atik_su_ucreti=0
while baska_abone=="e" or baska_abone=="E" :
    abone_no=int(input("Abone no giriniz:"))
    abone_kodu=int(input("Abone kodunu giriniz:"))
    while abone_kodu<1 or abone_kodu>5 :
        abone_kodu=int(input("Abone kodu 1 ile 5 arasında olmalıdır. Tekrar giriniz:"))
    onceki_sayac=int(input("Önceki sayaç değerini giriniz:"))
    while onceki_sayac<0 :
        onceki_sayac=int(input("Önceki sayaç negatif olamaz.Tekrar giriniz:"))
    simdiki_sayac=int(input("Şimdiki sayaç değerini giriniz:"))
    while simdiki_sayac<onceki_sayac:
        simdiki_sayac=int(input("Şimdiki sayaç öncekinden küçük olamaz. Tekrar giriniz:"))
    okuma_gun_sayisi=int(input("Faturanın okunma gün sayısını giriniz: "))
    while okuma_gun_sayisi<0 :
        okuma_gun_sayisi=int(input("Gün sayısı negatif olamaz. Tekrar giriniz:"))
    su_tuketim=0 #Su tüketim miktarına karşılık gelen su tüketim ücretidir.
    atik_su=0 #Su tüketim miktarına karşılık gelen atık su ücretidir.
    fatura=0
    kdv_tutari=0
    tuketim=simdiki_sayac-onceki_sayac #Su tüketim miktarıdır.
    hane_sayisi=0
    oran =30/okuma_gun_sayisi
    if abone_kodu==1:
        konut_su+=tuketim
        konut_sayisi+=1
        hane_sayisi = int(input("Hane sayısını giriniz: "))
        while hane_sayisi<1 :
            hane_sayisi=int(input("Hane sayısı 1'den küçük olamaz. Tekrar giriniz: "))
        toplam_hane_sayisi+=hane_sayisi
        if hane_sayisi == 1:
            if tuketim <= 13:
                kademe1_sayisi+=1
                su_tuketim = (tuketim * 2.89)
                atik_su = (tuketim * 1.44)
                aylik_kadame1_su = (30 * tuketim) / okuma_gun_sayisi
                aylik_kadame1_su_toplam += aylik_kadame1_su
            if 14 <= tuketim <= 20:
                kademe2_sayisi+=1
                su_tuketim = (13 / oran) * 2.89 + (tuketim - (13 / oran)) * 3.13
                atik_su = (13 / oran) * 1.44 + (tuketim - (13 / oran)) * 1.56
                aylik_kadame2_su = (30 * tuketim) / okuma_gun_sayisi
                aylik_kadame2_su_toplam += aylik_kadame2_su
            if tuketim >= 21:
                kademe3_sayisi+=1
                su_tuketim = (13 / oran) * 2.89 + (7 * 3.13) + (tuketim-(20/ oran)) * 6.43
                atik_su = (13 / oran) * 1.44 + (7 * 1.56) + (tuketim-(20 / oran))* 3.22
                aylik_kadame3_su = (30 * tuketim) / okuma_gun_sayisi
                aylik_kadame3_su_toplam += aylik_kadame3_su
            indirim_durumu = input("İndirim durumunuzu giriniz(Y,y,Ş,ş,G,g,S,s,E,e): ")
            while indirim_durumu not in ["Y","y","Ş", "ş","G","g","S","s","E","e"]:
                indirim_durumu=input("Böyle bir indirim durumu yoktur. Verilen değerlerden birini giriniz:")
            if indirim_durumu in ["Ş", "ş", "G", "g", "S", "s"]:
                genel_ozel_durum_kisi_sayisi+=1
                su_tuketim = su_tuketim / 2
                atik_su = atik_su / 2
            if indirim_durumu in ["E", "e"] and tuketim <= 20:
                genel_engelli_sayisi+=1
                su_tuketim = su_tuketim / 2
                atik_su = atik_su / 2
        else:
            ozel_durum_kisi_sayisi = int(input("Toplam sporcu,gazi,şehit sayısını giriniz: "))
            tuketim =tuketim / hane_sayisi
            while ozel_durum_kisi_sayisi<0 or ozel_durum_kisi_sayisi>hane_sayisi:
                   ozel_durum_kisi_sayisi = int(input("Sporcu,gazi,şehit sayısı hane sayısından büyük olamaz. Tekrar girinz: "))
            engelli_kisi_sayisi = int(input("Engelli kişi sayısını giriniz: "))
            while engelli_kisi_sayisi<0 or engelli_kisi_sayisi>hane_sayisi :
                engelli_kisi_sayisi = int(input("Engelli kişi sayısı hane sayısından büyük olamaz. Tekrar giriniz: "))
            while (ozel_durum_kisi_sayisi + engelli_kisi_sayisi) > hane_sayisi:
                print("Özel ve engelli kişi sayısı toplamı hane sayısından büyük olamaz. ")
                ozel_durum_kisi_sayisi = int(input("Sporcu,gazi,şehit sayısını giriniz: "))
                engelli_kisi_sayisi = int(input("Engelli kişi sayısını giriniz: "))
            genel_ozel_durum_kisi_sayisi += ozel_durum_kisi_sayisi
            genel_engelli_sayisi += engelli_kisi_sayisi
            if ozel_durum_kisi_sayisi + engelli_kisi_sayisi > 0:
                if tuketim <= 13:
                    kademe1_sayisi+=hane_sayisi
                    indirim_su_tuketim1=(2.89/2)*((engelli_kisi_sayisi+ozel_durum_kisi_sayisi)/hane_sayisi)
                    su_tuketim = (tuketim * (2.89-indirim_su_tuketim1))*hane_sayisi
                    indirim_atik_tuketim1=(1.44/2)*((engelli_kisi_sayisi+ozel_durum_kisi_sayisi)/hane_sayisi)
                    atik_su = (tuketim * (1.44-indirim_atik_tuketim1))*hane_sayisi
                    aylik_kadame1_su = (30 * tuketim) / okuma_gun_sayisi
                    aylik_kadame1_su_toplam += aylik_kadame1_su
                if 13 < tuketim <= 20:
                    kademe2_sayisi+=hane_sayisi
                    indirim_su_tuketim1 = (2.89 / 2) * ((engelli_kisi_sayisi + ozel_durum_kisi_sayisi) / hane_sayisi)
                    indirim_su_tuketim2=(3.13/2)*((engelli_kisi_sayisi+ozel_durum_kisi_sayisi)/hane_sayisi)
                    indirim_atik_tuketim1 = (1.44 / 2) * ((engelli_kisi_sayisi + ozel_durum_kisi_sayisi) / hane_sayisi)
                    indirim_atik_tuketim2=(1.56/2)*((engelli_kisi_sayisi+ozel_durum_kisi_sayisi)/hane_sayisi)
                    su_tuketim = ((13 / oran) *(2.89-indirim_su_tuketim1) + (tuketim - (13 / oran)) *(3.13-indirim_su_tuketim2))*hane_sayisi
                    atik_su = ((13 / oran) * (1.44-indirim_atik_tuketim1)+ (tuketim - (13 / oran)) *(1.56-indirim_atik_tuketim2))*hane_sayisi
                    aylik_kadame2_su = (30 * tuketim) / okuma_gun_sayisi
                    aylik_kadame2_su_toplam += aylik_kadame2_su
                if tuketim > 20:
                    kademe3_sayisi+=hane_sayisi
                    indirim_su_tuketim1 = (2.89 / 2) * (( ozel_durum_kisi_sayisi+engelli_kisi_sayisi) / hane_sayisi)
                    indirim_su_tuketim2 = (3.13 / 2) * (( ozel_durum_kisi_sayisi+engelli_kisi_sayisi) / hane_sayisi)
                    indirim_atik_tuketim1 = (1.44 / 2) * ((ozel_durum_kisi_sayisi+engelli_kisi_sayisi) / hane_sayisi)
                    indirim_atik_tuketim2 = (1.56 / 2) * (( ozel_durum_kisi_sayisi+engelli_kisi_sayisi) / hane_sayisi)
                    indirim_su_tuketim3=(6.43/2)*((ozel_durum_kisi_sayisi)/hane_sayisi)
                    indirim_atik_tuketim3=(3.22/2)*((ozel_durum_kisi_sayisi)/hane_sayisi)
                    su_tuketim = ((((13 / oran) * (2.89 - indirim_su_tuketim1) + (7/oran) * (3.13 - indirim_su_tuketim2))+((tuketim -20) / oran) * (6.43-indirim_su_tuketim3))* hane_sayisi)
                    atik_su = ((((13 / oran) * (1.44 - indirim_atik_tuketim1) + (7/oran) * (1.56 - indirim_atik_tuketim2))+((tuketim - 20) / oran) *(3.22-indirim_atik_tuketim3))* hane_sayisi)
                    aylik_kadame3_su = (30 * tuketim) / okuma_gun_sayisi
                    aylik_kadame3_su_toplam += aylik_kadame3_su
            else:
                if tuketim <= 13:
                    kademe1_sayisi+=1
                    su_tuketim = (tuketim * 2.89) * hane_sayisi
                    atik_su = (tuketim * 1.44) * hane_sayisi
                    aylik_kadame1_su = (30 * tuketim) / okuma_gun_sayisi
                    aylik_kadame1_su_toplam+=aylik_kadame1_su
                if 14 <= tuketim <= 20:
                    kademe2_sayisi+=1
                    su_tuketim = ((13 / oran) * 2.89 + (tuketim - (13 / oran)) * 3.13) * hane_sayisi
                    atik_su = ((13 / oran) * 1.44 + (tuketim - (13 / oran)) * 1.56) * hane_sayisi
                    aylik_kadame2_su = (30 * tuketim) / okuma_gun_sayisi
                    aylik_kadame2_su_toplam += aylik_kadame2_su
                if tuketim >= 21:
                    kademe3_sayisi+=1
                    su_tuketim = ((13 / oran) * 2.89 + (7 * 3.13) + ((tuketim - 20)/ oran) * 6.43) * hane_sayisi
                    atik_su = ((13 / oran) * 1.44 + (7 * 1.56) + ((tuketim - 20 )/ oran)* 3.22) * hane_sayisi
                    aylik_kadame3_su = (30 * tuketim) / okuma_gun_sayisi
                    aylik_kadame3_su_toplam += aylik_kadame3_su
        tuketim=tuketim*hane_sayisi
        aylik_konut_tuketim = (30 * tuketim) / okuma_gun_sayisi
        aylik_konut_tuketim_toplam += aylik_konut_tuketim
        aylik_konut_tuketim_ucreti = (30 * su_tuketim) / okuma_gun_sayisi
        aylik_konut_tuketim_ucreti_toplam += aylik_konut_tuketim_ucreti
        if aylik_konut_tuketim > 100 or aylik_konut_tuketim_ucreti > 500:
                ton100_ve_tl500 += hane_sayisi

    if abone_kodu==2 :

        hane_sayisi=1
        isyeri_su+=tuketim
        isyeri_sayisi+=1
        su_tuketim=tuketim*7.38
        atik_su=tuketim*3.68
        isyeri_toplam_su_tuketim_ucreti+=su_tuketim
        isyeri_toplam_atik_su_ucreti+=atik_su
        aylik_isyeri_tuketim = (30 * tuketim) / okuma_gun_sayisi
        aylik_isyeri_tuketim_toplam+=aylik_isyeri_tuketim
        aylik_isyeri_tuketim_ucreti=(30 * su_tuketim) / okuma_gun_sayisi
        aylik_isyeri_tuketim_ucreti_toplam+=aylik_isyeri_tuketim_ucreti
    if abone_kodu==3 :
        hane_sayisi=1
        resmi_daire_su+=tuketim
        resmi_daire_sayisi+=1
        su_tuketim=tuketim*4.34
        atik_su=tuketim*2.16
        resmi_daire_toplam_su_tuketim_ucreti+=su_tuketim
        resmi_daire_toplam_atik_su_ucreti+=su_tuketim
        aylik_resmi_tuketim = (30 * tuketim) / okuma_gun_sayisi
        aylik_resmi_tuketim_toplam += aylik_resmi_tuketim
        aylik_resmi_tuketim_ucreti = (30 * su_tuketim) / okuma_gun_sayisi
        aylik_resmi_tuketim_ucreti_toplam += aylik_resmi_tuketim_ucreti
        if aylik_resmi_tuketim>max_resmi_daire:
            max_resmi_daire=aylik_resmi_tuketim
            max_resmi_daire_abone=abone_no

    if abone_kodu==4 :
        hane_sayisi=1
        organize_sanayi_sayisi+=1
        su_tuketim=tuketim*5
        atik_su=tuketim*2.50
        organize_sanayi_toplam_su_tuketim_ucreti+=su_tuketim
        organize_sanayi_toplam_atik_su_ucreti+=atik_su
        aylik_organize_tuketim = (30 * tuketim) / okuma_gun_sayisi
        aylik_organize_tuketim_toplam += aylik_organize_tuketim
        aylik_organize_tuketim_ucreti = (30 * su_tuketim) / okuma_gun_sayisi
        aylik_organize_tuketim_ucreti_toplam += aylik_organize_tuketim_ucreti

    if abone_kodu==5 :
        hane_sayisi=1
        tarim_su+=tuketim
        tarim_sayisi+=1
        if tuketim <= 13:
            su_tuketim = (tuketim*1.45)
            atik_su = (tuketim*0.72)

        if 13 < tuketim <= 20:
            su_tuketim =(13 /oran)*1.45+(tuketim - (13 / oran))*2.89
            atik_su = (13 / oran) *0.72 + (tuketim - (13 / oran))*1.44

        if tuketim >= 21:
            su_tuketim = (13 / oran)*1.45+(7/oran)*2.89 +(tuketim-(20/oran))*6.43
            atik_su = (13 / oran)*0.72 +(7/oran)*1.44 + (tuketim -(20/oran))*3.22
        tarim_toplam_su_tuketim_ucreti+=su_tuketim
        tarim_toplam_atik_su_ucreti+=atik_su
        aylik_tarim_tuketim = (30 * tuketim) / okuma_gun_sayisi
        aylik_tarim_tuketim_toplam += aylik_tarim_tuketim
        aylik_tarim_tuketim_ucreti = (30 * su_tuketim) / okuma_gun_sayisi
        aylik_tarim_tuketim_ucreti_toplam += aylik_tarim_tuketim_ucreti
        if aylik_tarim_tuketim>50:
            tarim50_sayisi+=1

    print("Abone no:",abone_no)
    if abone_kodu==1 :
        print("Abone tipi adı:Hane")
    elif abone_kodu==2:
        print("Abone tipi adı:İşyeri")
    elif abone_kodu==3:
        print("Abone tipi adı:Resmi daire")
    elif abone_kodu==4:
        print("Abone tipi adı:Organize sanayi")
    else :
        print("Abone tipi adı:İlçe Tarımsal ve Hayvan Sulama")
    kdv_tutari = ((su_tuketim + atik_su + KATI_ATIK_UCRETI*hane_sayisi + KATI_ATIK_BERTARAF_UCRETI*hane_sayisi) / 100) * 8
    fatura=su_tuketim+atik_su+(CTV*tuketim)+KATI_ATIK_BERTARAF_UCRETI*hane_sayisi+KATI_ATIK_UCRETI*hane_sayisi+kdv_tutari
    print("Dönemlik su tüketim miktarı:",tuketim)
    print("Dönemlik su tüketim ücreti:",format(su_tuketim,".2f"))
    print("Dönemlik atık su ücreti:",format(atik_su,".2f"))
    print("Dönemlik toplam su tüketim ve atık su tüketim ücreti:",format(su_tuketim+atik_su,".2f"))
    print("Dönemlik ÇTV tutarı:",format(tuketim*CTV,".2f"))
    print("Dönemlik katı atık toplama ücreti:",KATI_ATIK_UCRETI*hane_sayisi)
    print("Dönemlik katı atık bertaraf ücreti:",format(KATI_ATIK_BERTARAF_UCRETI*hane_sayisi,".2f"))
    print("Dönemlik toplam fatura tutarı:",format(fatura,".2f"))
    print("Dönemlik KDV tutarı:",format(kdv_tutari,".2f"))
    print("Dönemlik ilçe belediyesine aktarılacak tutar:",format(CTV*tuketim+KATI_ATIK_UCRETI*hane_sayisi,".2f"))
    print("Dönemlik büyükşehir belediyesine aktarılacak tutar:",format(KATI_ATIK_BERTARAF_UCRETI*hane_sayisi,".2f"))
    print("Dönemlik İZSU payı:",format(su_tuketim+atik_su,".2f"))
    baska_abone=input("Başka abone var mı?(E/e/H/h):")
    while baska_abone!= "E" and baska_abone!= "e" and baska_abone!= "h" and baska_abone!= "H":
        baska_abone = input("Lütfen E/e/H/h karakterlerinden birini giriniz:")
    genel_ctv+=(CTV*tuketim)
    genel_kta+=KATI_ATIK_UCRETI*hane_sayisi
    genel_ktba+=KATI_ATIK_BERTARAF_UCRETI*hane_sayisi
    genel_kdv+=kdv_tutari
toplam_sayi=toplam_hane_sayisi+isyeri_sayisi+resmi_daire_sayisi+organize_sanayi_sayisi+tarim_sayisi
aylik_toplam_tuketim=aylik_tarim_tuketim_toplam+aylik_organize_tuketim_toplam+aylik_resmi_tuketim_toplam+aylik_isyeri_tuketim_toplam+aylik_konut_tuketim_toplam
aylik_toplam_tuketim_ucreti=aylik_tarim_tuketim_ucreti_toplam+aylik_organize_tuketim_ucreti_toplam+aylik_resmi_tuketim_ucreti_toplam+aylik_isyeri_tuketim_ucreti_toplam+aylik_konut_tuketim_ucreti_toplam
bornova_tuketim=konut_su+isyeri_su+resmi_daire_su+organize_sanayi_su+tarim_su
tum_abone_geliri=aylik_organize_tuketim_ucreti_toplam+aylik_resmi_tuketim_ucreti_toplam+aylik_isyeri_tuketim_ucreti_toplam+aylik_konut_tuketim_ucreti_toplam+aylik_tarim_tuketim_ucreti_toplam
izsu_geliri=aylik_konut_tuketim_ucreti_toplam+aylik_isyeri_tuketim_ucreti_toplam+aylik_resmi_tuketim_ucreti_toplam+aylik_organize_tuketim_ucreti_toplam+aylik_tarim_tuketim_ucreti_toplam+konut_toplam_atik_su_ucreti+isyeri_toplam_atik_su_ucreti+resmi_daire_toplam_atik_su_ucreti+organize_sanayi_toplam_atik_su_ucreti+tarim_toplam_atik_su_ucreti
print("Konut sayısı:",toplam_hane_sayisi,"Toplam aboneler içindeki yüzdesi:",format((toplam_hane_sayisi*100)/toplam_sayi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_konut_tuketim_toplam/toplam_hane_sayisi,".2f"))
print("İşyeri sayısı:",isyeri_sayisi,"Toplam aboneler içindeki yüzdesi:",format((isyeri_sayisi*100)/toplam_sayi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_isyeri_tuketim_toplam/isyeri_sayisi,".2f"))
print("Resmi daire sayısı:",resmi_daire_sayisi,"Toplam aboneler içindeki yüzdesi:",format((resmi_daire_sayisi*100)/toplam_sayi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_resmi_tuketim_toplam/resmi_daire_sayisi,".2f"))
print("Organize sanayi sayısı:",organize_sanayi_sayisi,"Toplam aboneler içindeki yüzdesi:",format((organize_sanayi_sayisi*100)/toplam_sayi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_organize_tuketim_toplam/organize_sanayi_sayisi,".2f"))
print("İlçe Tarımsal ve Hayvansal Sulama sayısı:",tarim_sayisi,"Toplam aboneler içindeki yüzdesi:",format((tarim_sayisi*100)/toplam_sayi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_tarim_tuketim_toplam/tarim_sayisi,".2f"))
print("1.kademe konut abonelerinin sayısı:",kademe1_sayisi,"Toplam konut aboneleri içindeki yüzdesi:",format((kademe1_sayisi*100)/toplam_hane_sayisi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_kadame1_su/kademe1_sayisi,".2f"))
print("2.Kademe konut abonelerinin sayısı:",kademe2_sayisi,"Toplam konut aboneleri içindeki yüzdesi:",format((kademe2_sayisi*100)/toplam_hane_sayisi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_kadame2_su/kademe2_sayisi,".2f"))
print("3.Kademe konut abonelerinin sayısı:",kademe3_sayisi,"Toplam konut aboneleri içindeki yüzdesi:",format((kademe3_sayisi*100)/toplam_hane_sayisi,".2f"),"Aylık ortalama su tüketim miktarları:",format(aylik_kadame3_su/kademe3_sayisi,".2f"))
print("50 tondan fazla kullanan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı:",tarim50_sayisi,"İlçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdeleri:",format((tarim50_sayisi*100)/tarim_sayisi),".2f")
print("100 tondan fazla kullanan ve ya 500TL'den fazla su tüketim ücreti olan hane sayısı:",ton100_ve_tl500)
print("Şehit,gazi veya sporcu olan konut tipi abonelerin sayısı:",genel_ozel_durum_kisi_sayisi,"Toplam konut aboneleri içindeki yüzdeleri:",format((genel_ozel_durum_kisi_sayisi*100)/toplam_hane_sayisi,".2f"))
print("Engelli tipi abonelerin sayısı:",genel_engelli_sayisi,"Konut aboneleri içindeki Yüzdeleri:",format((genel_engelli_sayisi*100)/toplam_hane_sayisi,".2f"))
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone nosu:",max_resmi_daire_abone,"Aylık su tüketim miktarı:",max_resmi_daire)
print("Konutların toplam su tüketim miktarı:",format(aylik_konut_tuketim_toplam,".2f"),"Bornova içindeki yüzdeleri:",format((aylik_konut_tuketim_toplam*100)/aylik_toplam_tuketim,".2f"))
print("İşyerlerinin toplam su tüketim miktarı:",format(aylik_isyeri_tuketim_toplam,".2f"),"Bornova içindeki yüzdeleri:",format((aylik_isyeri_tuketim_toplam*100)/aylik_toplam_tuketim,".2f"))
print("Resmi dairelerin toplam su tüketim miktarı:",format(aylik_resmi_tuketim_toplam,".2f"),"Bornova içindeki yüzdeleri:",format((aylik_resmi_tuketim_toplam*100)/aylik_toplam_tuketim,".2f"))
print("Organize sanayilerin toplam su tüketim miktarı:",format(aylik_organize_tuketim_toplam,".2f"),"Bornova içindeki yüzdeleri:,",format((aylik_organize_tuketim_toplam*100)/aylik_toplam_tuketim,".2f"))
print("İlçe Tarımsal ve Hayvansal Sulamaların toplam su tüketim miktarı :",format(aylik_tarim_tuketim_toplam,".2f"),"Bornova içindeki yüzdeleri:",format((aylik_tarim_tuketim_toplam*100)/aylik_toplam_tuketim,".2f"))
print("Bornova'nın aylık su tüketim miktarı:",bornova_tuketim)
print("Konutların toplam su tüketim ücreti :",format(aylik_konut_tuketim_ucreti_toplam,".2f"))
print("İşyerlerinin toplam su tüketim ücreti:",format(aylik_isyeri_tuketim_ucreti_toplam,".2f"))
print("Resmi dairelerin toplam su tüketim ücreti:",format(aylik_resmi_tuketim_ucreti_toplam,".2f"))
print("Organize sanayilerin toplam su tüketim ücreti:",format(aylik_organize_tuketim_ucreti_toplam,".2f"))
print("İlçe Tarımsal ve Hayvansal Sulamaların toplam su tüketim ücreti:",format(aylik_tarim_tuketim_ucreti_toplam,".2f"))
print("Tüm abonelerden elde edilen aylık su tüketim ücreti:",format(tum_abone_geliri,".2f"))
print("İZSU'nun elde ettiği gelir:",format(izsu_geliri,".2f"))
print("İlçe belediyesinin elde ettiği gelir:",format(genel_ctv+genel_kta,".2f"))
print("Büyükşehir belediyesinin elde ettiği gelir:",format(genel_ktba,".2f"))
print("Devletin elde ettiği gelir:",format(genel_kdv,".2f"))
