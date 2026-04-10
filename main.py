from fastapi import FastAPI
from datetime import date
from databeissi import get_connection

app =FastAPI()

@app.get("/count")
def count_mittaukset():
           conn= get_connection()
           cursor= conn.cursor()

           query = """
           SELECT COUNT(*) 
           FROM mittaukset 
           
           """
           cursor.execute(query)
           result=cursor.fetchone()
           
           cursor.close()
           conn.close()
           return {"count":result[0]if result else 0}

@app.get("/average/{sensori}/{date}")
def average(sensori: int, date: date):
           conn= get_connection()
           cursor= conn.cursor()

           query="""
           SELECT AVG(arvo)
           FROM mittaukset 
           WHERE sensoriID = %s
           AND aika >= %s
           AND aika < DATE_ADD(%s, INTERVAL 1 DAY)
           """
           cursor.execute(query,(sensori, date, date))
           result=cursor.fetchone()
           if result is None or result[0] is None:
                   avg=None
           else:
                   avg=float(result[0])
           cursor.close()
           conn.close()
           return{"average":avg}

@app.get("/date/{date}")
def get_mittaukset(date: str):
           conn= get_connection()
           cursor= conn.cursor()

           query= """
           SELECT arvo,aika
           FROM mittaukset
          
           WHERE DATE(aika)=%s
           """
           cursor.execute(query,(date,))

           rows=cursor.fetchall()
           cursor.close()
           conn.close()
           return [
                   {"arvo": r[0], "aika": r[1]}
                   for r in rows
           ]


