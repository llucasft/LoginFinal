import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="all_data",
    user="postgres",
    password="postgres")

cursor = conn.cursor()

conn.commit()


def mod_verifier(nick):
    string_sql = f"""
        select exists
        (select * from usuarios where nick = '{nick}')' ;
    """

    cursor.execute(string_sql)
    row = cursor.fetchone()
    return row


def insert(a, b, c):
    add_user = f"""INSERT INTO usuarios(nome, nick, senha)
        VALUES ('{a}', '{b}', '{c}')"""

    cursor.execute(add_user)
    conn.commit()
