from time import time
import mysql.connector

import credentials

db = mysql.connector.connect(
    host="localhost",
    user=credentials.db_user,
    password=credentials.db_pass,
    database=credentials.db_name)
cursor = db.cursor()

file = open("title_ratings.tsv", 'r')
file.readline()  # read first line and does nothing with it
start = time()
for line in file:
    dataArr = line.strip().split('\t')
    cursor.execute(
        f'INSERT INTO title_ratings VALUES ("{dataArr[0]}",{dataArr[1]},{dataArr[2]});')

file.close()
db.commit()

finish = time()
print(f"Took {finish-start} seconds to complete")
