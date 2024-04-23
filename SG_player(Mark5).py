from tkinter import *
import vlc 
import time 
dashboard = Tk()
dashboard.geometry("500x300")
dashboard.title("SG_Player (Mark5)")
def play():
	songs = ["C:\\Users\\Subash_G Mark2\\Music\\Elley-Duhe-Middle-of-the-Night.mp3","C:\\Users\\Subash_G Mark2\\Music\\Eminem_-_Venom_Remix_.mp3","C:\\Users\\Subash_G Mark2\\Music\\Chammak-Challo-(Muthada-Chammak-Challo)-MassTamilan.fm.mp3"
,"C:\\Users\\Subash_G Mark2\\Music\\[MP3DOWNLOAD.TO] Sean Paul - No Lie ft. Dua Lipa-320k.mp3","C:\\Users\\Subash_G Mark2\\Music\\Arcade Duncan Laurence Lyrics Terjemahan Loving you is a losing game.mp3"
,"C:\\Users\\Subash_G Mark2\\Music\\Aurora Runaway Mp3 Song(NewDjSongRemix).mp3"]
	for s in songs:
		media_player = vlc.MediaPlayer()
		media = vlc.Media(s)
		media_player.set_media(media)
		media_player.play()
		time.sleep(1)
		d = str(media.get_duration())
		sd = d[0:3]
		print(s,"is Having the Duration :",sd)
		isd = int(sd)
		time.sleep(isd)
		

def stop():
	play()
	media.stop()
	media.stop()
play_button = Button(dashboard,text="Play!",command = play,bg = "red")
stop_button = Button(dashboard,text="Stop!",command= stop,bg="green")
play_button.grid()
stop_button.grid()
dashboard.mainloop()