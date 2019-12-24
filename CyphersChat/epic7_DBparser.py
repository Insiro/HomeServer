import sqlite3
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
# API Documents : https://epicsevendb-apiserver.herokuapp.com/

def parse():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    url = "https://api.epicsevendb.com/api/hero"
    req = requests.get(url)
    json = req.json()
    cur.execute("SELECT count(SearchKey) from epic7_heros")
    for c in cur:
        count = c[0]
    for hero in json['results']:
        _id = "'"+hero['_id']+"'"
        cur.execute("SELECT count(SearchKey) from epic7_heros where SearchKey="+_id)
        for c in cur:
            temp_c = c[0]
        if temp_c == 0:
            cur.execute("SELECT * from epic7_heros where SearchKey="+_id)
            count = count+1
            query = "INSERT into epic7_heros values ( " + str(count)+", "+_id+", '" + hero['name']+"' ,"
            query = query + str(hero['rarity'])+", '" + hero['classType']+"', '"+hero['element']+"' ) "
            print("new data : "+_id)
            cur.execute(query)
    cur.close()
    con.commit()
    con.close()

if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(parse, 'cron',week='fri', hour='3')
    sched.start()
