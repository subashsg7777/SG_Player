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

'''
what's new in SG_Player (mark10)
1)resume mode playing - Added
2)random mode -Added
3)playlist mode -Added
4) que mode -Added
5) new song addition 
'''
#C:\Users\Subash_G Mark2\Music\David Guetta - Hey Mama, (ft. Nicki Minaj, Bebe Rexha) Lyrics (320 kbps).mp3
#C:\Users\Subash_G Mark2\Music\Dumeel-MassTamilan.com.mp3
#C:\Users\Subash_G Mark2\Music\Enemy(PaglaSongs).mp3
#C:\Users\Subash_G Mark2\Music\Fairytale.mp3
#C:\Users\Subash_G Mark2\Music\Eyy-Beta-Idhu-En-Patta-MassTamilan.fm.mp3


import mysql.connector
import vlc
import time
import random
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
    c2i= ci[5:-2]
    ioi = ci[1:2]
    print("ioi :" , ioi)
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
    def stopm():
        print("stopping!")
        media_player.stop()
    choice = input("enter the choice :")
    if(choice == "s"):
        print("The Current Song Is Playing In Normal Mode")
        while True :
            if(media_player.is_playing() == 1):
                continue
            elif(media_player.is_playing() == 0):
                try:
                    sql2 = "DELETE FROM `resume` WHERE no = 1"
                    cursor.execute(sql2)
                    sql3 = f"INSERT INTO `resume`(`no`, `index`) VALUES (1,{ioi})"
                    cursor.execute(sql3)
                    print(f"the resume key for the {c2i} song is set sucessfully ! ")
                except :
                    print("error in resume key set function !")
                break


            else:
                print("Error Code : SG001")
        #time.sleep(isd)

    elif(choice == "n"):
        stopm()
        print("The Current Song Is Skipped And The Current Song Is :",c2i)
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
                        try:
                            sql2 = "DELETE FROM `resume` WHERE no = 1"
                            cursor.execute(sql2)
                            sql3 = f"INSERT INTO `resume`(`no`, `index`) VALUES (1,{ioi})"
                            cursor.execute(sql3)
                            print(f"the resume key for the {c2i} song is set sucessfully ! ")
                        except:
                            print("error in No resume key set function !")
                        break

            else:
                print("The Song Is Playing In Addiion Else Mode (Rare Mode)")
                while True:
                    if (media_player.is_playing() == 1):
                        continue
                    elif (media_player.is_playing() == 0):
                        try:
                            sql2 = "DELETE FROM `resume` WHERE no = 1"
                            cursor.execute(sql2)
                            sql3 = f"INSERT INTO `resume`(`no`, `index`) VALUES (1,{ioi})"
                            cursor.execute(sql3)
                            print(f"the resume key for the {c2i} song is set sucessfully ! ")
                        except:
                            print("error in resume key set function !")
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
            if (media_player.is_playing() == 1):
                continue
            elif (media_player.is_playing() == 0):
                try:
                    sql2 = "DELETE FROM `resume` WHERE no = 1"
                    cursor.execute(sql2)
                    sql3 = f"INSERT INTO `resume`(`no`, `index`) VALUES (1,{ioi})"
                    cursor.execute(sql3)
                    print(f"the resume key for the {c2i} song is set sucessfully ! ")
                except:
                    print("error in prevous mode resume key set function !")
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
    elif (choice == "res"):
        stopm()
        sql4 = "select sindex from resume"
        cursor.execute(sql4)
        dup = str(cursor.fetchone())
        print(dup)
        dup = dup[1:2]
        print(dup)
        sql5 = f"select url from songs_table where no = {dup}"
        cursor.execute(sql5)
        udup = str(cursor.fetchone())
        print(udup)
        udup = udup[2:-3]
        print(udup)
        mediaplayer3 = vlc.MediaPlayer()
        media = vlc.Media(udup)
        mediaplayer3.set_media(media)
        media_player.stop()
        mediaplayer3.play()
        print("the song is now playing in resume normal mode")
        while True:
            if (mediaplayer3.is_playing() == 1):
                continue
            elif (mediaplayer3.is_playing() == 0):
                try:
                    sql2 = "DELETE FROM `resume` WHERE no = 1"
                    cursor.execute(sql2)
                    sql3 = f"INSERT INTO `resume`(`no`, `sindex`) VALUES (1,{ioi})"
                    cursor.execute(sql3)
                    print(f"the resume key for the {c2i} song is set sucessfully ! ")
                    continue
                except:
                    print("error in is playing mode resume key set function !")
                break
    elif(choice == "ran"):
        ran_index = random.randint(1,10)
        print(ran_index)
        sql = f"select url from songs_table where no = {ran_index}"
        cursor.execute(sql)
        ran_url0 = str(cursor.fetchone())
        print("the ran url is :",ran_url0)
        ran_url1 = ran_url0[2:-3]
        print(ran_url1)
        media_player4 = vlc.MediaPlayer()
        media = vlc.Media(ran_url1)
        media_player4.set_media(media)
        stopm()
        media_player4.play()
        time.sleep(3)
        while True:
            if (media_player4.is_playing() == 1):
                continue
            elif (media_player4.is_playing() == 0):
                try:
                    sql2 = "DELETE FROM `resume` WHERE no = 1"
                    cursor.execute(sql2)
                    sql3 = f"INSERT INTO `resume`(`no`, `sindex`) VALUES (1,{ran_index})"
                    cursor.execute(sql3)
                    print(f"the resume key for the {c2i} song is set sucessfully ! ")
                except:
                    print("error in random resume key set function !")
                    media_player4.stop()
                break

    elif(choice == "q"):
        sql = "truncate que"
        cursor.execute(sql)
        inp = []
        while 1:
            i = int(input("enter the index of the song that you want to add to the que :"))
            if(i == 0):
                break
            else:
                inp.append(i)
        for queindex in inp:
            sql2 = f"select url from songs_table where no={queindex}"
            cursor.execute(sql2)
            queurl0 = str(cursor.fetchone())
            print(queurl0)
            queurl1 = queurl0[2:-3]
            print(queurl1)
            media_player5 = vlc.MediaPlayer()
            media = vlc.Media(queurl1)
            media_player5.set_media(media)
            stopm()
            media_player5.play()
            time.sleep(2)
            d = str(media.get_duration())
            print(d)
            sd = d[0:3]
            print(queurl1," is Playing Now And It's duration is :", sd, "Seconds")
            isd = int(sd)
            time.sleep(isd)

    elif(choice == "pl"):
        playlist = input("enter the name of the playlist :")
        sql = f"create table {playlist} (pindex integer not null unique)"
        cursor.execute(sql)
        sql3 = "select * from songs_table"
        cursor.execute(sql3)
        listing = cursor.fetchall()
        for k in listing:
            print(k)
        plinp = []
        while 1 :
            i = int(input(f"enter the index of the song that you want to add to the playlist called {playlist}:"))
            if (i == 0):
                break
            else:
                plinp.append(i)
        for plindex in plinp:
            sql2 = f"select url from songs_table where no={plindex}"
            cursor.execute(sql2)
            plurl0 = str(cursor.fetchone())
            print(plurl0)
            plurl1 = plurl0[2:-3]
            print(plurl1)
            media_player6 = vlc.MediaPlayer()
            media = vlc.Media(plurl1)
            media_player6.set_media(media)
            stopm()
            media_player6.play()
            time.sleep(2)
            d = str(media.get_duration())
            print(d)
            sd = d[0:3]
            print(plurl1," is Playing Now And It's duration is :", sd, "Seconds")
            isd = int(sd)
            time.sleep(isd)

    elif(choice == "sp"):
        spindex = int(input("enter the index of the specific song that you want to play :"))
        while True :
            if(spindex == 0):
                break
            else:
                sql = f"select url from songs_table where no = {spindex}"
                cursor.execute(sql)
                spr = str(cursor.fetchone())
                spcr = spr[2:-3]
                print("the specific song url is :",spcr)
                media_player7 = vlc.MediaPlayer()
                media = vlc.Media(spcr)
                media_player7.set_media(media)
                stopm()
                media_player7.play()
                time.sleep(2)
                d = str(media.get_duration())
                print(d)
                sd = d[0:3]
                print(spcr, " is Playing Now And It's duration is :", sd, "Seconds")
                isd = int(sd)
                time.sleep(isd)
    else:
        print("the else part is running!")
        while True:
            if (media_player.is_playing() == 1):
                continue
            elif (media_player.is_playing() == 0):
                try:
                    sql2 = "DELETE FROM `resume` WHERE no = 1"
                    cursor.execute(sql2)
                    sql3 = f"INSERT INTO `resume`(`no`, `sindex`) VALUES (1,{ioi})"
                    cursor.execute(sql3)

                    877
                    print(f"the resume key for the {c2i} song is set sucessfully ! ")
                except:
                    print("error in else resume key set function !")
                break
            else:
                print("Error Code : SG001")
