from time import time
import mysql.connector

import credentials

db = mysql.connector.connect(
    host="localhost",
    user=credentials.db_user,
    password=credentials.db_pass,
    database=credentials.db_name)
cursor = db.cursor()

file = open("title_crew.tsv", 'r')
file.readline()  # read first line and does nothing with it
start = time()
for line in file:
    dataArr = line.strip().split('\t')
    for director in dataArr[1].split(','):
        if (director == "\\N"):
            continue
        cursor.execute(
            f'INSERT INTO title_directors VALUES ("{dataArr[0]}","{director}");')
    for writer in dataArr[2].split(','):
        if (writer == "\\N"):
            continue
        cursor.execute(
            f'INSERT INTO title_writers VALUES ("{dataArr[0]}","{writer}");')

file.close()
db.commit()

finish = time()
print(f"Took {finish-start} seconds to complete")

