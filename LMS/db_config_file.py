# Host: 192.168.0.102
# User: dev_user
# Password: Dev#user123
# DB: dev_db

import mysql.connector

j_host = '192.168.0.102'
j_user = 'dev_user'
j_password = 'Dev#user123'
j_database = 'dev_db'

my_database = mysql.connector.connect(host=j_host, user=j_user, passwd=j_password, database=j_database)

print(my_database)


