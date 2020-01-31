#Jacob Olin
#SoftDev
#
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="thedatabase.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
#
#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
doneHeader = False
file = open("static/courses.csv",'r')
#c.execute("DROP TABLE courses")
for line in file:
    i = 0
    if line[i] != ',':
        i += 1
    word1 = line[0:i]
    i += 1
    last = i
    if line[i] != ',':
        i += 1
    word2 = line[last:i]
    word3 = line[i+1:len(line)]
    if doneHeader == False:
        command = "CREATE TABLE courses (word1 TEXT, word2 INTEGER, word3 INTEGER)"
        c.execute(command)
        doneHeader = True
    else:
        command = "INSERT INTO courses VALUES (word1 TEXT, word2 INTEGER, word3 INTEGER)"
        c.execute(command)



command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
