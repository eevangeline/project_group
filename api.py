import json
import requests
url = url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=K3O1IE4SNE9OS01J'
r = requests.get(url)
response = r.json()
exchange_rate = float(response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
statement = f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exchange_rate}"
print(statement)