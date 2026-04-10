Tässä sovellus joka käyttää REST API rajapintaa (Fast API) open air quality datan hakuun tietokannasta. 

Kolme vaadittua endpointia löytyy. 
Sovelluksella pystyy laskemaan kaikkien sijainnin (Helsinki) mittausten määrän, laskemaan sensorin mittausten keskiarvon tietyltä päivältä ja näkemään kaikki tietyn päivän mittaukset

Käyttäminen:
1. Cloonaa repositorio
2. Asenna Dependencies
3. mene projektikansioon ja starttaa FastAPI serveri Uvicornilla (komento joka toimii: python -m uvicorn main:app --reload)
4. API tulee näkyviin http://localhost:8000

Endpointien käyttö:
Count mittaukset: Klikkaa "try it out"
Average: laita parametreiksi joku sensori id (6306, 6403, 27740, 2002989) ja date= 2023-01-dd (data on haettu 1 kuukauden ajalta)
Get mittaukset: parametriksi date= 2023-01-dd



