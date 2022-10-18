#importing the youtube
from pytube import YouTube

#Initialization
yt = YouTube('https://www.youtube.com/watch?v=-KnAZcXzxRA')

#Gets the first stream
stream = yt.streams.first()

#Downloading
stream.download()
'C:\\Python\\Python3\\Ravin\U0001f525\U0001f525\U0001f525.mp4'