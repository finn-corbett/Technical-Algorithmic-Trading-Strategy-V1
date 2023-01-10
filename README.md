# trading-algo-0.1

A simple stock trading algorithm, backtested for 5 years from Sep 1 2017 to Sep 1 2022.

## Table of Contents

* [About](#about)
* [Features](#features)
   1. [Data Collection](#data-collection)
   2. [Stock Selection](#stock-selection)
   3. [Indicators](#indicators)
   4. [Signal Generation](#signal-generation)
   5. [Portfolio Allocation](#portfolio-allocation)
* [Performance](#performance)
* [Conclusion](#conclusion)

## About <a name="about"></a>

This algorithm is a simple trading strategy, using 2 technical indicators to generate buy and sell signals for a selection of stocks.
There is no live version of this strategy, the 'backtest.py' is the only file for this strategy. In order to use the backtest file, you must create an account with alpaca to get keys for their historical data API.

# Features <a name="features"></a>
## Data Collection <a name="data-collection"></a>

Stock pricing data is collected using the alpaca-py SDK, 5 years of historical daily ticker data is collected for each stock. This data includes daily open and close prices, which this algorithm requires.

Data for stock selection is manually collected and processed, from TradingView.

## Stock Selection <a name="stock-selection"></a>

Stocks are selected manually, with 10 large cap stocks being selected. One issue with this method is that the stocks are selected on current data, but are tested against historic data. This has the potential to introduce bias, wherein returns from this strategy may outperform other strategies as the highest cap stocks at the end of the backtest period were selected. This means that the stocks selected were likely to increase or maintain a high value during the 5 year backtest.

As a result of this limitation, the returns from the trading strategy should only be compared against the buy and hold performance for the same stocks. Such results will indicate the ability of the strategy to 

This is not representative of live performance, whereing stocks would be selected based on current data and be tested (or implemented live) against future data. This will undoubtedly affect the results, future algorithms should avoid this.

The 10 stocks with the largest market capitalisation that meet these requirements are selected:

* free float > 20%
* EPS        > 0
* P/E        < 20
* P/S        < 15

## Indicators <a name="indicators"></a>

The algorithm calculates two indicators using the daily closing prices, that is the MACD (moving average convergence divergence) and RSI (relative strength index)

MACD is calculated by subtracting the 26 day EMA (exponential moving average) from the 12 day EMA. A signal line is created using the 9 day EMA which the MACD can be compared to, to generate buy and sell signals.

RSI is caculated by looking at the previous 14 losses and gains to see if the price is trending upwards or downwards. Feel free to google exactly how it's calculated, investopedia is a great source.

## Signal Generation <a name="signal-generation"></a>

A buy signal is generated if:
* The MACD value is greater than the signal value AND
* The RSI>30 AND
* The RSI value is greater than the value for the previous period

A sell signal is generated if:
* The MACD value is less than the signal value AND
* The RSI<70 AND
* The RSI value is less than the value for the previous period

## Portfolio Allocation <a name="portfolio-allocation"></a>

$10000 is allocated to each of the 10 stocks, and any losses or gains are applied to this value, so that underperforming stocks take up a smaller portion of the portfolio, whilst overperforming stocks take up a larger portion. Any buy or sell signal sells and buys a stock with all of the money available to that stock. 

## Performance <a name="performance"></a>

This algorithm was able to produce 33.50% returns over a 5 year period.
The S&P500 was able to produce 60.18% returns over the same period.
A buy and hold strategy for the same 10 stocks yielded 40.34% over the same period.
### Performance Charts
* ### META
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/META.png)
* ### XOM
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/XOM.png)
* ### JPM
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/JPM.png)
* ### CVX
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/CVX.png)
* ### HD
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/HD.png)
* ### BAC
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/BAC.png)
* ### PFE
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/PFE.png)
* ### ABBV
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/ABBV.png)
* ### MRK
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/MRK.png)
* ### CSCO
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/CSCO.png)

## Conclusion <a name="conclusion"></a>

The performance of this strategy is not outstanding, it is able to generate positive returns, but will not outperform investing (long term) strategies such as 'buy and hold' for the same stocks, or index investing. This shows that the buy and sell signals are somewhat effective in generating returns.

The main concerns with this strategy and algorithm are:
* stock selection uses current data, but is tested historically. This makes the backtest innacurate for future results.
* stop losses are not yet implimented, meaning that the algorithm may lose excessive amounts of money to large crashes.
* algorithm must wait 30 days to calculate indicators properly, resulting in 30 days downtime when it is initiated

trading-algo-0.2 will include:
* automated stock selection
* more technical indicators with stacked LTSM model to learn which indicators are most effective for each stock
* more computationally efficient indicator calculation

trading-algo-0.3 and beyond may include:
* more advanced portfolio allocation, including a cash position, based on volatility
* sharpe ratio and alpha considerations
