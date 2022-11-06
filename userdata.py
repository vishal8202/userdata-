import requests
import sys
import mysql.connector
import json

try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userinfodb')
except mysql.connector.Error as e:
    sys.exit(e)

mycursor = mydb.cursor()

data = requests.get("https://dummyjson.com/users").text

data_info = json.loads(data)

for i in data_info["users"]:
    
    hair = i['hair']
    chair = hair['color']
    sql = "INSERT INTO `userdata`(`first_name`, `last_name`, `maidenName`, `user_name`, `password`, `birthdate`, `hair`) VALUES (%s,%s,%s,%s,%s,%s,%s)" #('"+i['firstName']+"','"+i['lastName']+"','"+i['maidenName']+"','"+i['username']+"','"+i['password']+"','"+i['birthDate']+"','"+chair+"')"
    data = (i['firstName'],i['lastName'],i['maidenName'],i['username'],i['password'],i['birthDate'],chair)
    mycursor.execute(sql,data)
    mydb.commit()
    print('Inserted')