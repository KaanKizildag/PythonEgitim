def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as ex:
        raise ex

try:
    print(divide(10,1))
except:
    print('Sıfıra bölme hatası')
'''
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
except ZeroDivisionError:
    print("y değeri 0 olamaz")
except ValueError as ex:
    raise ex
    print('Sayısal veri giriniz')
else: # except çalışmazsa buraya girer
    print("her şey yolunda")
finally:
    print("Her durumda çalışır")

'''
'''
    Bütün hatalar Exception base classından türetilmiştir 

'''