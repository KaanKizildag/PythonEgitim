import urllib.request 
url = "https://icons.iconarchive.com/icons/goescat/macaron/128/atom-icon.png"
url1 = "https://icons.iconarchive.com/icons/goescat/macaron/128/burp-suite-icon.png"
url2 = "https://icons.iconarchive.com/icons/goescat/macaron/128/calc-icon.png"

urller = [url, url1, url2,"https://icons.iconarchive.com/icons/papirus-team/papirus-mimetypes/128/app-x-iso9660-appimage-icon.png"]
import os
os.system("clear")
say = 1
for url in urller:
	resim =  urllib.request.urlretrieve(url, "resim_" + str(say) + ".jpg")
	os.system("clear")
	print("resim_" + str(say) + " indirildi.")
	say += 1




