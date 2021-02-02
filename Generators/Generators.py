# generatorler bellekte yer işgal etmeyen bir şeylermiş
# o nasıl şey lan öyle (Eğitim başında)
#

# def cube():
#     liste = []
#     for i in range(5):
#         liste.append(i ** 3)
#     return liste

def cube():
    for i in range(5):
        yield i ** 3
        # bellekte saklanmaz ihtiyaç halinde çağrılır ve kaybolur

for tmp in cube():
    print(tmp)

