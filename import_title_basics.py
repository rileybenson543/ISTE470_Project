from time import time
import mysql.connector

import credentials

db = mysql.connector.connect(
    host="localhost",
    user=credentials.db_user,
    password=credentials.db_pass,
    database=credentials.db_name)
cursor = db.cursor()

file = open("title_basics.tsv", 'r')
file.readline()  # read first line and does nothing with it
start = time()
for line in file:
    dataArr = line.strip().split('\t')
    if (dataArr[1] == "movie"):
        try:
            cursor.execute(
                f'UPDATE title_ratings SET genre = "{dataArr[8]}", titleName = "{dataArr[2]}" WHERE tconst = "{dataArr[0]}"')
        except Exception as e:
            print(dataArr)
            print(e)

file.close()
db.commit()

finish = time()
print(f"Took {finish-start} seconds to complete")


