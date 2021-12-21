from mhyt import yt_download
url = r"https://www.youtube.com/watch?v=0BVqFYParRs"
file = "Clouds.mp4"
yt_download(url,file)
#########################
file = "Clouds_music.mp3"
yt_download(url,file,ismusic=True)