liste = ['21','2s','4a','Beyda','15',]

def sayiMi(girdi):
    try:
        int(girdi)
        return True
    except ValueError:
        False

# liste içindeki sayısal elemanları bulun
'''for tmp in liste:
    if (sayiMi(tmp)):
        print(tmp + "--> değeri sayıdır")
'''
# kullanıcı q girmediği durumlarda  inputun sayı olduğunu doğrulayın
print('soru 2')

while True:
    x = input('Bir şeyler giriniz: ')
    if x != 'q':
        try:
            x = int(x)
            print(str(x) + '--> değeri sayıdır')
        except ValueError:
            print('gecersiz sayi')
            pass
    else:
        break


# girilen parola içinde türkçe karakter olup olmadığına bakınız

#