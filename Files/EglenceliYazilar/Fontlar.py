import pyfiglet

list = []

with open('Fontlar','r') as file:
    line = file.readline()
    while(line):
        list.append(line)
        line = file.readline()

for i in list:
    try:
        print(i[:-1])
        print(pyfiglet.figlet_format('kaan',font = i[:-1]))
        print('-'*20)
    except:
        print('font bulunamadı')
        pass

