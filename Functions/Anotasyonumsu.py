def my_decorator(func):

    def wrapper():
        print('Fonksiyondan önceki metotlar')
        func()
        print('fonksiyondan sonraki metotlar')

    return wrapper # metodu çağırma metodu gönder


@my_decorator # anotasyon bazlı bir metot oluşturulur
def sayHello():
    print('merhaba Anotasyonumsu şey')

# my_decorator(sayHello)


sayHello()

