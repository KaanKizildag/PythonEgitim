from pytube import YouTube
liste = []
_url = ''
videolar = []

def download(index,url):
    yt = YouTube(url=url)
    videolar = yt.streams.filter()
    print(videolar[index])
    videolar[index].download()

def analiz(url):
    yt = YouTube(url=url)
    videolar = yt.streams.filter()
    for eleman in videolar:
        if(eleman.type == 'audio'):
            liste.append('Ses: ' +eleman.abr)
        else:
            liste.append(eleman.resolution + ' Format: ' + eleman.mime_type)
    print('analiz metodu çalışıyor')


# list = Downloader.analiz(url = 'https://www.youtube.com/watch?v=VHoT4N43jK8')
