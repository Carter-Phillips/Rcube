from userDB import DBClass
from datetime import datetime
from VideoCreate import CreateVid
from tinydb import TinyDB, Query, where


date=datetime.today().strftime('%Y-%m-%d')

#db = DBClass()
#db.updatenormDB('TheFlightlessPenguin', 'adress1')
#db.updateDBD('TheFlightlessPenguin', 'adress1', date)



vider = CreateVid(date)
vider.makeVid()

