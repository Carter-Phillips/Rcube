from mutagen.mp3 import MP3
from tinydb import TinyDB, Query, where
import math
from ffmpeg import concat
import os
import subprocess
import shutil
from userDB import DBClass


class CreateVid:

    def __init__(self, date):

        self.date = date
        self.dbd = TinyDB('UserDB.json')
        self.db = TinyDB(date + '/' + 'DayDB.json')

    def makeVid(self):
        usersAg = []
        users = []
        mpTimes = []
        imgNames = []
        audNames = []
        dbq = DBClass()
        users = self.db.all()
        dbd = TinyDB('UserDB.json')
        for user in users:
            query = dbd.search(where('user') != user['user'])
            qn = query[0]['user']
            qp = query[0]['permission']
            dbq.updateDBD(qn, qp, self.date)

        for user in users:
                    ################################################change here for test
            if(user['permission'] == 'stop'):
                usersAg.append(user['user'])

        for user in usersAg:
            mpTimes.append(math.ceil(MP3(self.date + '/' + user + '.mp3').info.length))
            imgNames.append(user + '.png')
            audNames.append(user + '.mp3')

        titleLen = math.ceil(MP3(self.date + '/title.mp3').info.length)

        f = open(self.date + '/vid.txt', "a")
        os.chdir(self.date)
        x=0
        for user in usersAg:
            os.system('ffmpeg -y -i ' + audNames[x] + ' -filter:a "atempo=2.0" -vn ' + audNames[x])
            x+=1

        x=0



        print(os.getcwd())
        for user in usersAg:
            os.system('ffmpeg -y -i ' + str(imgNames[x]) + ' -i ' + str(audNames[x]) + ' -c copy ' + str(x+1) + '.avi')
            os.system('ffmpeg -y -i titlepic.png -i title.mp3 -c copy 0.avi')
            f.write('file \'' + str(x) + '.avi\'\n')
            x+=1

        f.close()
        os.system('ffmpeg -y -f concat -safe 0 -i vid.txt -max_muxing_queue_size 1024 -c copy C:/Rcubetemp/vidout.avi')
        os.remove('vid.txt')