import pymysql
import json
file=open("./config.json","r")
datadic=json.loads(file.read())
file.close()
connect1=pymysql.connect(host="localhost",user="root",passwd="python",database="test")
print(connect1)