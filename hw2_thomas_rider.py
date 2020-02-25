import hashlib
import sqlite3
import time


def basic_algorithm():
    starttime = time.time()
    f = open('pw.txt', 'r')
    all_lines = f.readlines()
    for i in range(999999):
        this_line = all_lines[i].strip()
        this_hash = hashlib.sha1(this_line.encode('utf-8')).hexdigest()
        this_line_salt = ('slayer'+this_line)
        this_salted = hashlib.sha1(this_line_salt.encode('utf-8')).hexdigest()
        if this_hash == h1:
            print('p1: ' + this_line)
        if this_hash == h2:
            print('p2:' + this_line)
        if this_hash == h3_1:
            print('salt term: ' + this_line)
        if this_salted == h3:
            print('p3: ' + this_line)
    print(time.time() - starttime)


def db_algorithm():
    starttime = time.time()
    for row in cur.execute("SELECT * FROM passwords WHERE hash = '{0}'".format(h1)):
        print(row)
    for row in cur.execute("SELECT * FROM passwords WHERE hash = '{0}'".format(h2)):
        print(row)
    print(time.time() - starttime, '\n')


def grad_finder(ub1, ub2):
    conn = sqlite3.connect('hw2.db')
    cur = conn.cursor()
    for row in cur.execute("SELECT COUNT(*) FROM ten_char"):
        ub1 = int(row[0])
    for row in cur.execute("SELECT COUNT(*) FROM eleven_char"):
        ub2 = int(row[0])
    for i in range(0, ub1):
        for row in cur.execute("SELECT * FROM ten_char LIMIT 1 OFFSET {0}".format(i)):
            first = row[0]
        for j in range(0, ub2):
            for row in cur.execute("SELECT * FROM eleven_char LIMIT 1 OFFSET {0}".format(j)):
                second = row[0]
                new = first + second
                new_hash = hashlib.sha1(str('{0}'.format(new)).encode('utf-8')).hexdigest()
                if new_hash == h4:
                    return new, new_hash
    conn.close()


if __name__ == '__main__':
    conn = sqlite3.connect('hw2.db')
    cur = conn.cursor()

    h1 = 'b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3'
    h2 = '801cdea58224c921c21fd2b183ff28ffa910ce31'
    h3 = 'ece4bb07f2580ed8b39aa52b7f7f918e43033ea1'
    h3_1 = 'f0744d60dd500c92c0d37c16174cc58d3c4bdd8e'
    h4 = '34302959e138917ce9339c0b30ec50e650ce6b40'

    db_algorithm()
    basic_algorithm()
    conn.close()
    #print(grad_finder())
