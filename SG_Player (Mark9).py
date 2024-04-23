'''
what's new in SG_Player (mark8)
1) itrative song addition - Added
2) specifing from which mode is the song is playing - Added
3) replacing sleep method with media.is_playing() method - Added
4) new 5 songs added to database - Added
5) add list view and it's query is SELECT * FROM `songs_table` ORDER BY no - Added
'''


'''
what's new in SG_Player (mark9)
1)index playing mode was introduced - Added
2)previous song mode is introduced - Added
3) loop mode is introduced - Added
4) new 5 songs added to database server - Added
5)database data entry bug fixed - Added

'''
import mysql.connector
import vlc
import time
mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "",database = "songsd")
cursor = mydb.cursor()
index = int(1)
#sindex = str(index)
#print(type(sindex))
for i in range(10,20):
    sql = f"select url from songs_table where no = {i}"
    media_player = vlc.MediaPlayer()
    print(i)
    cursor.execute(sql)
    result = cursor.fetchall()
    print("the current song is (from index playing mode) :",result)
    ci = str(result)
    c2i= ci[3:-4]
    print("the c2i is :",c2i)
    media = vlc.Media(c2i)
    media_player.set_media(media)
    print("media set sucessfully")
    media_player.play()
    print("media played !")
    time.sleep(1)

    sd = 240
    print(i,"is Playing Now And It's duration is :",sd,"Seconds")
    isd = int(sd)
    choice = input("enter the choice :")
    if(choice == "s"):
        print("The Current Song Is Playing In Normal Mode")
        while True :
            if(media_player.is_playing() == 1):
                continue
            elif(media_player.is_playing() == 0):
                break
            else:
                print("Error Code : SG001")
        #time.sleep(isd)
    elif(choice == "n"):
        print("The Current Song Is Skipped And The Current Song Is :",c2i)
        media_player.stop()
        continue
    elif(choice == "a"):
        def song_addition():
            no = int(input("Enter the Number of the Song :"))
            url = input("Enter The Url :")
            sql2 = "insert into songs_table(no,url) values(%s,%s)"
            val = no, url
            cursor.execute(sql2, val)
            print("The New Song Addition is Sucessfull !")



        song_addition()
        while True :
            achoice = input("If You Want To Add More Songs To Database :")
            if(achoice == "s"):
                song_addition()
            elif(achoice == "n"):
                print("The Song Is Playing In Addition Skipped Mode")
                while True:
                    if (media_player.is_playing() == 1):
                        continue
                    elif (media_player.is_playing() == 0):
                        break
                    else:
                        print("Error Code : SG001")
                break

            else:
                print("The Song Is Playing In Addiion Else Mode (Rare Mode)")
                while True:
                    if (media_player.is_playing() == 1):
                        continue
                    elif (media_player.is_playing() == 0):
                        break
                    else:
                        print("Error Code : SG001")
                break
    elif(choice == "l"):
        media_player.stop()
        cursor.execute("SELECT * FROM `songs_table` ORDER BY no ")
        result = cursor.fetchall()
        for i in result:
            print(i)
        print("---------------------------------------END OF THE LIST-----------------------------------")
        continue

    elif (choice == "p"):
        media_player.stop()
        i = i - 1
        print("the is :", i)
        media_player2 = vlc.MediaPlayer()
        sql3 = f"select * from songs_table where no = {i}"
        cursor.execute(sql3)
        re = cursor.fetchall()
        print("the re is :", re)
        purl = re[0][1]
        print(purl)
        media = vlc.Media(purl)
        media_player2.set_media(media)
        media_player2.play()
        time.sleep(5)
        while True:
            if (media_player2.is_playing() == 1):
                continue
            elif (media_player2.is_playing() == 0):
                print("song is fully completed")
                break
    elif (choice == "lo"):
        while True :
            sql4 = f"select url from songs_table where no = {i}"
            cursor.execute(sql4)
            re3 = cursor.fetchall()
            print("re3 is :",re3)
            looping_url = str(re3[0])
            looping_url = looping_url[2:-3]
            print("the looping song is :", looping_url)
            media_player3 = vlc.MediaPlayer()
            media3 = vlc.Media(looping_url)
            media_player3.set_media(media3)
            media_player.stop()
            media_player3.play()
            print("The song ", looping_url, "is looping now !")
            time.sleep(2)
            d = str(media3.get_duration())
            print(d)
            sd = d[0:3]
            print(i, "is Playing Now And It's duration is :", sd, "Seconds")
            isd = int(sd)
            time.sleep(isd)
    else:
        print("the else part is running!")
        while True:
            if (media_player.is_playing() == 1):
                continue
            elif (media_player.is_playing() == 0):
                break
            else:
                print("Error Code : SG001")
