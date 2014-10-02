#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import os
os.system("sudo service postgresql start")

def table(tupls,name):
	con = None
	try:
    		con = psycopg2.connect(database='testdb', user='manu') 
    		cur = con.cursor()  
    		cur.execute("DROP TABLE IF EXISTS %s"%(name))
    		cur.execute("CREATE TABLE %s(Count INT PRIMARY KEY, Word TEXT)"%(name))
    		query = "INSERT INTO %s"%(name)+"(Count,Word) VALUES (%s, %s)"
    		cur.executemany(query, tupls)        
    		con.commit()

	except psycopg2.DatabaseError, e:
    		if con:
        		con.rollback()
    		print 'Error %s' % e    
    		sys.exit(1)
    
	finally:
	    if con:
        	con.close()
