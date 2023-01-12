# trading-algo-0.1

A stock trading algorithm, backtested for 5 years from Sep 1 2017 to Sep 1 2022. This algorithm has been developed to test a simple trading strategy and evaluate its performance in managing a stock portfolio. I have conducted this project to improve my programming and financial skills, alongside showcasing my abilities. 

This graph compares the value of a portfolio managed by the trading algorithm against using the 'Buy and Hold' strategy for the same stocks. Each portfolio started the 5 year period with £10,000.  
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/Portfolio.png" alt="drawing" width="750"/>
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

This algorithm is a simple trading strategy, using 2 technical indicators to generate buy and sell signals for a selection of stocks. It has been developed using historical stock pricing data from the Alpaca-py SDK. This strategy is allowed to buy and sell 10 different stocks.  
There is no live version of this strategy, the 'backtest.py' is the only file for this strategy. In order to use the backtest script, you must create an account with alpaca to get keys for their historical data API.

# Features <a name="features"></a>
## Data Collection <a name="data-collection"></a>

Stock pricing data is collected using the Alpaca-py SDK, 5 years of historical daily ticker data is collected for each stock. This data used consists of daily close prices for each stock, which this algorithm computes indicators and buy/sell positions from.

Data for stock selection is manually collected and processed, from TradingView.

## Stock Selection <a name="stock-selection"></a>

Stocks are selected manually, with 10 large cap stocks being selected. One issue with this method is that the stocks are selected on current data, but are tested against historic data. This has the potential to introduce bias, wherein returns from this strategy may outperform other strategies as the highest cap stocks at the end of the backtest period were selected. This means that the stocks selected were likely to increase or maintain a high value during the 5 year backtest. This selection has been done to ensure that the strategy is employed on stocks that are frequently traded and have sensible fundementals.

As a result of this limitation, the returns from the trading strategy should only be compared against the buy and hold performance for the same stocks. Such results will indicate the ability of the strategy to generate additional returns by selling during downturns, and buying during predicted upwards price movements.

The 10 stocks with the largest market capitalisation that meet these requirements are selected:

* free float > 20%
* EPS        > 0
* P/E        < 20 AND > 0
* P/S        < 14

## Indicators <a name="indicators"></a>

The algorithm calculates two indicators using the daily closing prices, that is the MACD (moving average convergence divergence) and RSI (relative strength index)

MACD is calculated by subtracting the 26 day EMA (exponential moving average) from the 12 day EMA. A signal line is created using the 9 day EMA which the MACD can be compared to, to generate buy and sell signals.

RSI is calculated by looking at the previous 14 losses and gains to see if the price is trending upwards or downwards. Feel free to google exactly how it's calculated, Investopedia is a great source.

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

This algorithm was able to produce 33.50% returns over a 5 year period, with a standard deviation of ~13900.
A buy and hold strategy for the same 10 stocks yielded 40.34% over the same period, with a standard deviation of ~17600.
### Performance Charts
* ### META
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/META.png" alt="drawing" width="750"/>
* ### XOM
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/XOM.png" alt="drawing" width="750"/>
* ### JPM
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/JPM.png" alt="drawing" width="750"/>
* ### CVX
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/CVX.png" alt="drawing" width="750"/>
* ### HD
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/HD.png" alt="drawing" width="750"/>
* ### BAC
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/BAC.png" alt="drawing" width="750"/>
* ### PFE
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/PFE.png" alt="drawing" width="750"/>
* ### ABBV
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/ABBV.png)
* ### MRK
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/MRK.png)
* ### CSCO
![alt text](https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images%20V2/CSCO.png)

## Conclusion <a name="conclusion"></a>

The trading strategy is able to maintain profits when applied to profitable stocks. It can be seen across the various performance graphs that the strategy is capable of preventing large losses, such as that of the market crash caused by COVID-19. Whilst maintaining a degree of profitability, the strategy is capable of reducing volatility. This trading strategy is best suited towards low-risk investors, although it requires excellent stock-picking.

The main concerns with this strategy and algorithm are:
* stock selection uses current data, but is tested historically. This makes the backtest innacurate for future results and cannot be compared to other strategies.
* stop losses are not yet implimented, meaning that the algorithm may lose excessive amounts of money to large crashes.
* algorithm must wait 30 days to calculate indicators properly, resulting in 30 days downtime when it is initiated

Future versions should include:
* automated stock selection
* more technical indicators
* more computationally efficient indicator calculation
* Machine learning for signal generation
* more advanced portfolio allocation, including a cash position, based on volatility
* sharpe ratio and alpha considerations
