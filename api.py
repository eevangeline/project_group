import json
import requests
url = url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=K3O1IE4SNE9OS01J'
r = requests.get(url)
#extracting full data from web ap
response = r.json()
#sorting out data by extracting on exchange rate using keywords
#converting data into float for currency conversion later on
exchange_rate = float(response["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
#creating statement for use when writing summary report
statement = f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exchange_rate}"