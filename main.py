from fastapi import FastAPI
from databeissi import get_connection

app =FastAPI()
@app.get("/mittaukset/{location}/{date}")
def get_mittaukset(location: str, date: str):
           conn= get_connection()
           cursor= conn.cursor()

           query= """
           SELECT arvo,aika
           FROM mittaukset m
           JOIN sensori s ON m.sensoriID = s.ID
           Join mittauspaikka mp ON s.MittauspaikkaID = mp.id
           Where mp.id = %s
           WHERE DATE(aika)=%s
           """
           cursor.execute(query,(date,))
           results=cursor.fetchall()
         return results

@app.get("/mittaukset/count/{location}")
def count_mittaukset(location: str):
 conn= get_connection()
 cursor= conn.cursor()

           query = """
           SELECT COUNT(*) FROM mittaukset m
           Join sensori s ON m.sensoriID = s.ID
           WHERE s.MittauspaikkaID = %s
           """
 cursor.execute(query, (location,))
 count = cursor.fetchone()[0]
 return {"count":count}

@app.get("/mittaukset/average/{sensori}/{date}")
def average(sensori: str, date: str):
           conn= get_connection()
           cursor= conn.cursor()

           query="""
           SELECT AVG(arvo)
           FROM mittaukset m
           JOIN sensori s ON m.sensoriID = s.ID
           WHERE s.MittauspaikkaID = s.ID
           AND s.ID = %s
           AND DATE(aika)=%s
           """
          cursor.execute(query,(date,))
          avg=cursor.fetchone()[0]
          return{"average":avg}


