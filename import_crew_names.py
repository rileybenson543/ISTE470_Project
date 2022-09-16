from time import time
import mysql.connector

import credentials

start = time()

db = mysql.connector.connect(
    host="localhost",
    user=credentials.db_user,
    password=credentials.db_pass,
    database=credentials.db_name)
cursor = db.cursor()

professions = {"writer", "director"}

file = open("crew_names.tsv", 'r', encoding='utf-8')
file.readline()  # read first line and does nothing with it
for line in file:
    dataArr = line.strip().split('\t')
    if (professions.intersection(set(dataArr[4].split(',')))):
        if (dataArr[2] == "\\N"):
            dataArr[2] = "NULL"
        if (dataArr[3] == "\\N"):
            dataArr[3] = "NULL"
        # escapes quotation marks
        dataArr[1].replace("'", r"\'")
        dataArr[1].replace('"', r"\"")
        try:
            cursor.execute(
                f'INSERT INTO crew_names VALUES ("{dataArr[0]}","{dataArr[1]}",{dataArr[2]},{dataArr[3]});')
        except Exception as e:
            print(f"Failure to add record {dataArr[0]} with exception:")
            print(e)
    else:
        continue

file.close()
db.commit()

finish = time()
print(f"Took {finish-start} seconds to complete")
