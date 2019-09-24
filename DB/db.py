# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('clientes.db')
# definindo um cursor

# print(conn)

cursor = conn.cursor()

# cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='projects' ''')

# if cursor.fetchone()[0]==1: 
#     print('Table exists.')
# else:
#     print('Table does not exists.')

cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id integer PRIMARY KEY,
        name text NOT NULL,
        begin_date text,
        end_date text
    ); 
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integer,
        status_id integer NOT NULL,
        project_id integer NOT NULL,
        begin_date text NOT NULL,
        end_date text NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );
""")

# print('Tabela criada com sucesso.')
# # desconectando...
# conn.close()

# sqlite_insert_query = """
#     INSERT INTO `projects`
#         ('name', 'begin_date', 'end_date')  
#         VALUES  
#         ('LEO','29','30')"""

# count = cursor.execute(sqlite_insert_query)
# conn.commit()
# print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)


sqlite_insert_query = """
    INSERT INTO `tasks`
        ('name', 'priority', 'status_id','project_id','begin_date','end_date')  
        VALUES  
        ('Teste',2,1,1,'98','85')"""

count = cursor.execute(sqlite_insert_query)
conn.commit()
print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)





cursor.close()