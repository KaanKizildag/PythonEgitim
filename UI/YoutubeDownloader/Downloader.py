from pytube import YouTube

def download(self):
    url = 'https://www.youtube.com/watch?v=HCjNJDNzw8Y'
    yt = YouTube(url=url)
    vids= yt.streams.all()
    for i in range(len(vids)):
        print(i,'. ',vids[i])
    video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

    print(video.resolution)
    input('indirelim mi?')

    video.download()