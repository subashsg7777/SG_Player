from tkinter import *
import vlc 
import time
songs = ["C:\\Users\\Subash_G Mark2\\Music\\Elley-Duhe-Middle-of-the-Night.mp3","C:\\Users\\Subash_G Mark2\\Music\\Eminem_-_Venom_Remix_.mp3","C:\\Users\\Subash_G Mark2\\Music\\Chammak-Challo-(Muthada-Chammak-Challo)-MassTamilan.fm.mp3"
,"C:\\Users\\Subash_G Mark2\\Music\\[MP3DOWNLOAD.TO] Sean Paul - No Lie ft. Dua Lipa-320k.mp3","C:\\Users\\Subash_G Mark2\\Music\\Arcade Duncan Laurence Lyrics Terjemahan Loving you is a losing game.mp3"
,"C:\\Users\\Subash_G Mark2\\Music\\Aurora Runaway Mp3 Song(NewDjSongRemix).mp3"]
for s in songs:
	media_player = vlc.MediaPlayer()
	media = vlc.Media(s)
	media_player.set_media(media)
	media_player.play()
	time.sleep(2)
	d = str(media.get_duration())
	print(d)
	sd = d[0:3]
	print(sd)
	isd = int(sd)
	time.sleep(isd)