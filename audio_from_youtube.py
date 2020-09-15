from __future__ import unicode_literals
import youtube_dl


def download_wev_from_youtube(link: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloaded_audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


print('input string: ')
input_string = input()
download_wev_from_youtube(input_string)
