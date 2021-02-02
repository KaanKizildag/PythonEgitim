# iteratorler IIterable interface ini iplemente eder (Javada)
# python da __iter__() ve __next()__ metotlarını belirtmelisin

# aralık içindeki değerleri yazdır
class MyIterableClass():

    def __init__(this, bas, bit, adim = 1):
        this.bas = bas
        this.bit = bit
        this.adim = adim

    def __iter__(this):
        return this

    def __next__(this):
        if this.bas <= this.bit:
            x = this.bas
            this.bas += this.adim
            return x
        else:
            raise StopIteration
            # şayet sonraki nesne yoksa bu hata fırlatılsın

list = MyIterableClass(20,50,2)

for tmp in list:
    print(tmp)

