import vlc 
import time
song_list = ["C:\\Users\\Subash_G Mark2\\Music\\Elley-Duhe-Middle-of-the-Night.mp3","C:\\Users\\Subash_G Mark2\\Music\\Eminem_-_Venom_Remix_.mp3","C:\\Users\\Subash_G Mark2\\Music\\Chammak-Challo-(Muthada-Chammak-Challo)-MassTamilan.fm.mp3"
,"C:\\Users\\Subash_G Mark2\\Music\\[MP3DOWNLOAD.TO] Sean Paul - No Lie ft. Dua Lipa-320k.mp3","C:\\Users\\Subash_G Mark2\\Music\\Arcade Duncan Laurence Lyrics Terjemahan Loving you is a losing game.mp3"
,"C:\\Users\\Subash_G Mark2\\Music\\Aurora Runaway Mp3 Song(NewDjSongRemix).mp3"]
for song in song_list :
	print(song,"is Now Playing!")
	p = vlc.MediaPlayer(song)
	p.play()
	media = p.get_media()
	d = vlc.MediaPlayer.get_length()
	print(d)
	time.sleep(240)
	p.stop()
	continue