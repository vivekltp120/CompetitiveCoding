#split mp3
 mp3splt -o @f_@n  -f -S +10 'श्रीमद भगवद गीता सार ｜ संपूर्ण गीता ｜ Bhagawad Geeta- All Chapters With Narration｜ Shailendra Bharti.mp3'
 mp3splt -o @f_@n   -f -S 10 '/media/vivek/CRETA/Old_Evergreen/Aashiqui Songs Most Bollywood Romantic Songs ｜｜ Aashiqui & Aashiqui 2 ｜｜ Jukebox.wav'
 #working
ffmpeg -i 'श्रीमद भगवद गीता सार ｜ संपूर्ण गीता ｜ Bhagawad Geeta- All Chapters With Narration｜ Shailendra Bharti.mp3' -vn -acodec copy -ss 00:00:00 -t 00:01:50 Gita_Sar.mp3
