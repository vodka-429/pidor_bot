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


def pidorstats():
    res = []
    db = connect()

    for line in db.pidors.find():
        login = line.get('login')
        count = line.get('count', 0)
        res.append((login, count))

    return res


def set_count(login, count):
    count = int(count)
    db = connect()

    db.pidors.replace_one({"login": login}, {"count": count}, upsert=True)


def add_one(login):
    db = connect()

    lines = db.pidors.find({"login": login})
    if len(lines) == 1:
        for line in lines:
            count = line["count"]
            count += 1
            db.pidors.replace_one({"login": login}, {"count": count}, upsert=True)
