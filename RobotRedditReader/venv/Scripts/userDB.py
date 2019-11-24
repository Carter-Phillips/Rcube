from tinydb import TinyDB, Query, where

import praw

class DBClass:

    def __init__(self):
        userAgent = "Rcube reddit bot 1.0 by /u/Cthulhus_Cuck"

        self.reddit = praw.Reddit(client_id='EpM-tm-knvhoNQ',
                     client_secret='Rl8lhuns5hJGE5fv1wpxrPn6Xww',
                     user_agent=userAgent,
                     username = 'Rcube_Bot',
                     password = 'm6K3KA3jybH07SRivw#hi*ldH4z8ykBKBc233*NwWVM4h*1$FRr5$rxImzRXOUOwg3JGtS^g1QBiYycLsP8EejKGmR3OHvHDu2T')

    def updateDB(self, userlist):
        db = TinyDB('UserDB.json')
        for user in userlist:
            x = db.search(where('user') == user )
            if x==[]:
                print("USER ADDED")
                db.insert({'user': user, 'permission': 'stop'})
                praw.models.Redditor(self.reddit, name='Rcube_Bot', _data=None).message('Rcube Request', 'Hello!\n I am contacting you as you have recently made one of the top comments in an askreddit thread.  '
                                                                                                  'I am a bot who scrapes that sub every day and attemps to make youtube videos out of it.\n\n I know that '
                                                                                                  'these reddit videos are despised in the community, and that is why I have come to it with a new idea: A portion '
                                                                                                  'of the video profits will be re-destributed to the members that made the posts!\n\n All I need from you is that you reply '
                                                                                                  'with a paypal email, and in about a month 40% of the profits will be split between the accepting commenters and the OP.\n\n'
                                                                                                  'If you would like to be included but do not have a paypal email, please respond with \"permission\" and you can update to an email anytime with another message'
                                                                                                  'If you do not want to be in the video please ignore this and you will not be included.\n\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                                                                                                  '**Please message /u/Cthulhus_Cuck with any concerns.', from_subreddit=None)
            else:
                praw.models.Redditor(self.reddit, name='Rcube_Bot', _data=None).message('Rcube Selection',
                                                                                        'Hello! You have been selected for another video,\nCongrats!\n\n'
                                                                                        'If you are still alright being in the video, you can safely ignore this message, however'
                                                                                        'if you would not like to be in the video, please reply \"stop\"\n\n'
                                                                                        'If you would like to be included but do not have a paypal email, please respond with \"permission\" and you can update to an email anytime with another message'
                                                                                        '\n\n[You can find our youtube here](https://www.youtube.com/channel/UCzhQGpM1rv5Yx4I9pu1XjcQ)\n\n'
                                                                                        '**Please message /u/Cthulhus_Cuck with any concerns.',
                                                                                        from_subreddit=None)
                print('USER EXISTS')

    def updateoneDB(self, user):
        db = TinyDB('UserDB.json')
        x = db.search(where('user') == user)
        if x == []:
            print("USER ADDED")
            db.insert({'user': user, 'permission': 'stop'})
        else:
            print('USER EXISTS')

    def dayDB(self, userlist, date):
        ddb = TinyDB(date + '/' + 'DayDB.json')
        db = TinyDB('UserDB.json')
        for user in userlist:
            x=db.search(where('user') == user)
            y=db.get(where('user') == user )
            if x == []:
                ddb.insert({'user': user, 'permission': 'stop'})
            else:
                ddb.insert({'user': y['user'], 'permission': y['permission']})

    def purge(self):
        db = TinyDB('UserDB.json')
        db.purge()

    def updatenormDB(self, user, address):
        db = TinyDB('UserDB.json')
        db.remove(where('user') == user)
        db.insert({'user': user, 'permission': address})

    def updateDBD(self, user, address, date):
        ddb = TinyDB(date + '/' + 'DayDB.json')
        db = TinyDB('UserDB.json')
        db.remove(where('user') == user)
        ddb.remove(where('user') == user)
        db.insert({'user': user, 'permission': address})
        ddb.insert({'user': user, 'permission': address})

    def queryDB(self, query):
        db = TinyDB('UserDB.json')
        return(db.search(where(query)))
