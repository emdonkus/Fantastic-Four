import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="3308TermProject",
    user="postgres",
    password="")

cur = conn.cursor()

# Create new table
cur.execute('DROP TABLE IF EXISTS ingredients;')
cur.execute('CREATE TABLE ingredients (id serial PRIMARY KEY,'
                                       'name varchar(150) NOT NULL);'
            )

# Add data to the table
cur.execute('''INSERT INTO ingredients (id, name)
            VALUES
            (1,'Chicken'),
            (2,'Waffles');            
            ''')

conn.commit()
cur.close()
conn.close()