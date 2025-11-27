import sqlite3
from flask import g

DB_NAME = "main.db"


def init_tables(conn):
    conn.execute("create table if not exists tags (" \
    "tag_id integer primary key autoincrement," \
    "name varchar(127) not null)")

    conn.execute("create table if not exists tasks (" \
    "task_id integer primary key autoincrement ," \
    "name varchar(127) not null," \
    "desc varchar(225) not null," \
    "tag_id integer," \
    "foreign key(tag_id) references tags(tag_id))")

    conn.execute("create table if not exists attachments(" \
    "at_id integer primary key autoincrement, " \
    "name varchar(127) not null," \
    "url varchar(255) not null," \
    "task_id integer," \
    "foreign key(task_id) references tasks(taask_id))")

    conn.commit()


def init_db():
    conn = sqlite3.connect(DB_NAME)
    init_tables(conn)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_NAME)
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def get_all_tags():
    db = get_db()
    return db.execute("select * from tags").fetchall()


def insert_tags(name):
    db = get_db()
    db.execute("insert into tags (name) values (?)", (name,) )
    db.commit()



