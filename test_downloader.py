import pandas as pd
import gdax

public_client = gdax.PublicClient()
public_client.get_products()
products = public_client.get_products()

from time import sleep
from datetime import datetime

Ticker = "BTC/USD"

df = pd.DataFrame(columns="Ticker,Time,Bid,Ask".split(","))

for ii in range(10):
    sleep(2)
    nw = pd.datetime.now()
    l1 = public_client.get_product_order_book('BTC-USD', level=1)
    df.loc[ii] = [Ticker,nw,l1["bids"][0][0],l1["asks"][0][0]]

df.to_csv("data/BTC2USD.csv",index=False)