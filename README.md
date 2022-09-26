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
There is no live version of this strategy, the 'backtest.py' is the only file for this strategy, as improvements are desired before implementing a live version.

This algorithm is not documented in depth, it is not intended for others to use, it is simply for me to improve my skills and showcase the results.

# Features <a name="features"></a>
## Data Collection <a name="data-collection"></a>

Stock pricing data is collected using the alpaca-py SDK, 5 years of historical daily ticker data is collected for each stock. This data includes daily open and close prices, which this algorithm requires.

Data for stock selection is manually collected and processed, from TradingView.

## Stock Selection <a name="stock-selection"></a>

Stocks are selected manually, future versions may include automatic stock selection and reselection. One issue with this version of the trading algorithm is that the stocks are selected on current data, but are tested against historic data. This is not representative of live performance, whereing stocks would be selected based on current data and be tested (or implemented live) against future data. This will undoubtedly affect the results, future algorithms should avoid this.

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
* The RSI<60 AND
* The RSI value is less than the value for the previous period

## Portfolio Allocation <a name="portfolio-allocation"></a>

$10000 is allocated to each of the 10 stocks, and any losses or gains are applied to this value, so that underperforming stocks take up a smaller portion of the portfolio, whilst overperforming stocks take up a larger portion. Any buy or sell signal sells and buys a stock with all of the money available to that stock. 

## Performance <a name="performance"></a>

This algorithm was able to produce 29.76% returns over a 5 year period.
The S&P500 was able to produce 60.18% returns over the same period.
A buy and hold strategy for the same 10 stocks yielded 40.34% over the same period.
### Performance Charts
*### META
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/META%20Chart.png)
*### XOM
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/XOM%20Chart.png)
*### JPM
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/JPM%20Chart.png)
*### CVX
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/CVX%20Chart.png)
*### HD
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/HD%20Chart.png)
*### BAC
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/BAC%20Chart.png)
*### PFE
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/PFE%20Chart.png)
*### ABBV
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/ABBV%20Chart.png)
*### MRK
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/MRK%20Chart.png)
*### CSCO
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/CSCO%20Chart.png)

## Conclusion <a name="conclusion"></a>

The performance of this strategy is not outstanding, but it was able to outperform a buy and hold strategy for the same stocks over a 5 year period. This shows that the buy and sell signals are somewhat effective in generating returns. This strategy was not able to outperform 'the market' (S&P500 buy and hold strategy), which is considered a benchmark by investors.

The main concerns with this strategy and algorithm are:
* stock selection uses current data, but is tested historically. This makes the backtest innacurate for future results.
* stop losses are not yet implimented, meaning that the algorithm may lose excessive amounts of money to large crashes.
* 10 stocks is not a very diverse selection, which increases portfolio risk
* algorithm must wait 30 days to calculate indicators properly, resulting in 30 days downtime when it is initiated

Future improvements should include:
* automated stock selection and yearly reselection
* stop losses
* more technical indicators with stacked LTSM model to learn which indicators are most effective for each stock
* more computationally efficient indicator calculation
* 
