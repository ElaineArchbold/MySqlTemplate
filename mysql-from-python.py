import os
import pymysql

# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        list_of_names = ['jim', 'bob']
        cursor.execute("DELETE FROM Friends WHERE name in (%s,%s)", names)
        connection.commit()
finally:
    connection.close()
