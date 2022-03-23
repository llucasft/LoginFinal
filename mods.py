import pyodbc


def connector():
    data_conn = (
        "Driver={SQL Server};"
        "Server=DESKTOP-G90E8IG\SQLSERVER;"
        "Database=all_data;"
        "Trusted_Connection=Yes"
    )

    conn = pyodbc.connect(data_conn)

    cursor = conn.cursor()
    return cursor


def consult():
    cursor = connector()
    search = 


def mod_verifier():
    cursor = connector()
    string_sql = """
        SELECT * FROM usuarios 
        where nick = '{}' ;
    """
    cursor.execute(string_sql)
    lines = cursor.fetchall()
    return lines


def command(a, b, c):
    cursor = connector()

    add_user = f"""INSERT INTO usuarios(nome, nick, senha)
        VALUES ('{a}', '{b}', '{c}')"""

    cursor.execute(add_user)
    cursor.commit()