import re
string = 'Merhaba python kursu | Regular expression'
#
# result = re.findall('Regular',string)

# patern değişebilir.
# result = re.split(' ', string)  # boşluk için bir ayrım yaptı
#result = re.split('\|',string) # | karekteri ayrımı yapıldı (\| şeklinde yazıldı)

# result = re.sub(' ','-',string) # replace

result = re.search('Regular',string)  # re.Match Objesi
# result = result.start()
# print(result)

########################################################################

print('#'*20)
# string = 'merhaba bu bir deneme metnidir. bu string üzerinde aramalar yapılacaktır.'

# result = re.findall('[a,b,c]', string) # Köşeli parantez içerisinde yazılan karakterler tek tek aranır
# print(len(result)) # 14

# result = re.findall('[a-z]', string) # a dan z ye kadar tüm karakterler.

# result = re.findall('[^0-9]', string) # rakam haricindeki karakterler

# result = re.findall('...', string) # . herhangi bir karakteri tutar 3 erli grupla
# ['mer', 'hab', 'a b', 'u b', 'ir ', 'den'.....] gibi

# result = re.findall('.erhaba', string)
'''
 ^ ifadesi String .. ile başlıyor mu?  ---> ^M -> Merhaba 
 $ ifadesi String .. ile bitiyor mu?  --> yapılacaktır\.$ -> yapılacaktır. döner biten metni döndürür 
 \ ifadesi re bunu yorumlamasın demek
'''
# result = re.findall('yapılacaktır.$', string)

# string = 'mn' # maaan, maan, maaaaaaaaaaaaan --> geçerli karakterlerdir.
# result = re.findall('ma*n', string)


'''
    otomata dersini hatırla 
    * Kleene star
    + klenee plus 
    
    + boş karakter kabul etmez * kabul eder tek farkları bu
    
    ? ifadesi 0 ya da 1 kez tekrar edebilir
    
    {2} öncesindeki karakterin parantez içindeki kadar tekrar etmesini temsil eder
    {2,3} en az iki en fazla 3 olacak demek
    
'''

# result = re.findall('[0-9]{2}', string) # iki basamaklı değerleri getir demek

'''
    | or işareti
    a | b a ya da b arar 
'''

'''
    (a|b|c)xz => axz , bxz , abxz kabul 
'''
#
# string = 'abxz'
# result = re.findall('(a|b|c)xz', string)


print(result)


