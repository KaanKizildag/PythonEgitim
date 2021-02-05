from datetime import datetime, timedelta
# print(help(datetime))

# print(datetime.now().date())
simdi = datetime.now()

result = datetime.ctime(simdi) # Tue Feb  2 21:20:39 2021
result = datetime.strftime(simdi,'%Y')  # 2021
result = datetime.strftime(simdi,'%D')  # 02/02/21
result = datetime.strftime(simdi,'%X')  # 21:23:14
result = datetime.strftime(simdi,'%A')  # Tuesday
'''
%B -> ay bilgisi ...
'''

s = '15 April 2020 saat 14:43:30'

result = datetime.strptime(s,'%d %B %Y saat %H:%M:%S')
# result = result.time() # --> artık obje oluştu

result = simdi - result # -> timedelta objesi
# 293 days, 6:51:21.116103 --> toString metodu bu şekilde (override) yazılmış
#print(simdi)
result = simdi + timedelta(10) # --> 10 gün sonrası

'''
2021-02-02 21:37:50.578816
2021-02-12 21:37:50.578816
'''

print(result)

