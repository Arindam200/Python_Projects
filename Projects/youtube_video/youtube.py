
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=WWhgssiyfwY&list=WL&index=1&t=5s')
print(yt.thumbnail_url)
print(yt.title)


my_video=yt.streams.get_highest_resolution()
my_video.download()