import sqlite3
import os

try: 
    connection = sqlite3.connect(os.environ["DB_FILENAME"])
except:
    connection = sqlite3.connect("visitedthreads.db")
cur = connection.cursor()

def setup():
    cur.execute("""CREATE TABLE IF NOT EXISTS visited_threads (id text)""")

def add(thread_id):
    cur.execute("""INSERT INTO visited_threads VALUES (?)""", (thread_id,))

def check(thread_id):
    cur.execute("""SELECT * FROM visited_threads WHERE id=:tid""", {"tid": thread_id})
    return len(cur.fetchall()) > 0

def commit():
    connection.commit()

def close():
    connection.close()

if __name__=="__main__":
    setup()
    print check("asdf")
    add("asdf")
    print check("asdf")
    commit()
    close()

