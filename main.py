from fastapi import FastAPI
from databeissi import get_connection

app =FastAPI()
@app.get("/mittaukset/{location}/{date}")
def get_mittaukset(location: str, date: str):
           conn= get_connection()
           cursor= conn.cursor()

           query= """
           SELECT arvo,aika
           FROM mittaukset
           WHERE DATE(aika)=%s
           """
           cursor.execute(query,(date,))
           results=cursor.fetchall()
         return results

@app.get("/mittaukset/count/{location}")
def count_mittaukset(location: str):
 conn= get_connection()
 cursor= conn.cursor()
 cursor.execute("SELECT COUNT(*) FROM mittaukset")
 count = cursor.fetchone()[0]
 return {"count":count}

@app.get("/mittaukset/average/{sensori}/{date}")
def average(sensori: str, date: str):
           conn= get_connection()
           cursor= conn.cursor()

           query="""
           SELECT AVG(arvo)
           FROM mittaukset
           WHERE DATE(aika)=%s
           """
          cursor.execute(query,(date,))
          avg=cursor.fetchone()[0]
          return{"average":avg}


