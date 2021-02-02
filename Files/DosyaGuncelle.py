with open('guncellemeDosyasi.txt','r+') as file:
    content = file.read()
    print(content)
    print('-'*20)
    file.seek(20)
    file.write('\nZeynep\n') # r+ modunda açıldı
    file.seek(0)
    content = file.read()
    print(content)