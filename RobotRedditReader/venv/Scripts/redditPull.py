import webbrowser
import praw
import re
from gtts import gTTS
import pygame
import pdfkit
from datetime import datetime, timedelta
from imageCompile import mainClass
from TitlePic import TitlePic
from userDB import DBClass
from VideoCreate import CreateVid
from praw.models import Message
import os
import shutil


                            #initialising variables

x=0
usedComments=[]
finalComments=[]
userNames=[]
userAgent="Rcube reddit bot 1.0 by /u/Cthulhus_Cuck"
date=datetime.today().strftime('%Y-%m-%d')
postauthor = ''

                            #connect to reddit

reddit = praw.Reddit(client_id='EpM-tm-knvhoNQ',
                     client_secret='Rl8lhuns5hJGE5fv1wpxrPn6Xww',
                     user_agent=userAgent,
                     username = 'Rcube_Bot',
                     password = 'm6K3KA3jybH07SRivw#hi*ldH4z8ykBKBc233*NwWVM4h*1$FRr5$rxImzRXOUOwg3JGtS^g1QBiYycLsP8EejKGmR3OHvHDu2T')

                            #read submissionsd and store
print("\n\n\nCollecting comments", end ='')

for submission in reddit.subreddit('askreddit').top(time_filter='day', limit=1):
    submission.comment_sort='top'
    vidTitle=submission.title
    postauthor = str(submission.author)
    topComments = list(submission.comments)


sfound = postauthor.lower().find('(serious)')

if sfound != -1:
    postauthor = postauthor[:-(len(st) - placefound)]


try:
    os.mkdir(date)#make the day's directory
except WindowsError:
    shutil.rmtree(date)
    os.mkdir(date)

print("     DONE")
print('\nRemoving links',end='')

for com in topComments:
    print('.', end ='')
    if(com.author != None and com.author != 'AutoModerator'):
        comment = com.body
        userName = com.author.name
        comment.lower()
        if comment.find('http')==-1:
            usedComments.append(com.body)
            userNames.append(userName)
            x+=1
            if x>15:
                break

print("DONE")
print('\nRemoving edits',end='')
                            #comments selected
x=0

for st in usedComments:
    print('.', end ='')
    comment = st.lower()
    placefound= comment.find('edit')
    x+=1
    if placefound > -1:
        st = st[:-(len(st)-placefound)]
        finalComments.append(st + "         \n \n \n")
    else:
        finalComments.append(st+"           \n\n\n")

print("DONE")
print('\nMaking audio and saving images...', end='')

pygame.init()
pygame.mixer.init()

stringread = gTTS(text=vidTitle, lang='en', slow=False)
stringread.save(date + '/' + 'title.mp3')
x=0
for st in finalComments:
    print('.', end='')
    stringread = gTTS(text=st, lang='en', slow=False)
    stringread.save(date + '/' + userNames[x] +".mp3")
    imager = mainClass(st, userNames[x], vidTitle, date)
    imager.makepic()
    imager = TitlePic(vidTitle,date,postauthor)
    x+=1

imager.makePic()
print("DONE\n")

print('UPDATING DATABASE')

db = DBClass()
db.updateDB(userNames)
db.dayDB(userNames, date)
db.updateoneDB(postauthor)
query = db.queryDB('user' == postauthor)
f = open(date + '/OP.txt', 'a')
f.write(postauthor)

print('\nDONE')

print('\n\nChecking messages...')
usersused = []
for item in reddit.inbox.unread(limit = None):
    print(item)
    curword = ''
    words = item.body.split()

    if item.author not in usersused:  ##This disgusting mess of code responds to peoples messagse and updates the database
        for word in words:
            if '@' in word:
                curword = word
            elif 'stop' in word.lower():
                curword = word
            elif 'permission' in word.lower():
                curword = word

        if curword == '':
            item.author.message('Incorrect email', 'Your response did not contain an email, please respond with an email or you will be excluded from the video, or respond with \"permission\" if you would like to be in the video but do not have a paypal address\n\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                                                                                        '**Please message /u/Cthulhus_Cuck with any concerns.', from_subreddit=None)
            db.updatenormDB(str(item.author), 'stop')
        else:
            db.updatenormDB(str(item.author), curword.lower())
            if curword.lower() == 'permission':
                item.author.message('Thank you.',
                                    'Thank you,\nYou will be included in future videos but will not be paid, if you would like to add a paypal email message it to me at any time\n\nThank you!\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                                                                                        '**Please message /u/Cthulhus_Cuck with any concerns.',
                                    from_subreddit=None)
            elif curword.lower() != 'stop':
                item.author.message('Thank you.',
                                    'Thank you for responding!\nYour address is currently set to \"' + curword.lower() + '\"\nIf you would like to change your address at any time, please message me at any time with the new adress.\n\nIf you would no longer like to be included in videos,'
                                                                                                                        ' please respond with \"stop\"\n\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                                                                                        '**Please message /u/Cthulhus_Cuck with any concerns.',
                                    from_subreddit=None)
            else:
                item.author.message('Cancelled',
                                    'You have removed permissions for RCube. Reply with a paypal address at any time to re-join\n\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                                                                                        '**Please message /u/Cthulhus_Cuck with any concerns.',
                                    from_subreddit=None)
    item.mark_read()
    usersused.append(item.author)
    ##############################CHANGE THE NAME TO THE AUTHOR NAME
    praw.models.Redditor(self.reddit, name='Rcube_Bot', _data=None).message('RCube Video',
                        'Your recent post in r/AskReddit has been selected for a video, if you would like some of the profits please respond with a paypal email address.'
                        '\n\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                        '**Please message /u/Cthulhus_Cuck with any concerns.',
                        from_subreddit=None)

print('\nDONE')

print('\n\nCREATING VIDEO')

try:
    vidmake = CreateVid((datetime.today() - timedelta(days = 5).strftime('%Y-%m-%d')))
except:
    print("no folder for that day")

print('DONE')

print('\n\nTITLE: ' + vidTitle)

answer = input('\nOPEN THE POST? (Y/N): ')
if answer == 'y' or answer == 'Y':
    webbrowser.open_new_tab(submission.url)

print('\n\nPROGRAM FINISHED, TERMINATING')
