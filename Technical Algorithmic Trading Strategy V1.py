#Technical Algorithmic Trading Strategy V1
#Produced by Finn Corbett

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.requests import StockBarsRequest
from datetime import date
from alpaca.data.timeframe import TimeFrame
import pandas as pd
import numpy as np


Tickers=['AAPL', 'BRK.B', 'NEE', 'JPM', 'T', 'PG', 'WMT', 'VZ', 'WFC', 'BAC']
paper_market="https://paper-api.alpaca.markets"
key = "PKXGL3UM3EIW98H8CKD5"
secret = "9thwX2uaiRD5wwhsvbsdhAtuIisfrXoYeXyj7s97"
start="2017-09-01"
end="2022-09-01"

# VARIABLE SETUP #
algoperformance=pd.DataFrame(columns=Tickers) #dataframe for tracking the value of the algorithmic portfolio
BnHperformance=pd.DataFrame(columns=Tickers) #dataframe for tracking the value of the passive portfolio
B=pd.DataFrame(columns=Tickers) #dataframe for storing buy signals
S=pd.DataFrame(columns=Tickers) #dataframe for storing sell signals

# FUNCTION SETUP #
#function for calculating and storing Relative Strength Index
def RSIarrays(data, i):
    diff=(data.iloc[i, 3]-data.iloc[i-1, 3])/data.iloc[i-1, 3]
    current_gain=0
    current_loss=0
    if diff>0:
        avg_gain.append(diff)
        avg_loss.append(0)
        current_gain=diff
    if diff<0:
        avg_loss.append(abs(diff))
        avg_gain.append(0)
        current_loss=abs(diff)
    if diff==0:
        avg_gain.append(diff)
        avg_loss.append(diff)
    if len(avg_loss)>=15:
        avg_loss.pop(0)
    if len(avg_gain)>=15:
        avg_gain.pop(0)
    RSI=100-(100/(1+(sum(avg_gain)/sum(avg_loss))))
    RSI_array.append(RSI)

#function for calculating and storing the Simple Moving Averages
def SMAarrays(data, i):
    value=data.iloc[i, 3]
    close26_array.append(value)
    if len(close26_array)>26:
        close26_array.pop(0)
    close12_array.append(value)
    if len(close12_array)>12:
        close12_array.pop(0)
    SMA26=sum(close26_array)/len(close26_array)
    SMA12=sum(close12_array)/len(close12_array)
    SMA26_array.append(SMA26)
    SMA12_array.append(SMA12)

#functions for storing the Exponential Moving Average
def EMA26arrays(data, i):
    if i<25:
        EMA26_array.append(SMA26_array[i])
        return
    if i>=25:
        EMA26=(data.iloc[i, 3]*(2/(1+26)))+(EMA26_array[i-1]*(1-(2/(1+26))))
        EMA26_array.append(EMA26)

def EMA12arrays(data, i):
    if i<11:
        EMA12_array.append(SMA12_array[i])
        return
    if i>=11:
        EMA12=(data.iloc[i, 3]*(2/(1+12)))+(EMA12_array[i-1]*(1-(2/(1+12))))
        EMA12_array.append(EMA12)  

#functions for computing Moving Average Convergence Divergence
def MACDSMA9arrays(i):
    MACD=EMA12_array[i]-EMA26_array[i]
    MACD9_array.append(MACD)
    if len(MACD9_array)>9:
        MACD9_array.pop(0)
    MACDSMA9=sum(MACD9_array)/len(MACD9_array)
    MACDSMA9_array.append(MACDSMA9)

def MACDEMA9arrays(i):
    if i<26+9-1:
        MACDEMA9_array.append(MACDSMA9_array[i])
        return
    if i>=26+9-1:
        MACDEMA9=(MACDSMA9_array[i]*(2/(1+9)))+(MACDEMA9_array[i-1]*(1-(2/(1+9))))
        MACDEMA9_array.append(MACDEMA9)  

#establish historical data client
hsclient = StockHistoricalDataClient(key, secret)

# MAIN CODE BODY #
for q in range (0, len(Tickers)):
    #establish lists for technical indicators
    avg_gain=[]
    avg_loss=[]
    RSI_array=[]
    close26_array=[]
    close12_array=[]
    close9_array=[]
    SMA26_array=[]
    SMA12_array=[]
    MACD9_array=[]
    MACDSMA9_array=[]
    EMA26_array=[]
    EMA12_array=[]
    MACDEMA9_array=[]
    #collect stock data
    quote_request_params=StockLatestQuoteRequest(symbol_or_symbols=Tickers)
    dbar_request_params=StockBarsRequest(
        symbol_or_symbols=Tickers[q],
        timeframe=TimeFrame.Day,
        start=start,
        end=end
        )
    latest_quote=hsclient.get_stock_latest_quote(quote_request_params)
    bars=hsclient.get_stock_bars(dbar_request_params)
    data=bars.df
    #establish variables for trading loop
    i=0
    cash=10000
    stock_cnt=0
    data_len=len(data)
    #for loop to simulate days
    for i in range(0, data_len-1):
        #stock split price adjustements for NEE and AAPL
        if q==2 and i>=793:
            data.iat[i, 3]=data.iloc[i, 3]*4
        if q==0 and i>=753:
            data.iat[i, 3]=data.iloc[i, 3]*4
        #call functions for calculating technical indicators
        RSIarrays(data, i)
        SMAarrays(data, i)
        EMA26arrays(data, i)
        EMA12arrays(data, i)
        MACDSMA9arrays(i)
        MACDEMA9arrays(i)
        MACD=EMA12_array[i]-EMA26_array[i]
        #buy conditions
        if  i>26+9 and cash>0 and (MACD>MACDEMA9_array[i] and (RSI_array[i]>30 or RSI_array[i]>RSI_array[i-1])):
            stock_cnt=cash/data.iloc[i, 3]
            cash=0
            signal=1
        #sell conditions
        elif  i>26+9 and stock_cnt>0 and (MACD<MACDEMA9_array[i] or (RSI_array[i]<70 or RSI_array[i]<RSI_array[i-1])):
            cash=stock_cnt*data.iloc[i, 3]
            stock_cnt=0
            signal=-1
        else:
            signal=0
        PFvalue=cash+stock_cnt*data.iloc[i, 3] #calculate algorithmic portfolio value
        buynhold=10000*(data.iloc[i, 3]/data.iloc[0, 3]) #calculate passive portfolio value
        #DATA COLLATION
        if q==0:
            algoperformance=algoperformance.append({Tickers[q]:PFvalue}, ignore_index=True)
            BnHperformance=BnHperformance.append({Tickers[q]:buynhold}, ignore_index=True)
            if signal==1:
                B=B.append({Tickers[q]:PFvalue}, ignore_index=True)
                S=S.append({Tickers[q]:0}, ignore_index=True)
            elif signal==-1:
                B=B.append({Tickers[q]:0}, ignore_index=True)
                S=S.append({Tickers[q]:PFvalue}, ignore_index=True)
            else:
                B=B.append({Tickers[q]:0}, ignore_index=True)
                S=S.append({Tickers[q]:0}, ignore_index=True)
        else:
            algoperformance.iat[i, q]=PFvalue
            BnHperformance.iat[i, q]=buynhold
            if signal==1:
                B.iat[i,q]=PFvalue
                S.iat[i,q]=0
            elif signal==-1:
                B.iat[i,q]=0
                S.iat[i,q]=PFvalue
            else:
                B.iat[i,q]=0
                S.iat[i,q]=0

print(algoperformance)
print(BnHperformance)
algovalue=pd.DataFrame().append([sum(algoperformance.iloc[n].tolist()) for n in range(0,len(algoperformance))])
BnHvalue=pd.DataFrame().append([sum(BnHperformance.iloc[n].tolist()) for n in range(0,len(BnHperformance))])
#algovalue.to_csv('algovalue.CSV')
#BnHvalue.to_csv('BnHvalue.CSV')
#B.to_csv('buy signals.CSV')
#S.to_csv('sell signals.CSV')
