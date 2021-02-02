#Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# nasıl kullanılır.
# dosya erişme modu ==>

# w (write) yazma modu. dosyayı oluşturur içeriği siler ve yeniden yazar
# a (Append) ekleme modu. dosya konumda yoksa oluşturur
# x (create) oluşturma zaten varsa hata verir
# r (read) varsayılan mod. dosya konumda yoksa hata verir

file = open('deneme.txt','a')
file.write('Hüseyin Kaan Kızıldağ\n')
file.close()