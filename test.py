# coding: utf-8

import ccxt
import pandas as pd
import numpy as np
from pprint import pprint
import time

#各取引所のAPIを取得
cc = ccxt.coincheck()
bf = ccxt.bitflyer()
zaif = ccxt.zaif()
bb = ccxt.bitbank()

#for i in range(0, 3, 1):
        
#各取引所のBTC価格(ticker)を取得
#CC ticker情報
cc_ticker = cc.fetch_ticker("BTC/JPY")
ccask = cc_ticker["ask"]
ccbid = cc_ticker["bid"]

#bf ticker情報
bf_ticker = bf.fetch_ticker("BTC/JPY")
bfask = bf_ticker["ask"]
bfbid = bf_ticker["bid"]

#zaif ticker情報
zaif_ticker = zaif.fetch_ticker("BTC/JPY")
zaifask = zaif_ticker["ask"]
zaifbid = zaif_ticker["bid"]

#bb ticker情報
bb_ticker = bb.fetch_ticker("BTC/JPY")
bbask = bb_ticker["ask"]
bbbid = bb_ticker["bid"]

#print("Coincheck:ask",ccask)
#print("Coincheck:bid",ccbid)
#print("BitFlayer:ask",bfask)
#print("BitFlayer:bid",bfbid)
#print("Zaif:ask",zaifask)
#print("Zaif:bid",zaifbid)
#print("bitbank:ask",bbask)
#print("bitbank:bid",bbbid)



#表のレイアウトを調整する
pd.set_option('display.unicode.east_asian_width', True)

#各取引所の価格表データ
df = pd.DataFrame([ [ccask, ccbid, ccask-ccbid], 
                    [bfask, bfbid, bfask-bfbid],
                    [zaifask, zaifbid, zaifask-zaifbid],
                    [bbask, bbbid, bbask-bbbid]])
df.columns=['売値', '買値', 'スプレッド']
df.index=['CoinCheck', 'BitFlayer', 'zaif','bitbank']

#各取引所の価格表を出力する
print(df)

#一番高く売れる取引所と価格
max = df['買値'].max()
maxind = df['買値'].idxmax()

#一番安く買える取引所と価格
min =df['売値'].min()
minind =df['売値'].idxmin()

#どこで買ってどこで売ればいくらの利益が出るか出力
print('最高値:', maxind,max)
print('最安値:', minind,min)


print(minind,'で買って',maxind,'で売れば',max-min, '円の利益が出ます!/1BTCあたり')
input()
