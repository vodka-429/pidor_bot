import os
import pymongo

# TODO: просто чтобы потестить подключение. Нужно будет переделать


def connect():
    url = os.environ['MONGO_URL']
    db = pymongo.MongoClient(url, tls=False)['pidor']
    return db


def check():
    db = connect()

    ignore = []
    for line in db.tmp.find():
        ignore.append(line['login'])

    return ignore
