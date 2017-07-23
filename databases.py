# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:29:10 2017

@author: Naruto_kathi
"""

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Kathi(userName TEXT, password TEXT, date TEXT)")

def insert_data():
    c.execute("INSERT INTO Kathi VALUES('kathi747','ihtak', '09-07-2017')")
    conn.commit()
    c.close()
    conn.close()

create_table()
insert_data()