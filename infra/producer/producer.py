import time
import json
import requests
from kafka import KafkaProducer

#defibe variable

API_kEY = "d6th6i9r01qhkb446jk0d6th6i9r01qhkb446jkg"
BASE_URL = "https://finnhub.io/api/v1/quote"
SYMBOLS = ["AAPL","MSFT","TSLA","GOOGL","AMZN"]

#iniiitialize producer
producer = KafkaProducer(
    bootstrap_servers = ["host.docker.internal:29092"],
    value_serializer = lambda v: json.dumps(v).encode("utf-8")
)

#retrive data
def fetch_quote(symbol):
    url = f"{BASE_URL}?symbol={symbol}&token={API_kEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        data["symbol"] = symbol
        data["fetched_at"] = int(time.time())
        return data 
    except Exception as e:
        print(f"Error fetching {symbol} : {e}")
        return None
    
#stream(push to kafka)
while True:
    for symbol in SYMBOLS:
        quote = fetch_quote(symbol)
        if quote:
            print(f"Producing:{quote}")
            producer.send("stock-quotes",value = quote)
    time.sleep(6)
