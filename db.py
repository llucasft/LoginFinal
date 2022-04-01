import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="all_data",
    user="postgres",
    password="postgres")

cursor = conn.cursor()
conn.commit()


def close_conn():
    conn.close()


def get_user(nick):
    cursor.execute(f"select * from usuarios where nick = '{nick}'")
    row = cursor.fetchone()

    return row


def insert(user_name, user_nick, user_password):
    cursor.execute(f"INSERT INTO usuarios(nome, nick, senha) VALUES ('{user_name}', '{user_nick}', '{user_password}')")
    conn.commit()
