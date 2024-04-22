from flask import Flask, render_template, request, url_for, redirect
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')
    return conn

@app.route('/')
def index():
    return '<h1>Index Page</h1>'

@app.route('/ingredients', methods=('GET','POST'))
def ingredients():
    if request.method =='GET':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
                    SELECT *
                    FROM ingredients;
                    ''')
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    
@app.route('/instructions', methods=('GET','POST'))
def instructions():
    if request.method == 'GET':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
                    SELECT *
                    FROM instructions;
                    ''')
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data