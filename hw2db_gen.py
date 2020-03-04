import hashlib
import sqlite3
import inflect
import time

conn = sqlite3.connect('hw2.db')
cur = conn.cursor()
f = open('pw.txt', 'r')
all_lines = f.readlines()
p = inflect.engine()


def table_init():
    #cur.execute("DROP TABLE passwords;")
    #cur.execute("DROP TABLE other_char;")
    cur.execute("CREATE TABLE IF NOT EXISTS passwords (original TEXT, hash TEXT);")
    cur.execute("CREATE TABLE IF NOT EXISTS other_char (pw TEXT);")
    for i in range(1, 21):
        #cur.execute("DROP TABLE {0}_char;".format(p.number_to_words(i)))
        cur.execute("CREATE TABLE IF NOT EXISTS {0}_char (pw TEXT);".format(p.number_to_words(i)))


def table_fill():
    for i in range(999999):
        this_line = all_lines[i].strip()
        this_hash = hashlib.sha1(str('{0}'.format((all_lines[i].strip()))).encode('utf-8')).hexdigest()
        cur.execute("INSERT INTO passwords (original, hash) VALUES(?,?)", (this_line, this_hash))
        if len(this_line) < 21:
            cur.execute("INSERT INTO {0}_char (pw) VALUES(?);".format(p.number_to_words(len(this_line))), ([this_line]))
        else:
            cur.execute("INSERT INTO other_char (pw) VALUES(?);", ([this_line]))


starttime = time.time()
table_init()
table_fill()
conn.commit()
conn.close()
endtime = time.time()
print(endtime - starttime)
