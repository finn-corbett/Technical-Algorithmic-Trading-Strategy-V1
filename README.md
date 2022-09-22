# trading-algo-0.1
A simple stock trading algorithm, backtested for 5 years.

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
There is no live version of this strategy, the 'backtest.py' is the only file for this strategy, as improvements are desired before implementing a live version.

This algorithm is not documented in depth, it is not intended for others to use, it is simply for me to improve my skills and showcase the results.

# Features <a name="features"></a>
## Data Collection <a name="data-collection"></a>

Stock pricing data is collected using the alpaca-py SDK, 5 years of historical daily ticker data is collected for each stock. This data includes daily open and close prices, which this algorithm requires.

Data for stock selection is manually collected and processed, from TradingView.

## Stock Selection <a name="stock-selection"></a>

Stocks are selected manually, future versions may include automatic stock selection and reselection. One issue with this version of the trading algorithm is that the stocks are selected on current data, but are tested against historic data. This is not representative of live performance, whereing stocks would be selected based on current data and be tested (or implemented live) against future data. This will undoubtedly affect the results, future algorithms should avoid this.

The 10 stocks with the largest market capitalisation that meet these requirements are selected:

free float > 20%
EPS        > 0
P/E        < 20
P/S        < 15

## Indicators <a name="indicators"></a>

The algorithm calculates two indicators using the daily closing prices, that is the MACD (moving average convergence divergence) and RSI (relative strength index)

MACD is calculated by subtracting the 26 day EMA (exponential moving average) from the 12 day EMA. A signal line is created using the 9 day EMA which the MACD can be compared to, to generate buy and sell signals.

RSI is caculated by looking at the previous 14 losses or gains to see if the price is trending upwards or downwards. I don't know how to show equations on .md files yet so feel free to google exactly how it's calculated, investopedia is a great source.

## Signal Generation <a name="signal-generation"></a>

A buy signal is generated if:
* The MACD value is greater than the signal value AND
* The RSI>30 AND
* The RSI value is greater than the value for the previous period

A sell signal is generated if:
* The MACD value is less than the signal value AND
* The RSI<60
* The RSI value is less than the value for the previous period

## Portfolio Allocation <a name="portfolio-allocation"></a>

$10000 is allocated to each of the 10 stocks, and any losses or gains are applied to this value, so that underperforming stocks take up a smaller portion of the portfolio, whilst overperforming stocks take up a larger portion. Any buy or sell signal sells and buys a stock with all of the money available to the stock. 

## Performance <a name="performance"></a>
a
## Conclusion <a name="conclusion"></a>
a
