with open('karakterler.txt','r') as file:
    print(file.tell())
    karakterler = file.read()
    print(karakterler)
    print(file.tell()) # cursor konumunu döner
    file.seek(10) # cursoru ilgili konuma gönder
    karakterler = file.read()
    print(karakterler)