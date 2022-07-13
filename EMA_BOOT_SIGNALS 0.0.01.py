from talib.abstract import *
from iqoptionapi.stable_api import IQ_Option
import time
import numpy as np
from talib import SMA
from datetime import datetime
from discord import Webhook, RequestsWebhookAdapter
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
email = input("email:")
password = input("password:")
I_want_money = IQ_Option(email, password)
check = I_want_money.connect()
if check:
    print("connect succsuflly")
else:
    print("connection faild")
goal = input("goal:")
size = 3600
maxdict = 200
I_want_money.start_candles_stream(goal, size, maxdict)
def send_msj(message):
    webhook = Webhook.from_url("https://discord.com/api/webhooks/993496840001560706/cn6mKzNz0S_w_jYwf1cFjhy5tmtxuDxC6Z8h2fHuOJVGu7hjhn0fIx64O7LvVZ5Fis51", adapter=RequestsWebhookAdapter())
    webhook.send(message)
while True:
    candles = I_want_money.get_realtime_candles(goal, size)
    inputs = {
        'open': np.array([]),
        'high': np.array([]),
        'low': np.array([]),
        'close': np.array([]),
        'volume': np.array([])
    }
    for timestamp in list(candles.keys()):
        open = inputs["open"] = np.append(inputs["open"], candles[timestamp]["open"])
        high = inputs["high"] = np.append(inputs["open"], candles[timestamp]["max"])
        low = inputs["low"] = np.append(inputs["open"], candles[timestamp]["min"])
        close = inputs["close"] = np.append(inputs["open"], candles[timestamp]["close"])
        volume = inputs["volume"] = np.append(inputs["open"], candles[timestamp]["volume"])
        real_200 = SMA(close, timeperiod=200)
        real_100 = SMA(close, timeperiod=100)
        real_5 = SMA(close, timeperiod=5)
        rl200 = real_200[-1]
        rl100 = real_100[-1]
        major = high[-1]
        minor = low[-1]
        rl5_1 = real_5[-1]
        rl5_2 = real_5[-2]
        if rl200 <= major and rl200 >= minor:
            if rl100 >= rl200:
                if rl5_1 > rl5_2:
                    print(f"{goal}||{current_time}||byyy")
                    send_msj(f"{goal}|||{current_time}||byy")


        elif rl200 <= major and rl200 >= minor:
            if rl100 <= rl200:
                if rl5_1 < rl5_2:
                    print(f"{goal}||{current_time}||sell")
                    send_msj(f"{goal}||{current_time}||sell")





