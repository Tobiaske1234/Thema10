import pymssql
import time

conn = pymssql.connect(host='reathema10.database.windows.net', port=1433,
database='Thema10', user='kw1c@reathema10.database.windows.net', password='P@ssword')

import RPi.GPIO as GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    if GPIO.input(10) == GPIO.HIGH:
        cur = conn.cursor()
        timestamp = int( time.time() )
        cur.execute("INSERT INTO Oefening21 VALUES('Button', 'Pressed', " + str(timestamp) +")")
        print("Je klik is verstuurd naar de database met timestamp " + str(timestamp))
        conn.commit()
        time.sleep(2)
        
 
conn.close()


"""
conn = pymssql.connect(host='reathema10.database.windows.net', port=1433,
database='Thema10', user='kw1c@reathema10.database.windows.net', password='P@ssword')

cursor = conn.cursor()
cursor.execute('SELECT * FROM tafel;')
row = cursor.fetchone()
while row:
    #Doe iets met deze rows
    print(str(row[0]) + str(row[1]) )
    row = cursor.fetchone()

conn.commit()
conn.close()
"""