import sqlite3

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

