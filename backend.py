import sqlite3

from datetime import date
today=date.today()

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not EXISTS books (id integer primary key ,book text,teacher text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert1(book,teacher,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "insert into books values (null,?,?,?,?)",(book,teacher,year,isbn))
    conn.commit()
    conn.close()

def check1():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select book,teacher,year,isbn,count(*)as cnt from books group by book,teacher,year,isbn having count(*)>1")
    rows=cur.fetchall()
    conn.close()
    return rows


def deleteRuw1():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from books where ID not in(select max(ID)as MaxRecordID from books group by book,teacher,year,isbn)")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def viewall1():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from books ")
    rows=cur.fetchall()
    conn.close()
    return rows

def search1(book="",teacher="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from books where book=? or teacher=? or year=? or isbn=?  ",(book,teacher,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def update1(id,book,teacher,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute( "update books set book=?,teacher=?,year=?,isbn=? where id=?",(book,teacher,year,isbn,id))
    conn.commit()
    conn.close()

def delete1(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from books where id=?",(id,))
    conn.commit()
    conn.close()

def deleteEmptyRows():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE book=='___' and teacher=='___' and year=='___' and isbn=='___' " )
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
connect()

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not EXISTS members (id integer primary key ,name text,family text,birth integer,code integer)")
    conn.commit()
    conn.close()

def insert2(name,family,birth,code):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into members values (null,?,?,?,?)",(name,family,birth,code))
    conn.commit()
    conn.close()
def check2():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select name,family,birth,code,count(*)as cnt from members group by name,family,birth,code having count(*)>1")
    rows=cur.fetchall()
    conn.close()
    return rows


def deleteRuw2():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from members where ID not in(select max(ID)as MaxRecordID from members group by name,family,birth,code)")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def viewall2():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from members ")
    rows=cur.fetchall()
    conn.close()
    return rows

def search2(name="",family="",birth="",code=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from members where name=? or family=? or birth=? or code=?",(name,family,birth,code))
    rows = cur.fetchall()
    conn.close()
    return rows

def update2(id,name,family,birth,code):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute( "update members set name=?,family=?,birth=?,code=? where id=?",(name,family,birth,code,id))
    conn.commit()
    conn.close()

def delete2(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from members where id=?",(id,))
    conn.commit()
    conn.close()
def deleteEmptyRows1():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM members WHERE name=='___' and family=='___' and birth=='___' and code=='___' " )
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
connect()

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not EXISTS management (id integer primary key ,name text,family text,tahsilat text)")
    conn.commit()
    conn.close()

def insert3(name,family,tahsilat):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "insert into management values (null,?,?,?)",(name,family,tahsilat))
    conn.commit()
    conn.close()

def check3():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select name,family,tahsilat,count(*)as cnt from management group by name,family,tahsilat having count(*)>1")
    rows=cur.fetchall()
    conn.close()
    return rows


def deleteRuw3():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from management where ID not in(select max(ID)as MaxRecordID from management group by name,family,tahsilat)")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def viewall3():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from management ")
    rows=cur.fetchall()
    conn.close()
    return rows

def search3(name="",family="",tahsilat=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(
        "select * from management where name=? or family=? or tahsilat=?",(name,family,tahsilat))
    rows = cur.fetchall()
    conn.close()
    return rows

def update3(id,name,family,tahsilat):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute( "update management set name=?,family=?,tahsilat=? where id=?",(name,family,tahsilat,id))
    conn.commit()
    conn.close()

def delete3(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from management where id=?",(id,))
    conn.commit()
    conn.close()

def deleteEmptyRows2():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM management WHERE name=='___' and family=='___' and tahsilat=='___' " )
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
connect()

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not EXISTS ReservBooks (id integer primary key ,nameBook text,bookId integer,ExpireTime integer)")
    conn.commit()
    conn.close()

def insert4(nameBook,bookId,Expiretime):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute(" insert into ReservBooks values (null,?,?,?) ",(nameBook,bookId,Expiretime))
    conn.commit()
    conn.close()

def check():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select nameBook,bookId,ExpireTime,count(*)as cnt from Reservbooks group by nameBook,bookId,ExpireTime having count(*)>1")
    rows=cur.fetchall()
    conn.close()
    return rows


def deleteRuw():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from ReservBooks where ID not in(select max(ID)as MaxRecordID from ReservBooks group by nameBook,bookId,ExpireTime)")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()