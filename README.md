# IZSU-FATURA-PROGRAMI
FARKLI TARİFELERE GÖRE FATURA HESAPLAYAN PROGRAM(PYTHON)

İZSU tarafından bir faturalama döneminde kullanılmak üzere, Bornova ilçesinde ikamet eden abonelerin dönemlik (yaklaşık 1 aylık) su faturalarını düzenlemek ve abonelerin su tüketimi hakkında bazı istatistiksel bilgiler elde etmek için bir program geliştirilmesi istenmektedir. Bu amaçla her abone ve ilgili dönem için aşağıdaki veriler programa girilecektir: 
• Abone no 
• Abone tipi kodu: tamsayı (1-5 arasında) 
• Abone tipi konut ise 
o Hane sayısı: tamsayı (1 ya da 1’den büyük) 
o Hane sayısı 1 ise 
İndirim durumu: Yok/Şehit/Gazi/Sporcu/Engelli: (Y/y/Ş/ş/G/g/S/s/E/e karakterleri) 
o Hane sayısı 1’den büyük ise 
Şehit, gazi veya sporcu sayısı: tamsayı (0 ile hane sayısı arasında) 
Engelli sayısı: tamsayı (0 ile hane sayısı arasında) 

(Not: Toplam şehit, gazi, sporcu ve engelli sayısı, hane sayısından büyük olmamalıdır.) 
• Önceki sayaç değeri: tamsayı (0 ya da 0’dan büyük) 
• Şimdiki sayaç değeri: tamsayı (önceki sayaç değerine eşit ya da daha büyük) 
• Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısı: tamsayı (0’dan büyük) 

Her abonenin verileri girildikten sonra, o abone için ilgili döneme ait su faturası üzerinde bulunacak olan aşağıdaki bilgiler ekrana yazdırılmalıdır: 

Abone no 
Abone tipi adı 
Dönemlik su tüketim miktarı 
Dönemlik su tüketim ücreti 
Dönemlik atık su ücreti 
Dönemlik toplam su tüketim ve atık su ücreti 
Dönemlik ÇTV tutarı 
Dönemlik katı atık toplama ücreti 
Dönemlik katı atık bertaraf ücreti 
Dönemlik toplam fatura tutarı 
Dönemlik devlete aktarılacak KDV tutarı (%8) 
Dönemlik ilçe belediyesine aktarılacak tutar 
Dönemlik büyükşehir belediyesine aktarılacak tutar 
Dönemlik İZSU payı 

Daha sonra başka abone olup olmadığı sorularak (e/E/h/H karakterleri); varsa sonraki aboneye ilişkin işlemler yapılmalı, yoksa aşağıdaki istatistiksel bilgiler ekrana yazdırılmalıdır: 

(Not: Aşağıdaki istatistiksel çıktılarda “aylık” değerler bulunurken, 1 ay 30 gün kabul edilerek dönemlik değerler aylık değerlere çevrilmelidir. Ayrıca konut tipi aboneler için her bir hane ayrı bir abone olarak ele alınmalıdır.) 

• Her abone tipi için; abone (hane) sayıları, yüzdeleri ve aylık ortalama su tüketim miktarları 
• Aylık su tüketim miktarlarına göre her kademedeki konut tipi abonelerin (hanelerin) sayıları, konut tipi aboneler içindeki yüzdeleri ve aylık ortalama su tüketim miktarları 
• Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı ve ilçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi 
• Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı 
• Şehit, gazi veya devlet sporcusu olan ve engelli olan konut tipi abonelerin (hanelerin) sayısı ve konut tipi aboneler (haneler) içindeki yüzdeleri 
• Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su ve aylık su tüketim miktarı 
• Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su, abone tipi adı, aylık su tüketim miktarı ve ödediği aylık su tüketim ücreti 
• Her abone tipi için aylık toplam su tüketim miktarları, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdeleri ve Bornova’nın aylık toplam su tüketim miktarı 
• Her abone tipi için elde edilen aylık toplam su tüketim ücretleri ve tüm abonelerden elde edilen aylık toplam su tüketim ücreti 
• İlgili dönemde su faturalarından İZSU’nun, ilçe belediyesinin, büyükşehir belediyesinin ve devletin elde ettiği gelir tutarları 

İZSU tarafından bir faturalama döneminde kullanılmak üzere, Bornova ilçesinde ikamet eden abonelerin dönemlik (yaklaşık 1 aylık) su faturalarını düzenlemek ve abonelerin su tüketimi hakkında bazı istatistiksel bilgiler elde etmek için bir program geliştirilmesi istenmektedir. Bu amaçla her abone ve ilgili dönem için aşağıdaki veriler programa girilecektir: 
• Abone no 
• Abone tipi kodu: tamsayı (1-5 arasında) 
• Abone tipi konut ise 
o Hane sayısı: tamsayı (1 ya da 1’den büyük) 
o Hane sayısı 1 ise 
İndirim durumu: Yok/Şehit/Gazi/Sporcu/Engelli: (Y/y/Ş/ş/G/g/S/s/E/e karakterleri) 
o Hane sayısı 1’den büyük ise 
Şehit, gazi veya sporcu sayısı: tamsayı (0 ile hane sayısı arasında) 
Engelli sayısı: tamsayı (0 ile hane sayısı arasında) 

(Not: Toplam şehit, gazi, sporcu ve engelli sayısı, hane sayısından büyük olmamalıdır.) 
• Önceki sayaç değeri: tamsayı (0 ya da 0’dan büyük) 
• Şimdiki sayaç değeri: tamsayı (önceki sayaç değerine eşit ya da daha büyük) 
• Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısı: tamsayı (0’dan büyük) 

Her abonenin verileri girildikten sonra, o abone için ilgili döneme ait su faturası üzerinde bulunacak olan aşağıdaki bilgiler ekrana yazdırılmalıdır: 

Abone no 
Abone tipi adı 
Dönemlik su tüketim miktarı 
Dönemlik su tüketim ücreti 
Dönemlik atık su ücreti 
Dönemlik toplam su tüketim ve atık su ücreti 
Dönemlik ÇTV tutarı 
Dönemlik katı atık toplama ücreti 
Dönemlik katı atık bertaraf ücreti 
Dönemlik toplam fatura tutarı 
Dönemlik devlete aktarılacak KDV tutarı (%8) 
Dönemlik ilçe belediyesine aktarılacak tutar 
Dönemlik büyükşehir belediyesine aktarılacak tutar 
Dönemlik İZSU payı 

Daha sonra başka abone olup olmadığı sorularak (e/E/h/H karakterleri); varsa sonraki aboneye ilişkin işlemler yapılmalı, yoksa aşağıdaki istatistiksel bilgiler ekrana yazdırılmalıdır: 

(Not: Aşağıdaki istatistiksel çıktılarda “aylık” değerler bulunurken, 1 ay 30 gün kabul edilerek dönemlik değerler aylık değerlere çevrilmelidir. Ayrıca konut tipi aboneler için her bir hane ayrı bir abone olarak ele alınmalıdır.) 

• Her abone tipi için; abone (hane) sayıları, yüzdeleri ve aylık ortalama su tüketim miktarları 
• Aylık su tüketim miktarlarına göre her kademedeki konut tipi abonelerin (hanelerin) sayıları, konut tipi aboneler içindeki yüzdeleri ve aylık ortalama su tüketim miktarları 
• Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı ve ilçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi 
• Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı 
• Şehit, gazi veya devlet sporcusu olan ve engelli olan konut tipi abonelerin (hanelerin) sayısı ve konut tipi aboneler (haneler) içindeki yüzdeleri 
• Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su ve aylık su tüketim miktarı 
• Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su, abone tipi adı, aylık su tüketim miktarı ve ödediği aylık su tüketim ücreti 
• Her abone tipi için aylık toplam su tüketim miktarları, Bornova’nın aylık toplam su tüketim miktarı içindeki yüzdeleri ve Bornova’nın aylık toplam su tüketim miktarı 
• Her abone tipi için elde edilen aylık toplam su tüketim ücretleri ve tüm abonelerden elde edilen aylık toplam su tüketim ücreti 
• İlgili dönemde su faturalarından İZSU’nun, ilçe belediyesinin, büyükşehir belediyesinin ve devletin elde ettiği gelir tutarları 

