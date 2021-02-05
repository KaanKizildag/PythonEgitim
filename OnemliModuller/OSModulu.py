import os
from datetime import datetime

result = dir(os)
result = os.name # posix -> linux, nt -> windows
result = os.getcwd() # current working directory

# result = os.getcwd() # current working directory

#result = os.listdir()


#result = os.stat('DateTime.py')
#result = datetime.fromtimestamp(result.st_mtime) # değiştirilme tarihi (modified)
#result = datetime.fromtimestamp(result.st_atime) # erişim tarihi (access)
#result = datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi (create (?))

# os.system('netbeans') # -> direkt komutları yollarsın

# path

#result = os.path.abspath('OSModulu.py')
result = os.path.dirname(os.path.abspath('OSModulu.py')) # -> adı bilinen dosyanın yolu


print(result)