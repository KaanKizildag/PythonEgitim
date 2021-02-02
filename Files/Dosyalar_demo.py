with open('OgrenciBilgiSistemi.txt','a') as file:
    pass



def menuBas():

    print('1_Dosyayı oku\n'
          '2_Dosyaya ekle\n'
          '3_Ortalama Hesapla\n'
          '4_Çıkış\n'
          'Seçiminiz: ', end="")


def dosyayiOku():
    with open('OgrenciBilgiSistemi.txt','r') as file:
        print('-'*20)
        print(file.read())
        print('-' * 20)
        input()


def dosyayaEkle(isim, not1, not2, not3):
    with open('OgrenciBilgiSistemi.txt','a') as file:
        file.write(isim + " " +
                   str(not1)+ " " +
                   str(not2)+ " " +
                   str(not3)+'\n')



def ortalamaHesapla():
    pass


while True:
    menuBas()
    islem = input()
    if islem == '1':
        dosyayiOku()
    elif islem == '2':
        isim = input('İsminizi girin: ')
        not1 = int(input('not1: '))
        not2 = int(input('not2: '))
        not3 = int(input('not3: '))
        dosyayaEkle(isim,not1,not2,not3)
    elif islem == '3':
        ortalamaHesapla()
    elif islem == '4':
        break

