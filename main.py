import time
import requests



def Price_XRP():
    url = "https://api.binance.com/api/v3/ticker/price"
    data = requests.get(url)
    data.raise_for_status()
    data_1 = data.json()
    st = (next(x for x in data_1 if x["symbol"] == "XRPUSDT"))
    price_1 = (st.get('price'))
    sp = []
    sp.append(price_1)
    cr = float(sp[0])
    return cr


def time_l():
    tic = time.perf_counter()
    return tic


def Price_Difference(PriceStart):
    r = ((PriceStart - Price_XRP()) / PriceStart) * 100
    return r


while True:
    start = time_l()
    price = 0
    while (time_l() - start) <= 3599 :
        time.sleep(0.1)

        if price <= Price_XRP():
            price = Price_XRP()
        print(time_l())
        print(price)
        print(Price_Difference(price))
        if abs(Price_Difference(price)) >= 1:
            print("цена упала!!!")