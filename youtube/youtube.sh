#youtube-dl -f "bestaudio/best" -ciw -o "%(title)s.%(ext)s" -v --extract-audio https://www.youtube.com/watch?v=c29tZVZpZGVvUGxheWxpc3RQYXJ0



#audio from youtube list
# -a for download from a list of urls
yt-dlp -f "bestaudio/best" -ciw -o "/media/vivek/WD_HD/Fun/Audio/Converted/Fav_Evergreen/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format wav -a audio_url.txt
yt-dlp -f "bestaudio/best" -ciw -o "/media/vivek/CRETA/Fav_Mix/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format wav  -a /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/audio_url.info --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info
yt-dlp -f "bestaudio/best" -ciw -o "/media/vivek/CRETA/Bhakti/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format mp3  -a /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/devotional_audio_url.info --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info
yt-dlp -f "bestaudio/best" -ciw -o "/media/vivek/WALKMAN/Bhakti/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format mp3  -a /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/devotional_audio_url.info --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info

#user creted playlist with cookies
#devotional
yt-dlp -f "bestaudio/best" -ciw --cookies-from-browser brave -o  "/media/vivek/CRETA1/Bhakti/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format mp3  https://www.youtube.com/playlist?list=PLY9YBsprmPnbOR43srogzuoQJJT-SOIbq --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info
yt-dlp -f "bestaudio/best" -ciw --cookies-from-browser brave -o  "/media/vivek/WALKMAN/Bhakti/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format mp3  https://www.youtube.com/playlist?list=PLY9YBsprmPnbOR43srogzuoQJJT-SOIbq --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info

#daily devotional 
yt-dlp -f "bestaudio/best" -ciw --cookies-from-browser brave -o  "/media/vivek/CRETA1/Bhakti/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format mp3  https://www.youtube.com/playlist?list=PLY9YBsprmPnYqwqt-pPuN3DVS580_yNhv --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info
yt-dlp -f "bestaudio/best" -ciw --cookies-from-browser brave -o  "/home/vivek/Music/Bhakti/%(title)s.%(ext)s" -v --extract-audio --audio-quality 0 --audio-format mp3  https://www.youtube.com/playlist?list=PLY9YBsprmPnYqwqt-pPuN3DVS580_yNhv --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_audio_url.info

#favourite


#video file
#give in  best available mp4 format
#yt-dlp -f "best" -ciw -o "/media/vivek/Data/Vivek/Interview_Prep/AI_ML_Concept/Tutorials/%(title)s.%(ext)s" -v -a /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/video_url.txt

#best video format
yt-dlp  -o "/media/vivek/Data/Vivek/Interview_Prep/Tutorials/%(title)s.%(ext)s" -v -a /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/video_url.txt

# bytebytego mentaining the archieve file
yt-dlp -f "best" -ciw --cookies-from-browser brave -o "/media/vivek/Data/Vivek/Interview_Prep/System Design/Design_Interview/Design_Fundamental_byte_byte_go/%(title)s.%(ext)s" -v -a /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/edu_video_url.info --download-archive /media/vivek/Data/Vivek/Interview_Prep/CompetitiveCoding/youtube/downloaded_video_url_edu_url.info

#short name
yt-dlp -o "%(id)s.%(ext)s"  https://www.youtube.com/watch?v=hux7hG6NrHE&ab_channel=AasthaChannel