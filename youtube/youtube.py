__author__ = "Vivek"
__author_email__ = "vivekltp120@gmail.com"

import os

import yt_dlp
cur_dir=os.getcwd()
def download_audio(link):
  yt_option={'extract_audio': True, 'format': 'bestaudio', 'outtmpl': os.path.join(cur_dir, '%(title)s.mp3')}
  if link.contains('playlist'):
    yt_option.update({'batch-file': True})
  with yt_dlp.YoutubeDL() as video:
    info_dict = video.extract_info(link, download = True)
    video_title = info_dict['title']
    print(video_title)
    video.download(link)
    print("Successfully Downloaded - see local folder")

def download_video(link):
  import os
  youtube_dl_options = {
    "format": "bestvideo",  # This will select the specific resolution typed here
    "outtmpl": os.path.join(cur_dir, '%(title)s.mp4')
  }

  with yt_dlp.YoutubeDL(youtube_dl_options) as video:
    info_dict = video.extract_info(link, download=True)
    video_title = info_dict['title']
    print(video_title)
    video.download(link)
    print("Successfully Downloaded - see local folder")


if __name__=="__main__":
   # download_audio('https://www.youtube.com/watch?v=28sptQICKCk&list=PLY9YBsprmPnbOR43srogzuoQJJT-SOIbq')
   download_video('https://www.youtube.com/watch?v=28sptQICKCk&list=PLY9YBsprmPnbOR43srogzuoQJJT-SOIbq')