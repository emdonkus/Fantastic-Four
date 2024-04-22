'''
Author: Lex Bukowski
Date: April 22, 2024
Usage: Clears the database of all tables and information stored

'''


import os
import psycopg2

conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')

cur = conn.cursor()

#Clean up for re-init
cur.execute('DROP TABLE IF EXISTS ingredients')
cur.execute('DROP TABLE IF EXISTS instructions')
cur.execute('DROP TABLE IF EXISTS recipe')



conn.commit()
cur.close()
conn.close()