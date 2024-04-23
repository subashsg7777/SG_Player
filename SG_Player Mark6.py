import mysql.connector
import vlc
import time
mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "",database = "songsd")
cursor = mydb.cursor()
sql = "select * from songs_table"
cursor.execute(sql)
result = cursor.fetchall()
lresult = list(result)
print(type(lresult))
for i in lresult:
    media_player = vlc.MediaPlayer()
    print(i)
    ci = str(i)
    c2i= ci[7:-2]
    print(c2i)
    media = vlc.Media(c2i)
    media_player.set_media(media)
    media_player.play()
    time.sleep(2)
    d = str(media.get_duration())
    print(d)
    sd = d[0:3]
    print(i,"is Playing Now And It's duration is :",sd,"Seconds")
    isd = int(sd)
    choice = input("enter the choice :")
    if(choice == "s"):
        time.sleep(isd)
    elif(choice == "n"):
        media_player.stop()
        continue
    else:
        time.sleep(isd)