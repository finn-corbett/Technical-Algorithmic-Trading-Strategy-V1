# trading-algo-0.1

A stock trading algorithm, backtested for 5 years from Sep 1 2017 to Sep 1 2022. This algorithm has been developed to test a simple trading strategy and evaluate its performance in managing a stock portfolio. I have conducted this project to improve my programming and financial skills, alongside showcasing my abilities.  
  
As of posting this report, I am a 4th year Meng Aerospace Engineering student. I began this project to take on a challenging new task which is outside my area of expertise, I have taught myself to code using Python and have conducted my own research to gain the skills necessary to complete this.

This graph compares the value of a portfolio managed by the trading algorithm against using the 'Buy and Hold' strategy for the same stocks, and a Buy and Hold strategy applied to the S&P500 (SPY). Each portfolio started the 5 year period with £100,000. The risk free rate for that 5 year period is included for comparison. To briefly summarise the results, the trading strategy is able to choose performant stocks, which by trading them based on price movements can maintain a reasonable degree of profitability whilst greatly reducing volatility/risk.
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/Portfolio.png" alt="drawing" width="750"/>
### Table of Contents

* [About](#about)
* [Features](#features)
   1. [Data Collection](#data-collection)
   2. [Stock Selection](#stock-selection)
   3. [Indicators](#indicators)
   4. [Signal Generation](#signal-generation)
   5. [Portfolio Allocation](#portfolio-allocation)
* [Performance](#performance)
* [Conclusion](#conclusion)

### About <a name="about"></a>

This algorithm is a simple trading strategy, using 2 technical indicators to generate buy and sell signals for a selection of stocks. It has been developed using historical stock pricing data from the Alpaca-py SDK. This algorithm is allowed to buy and sell 10 different stocks.  
There is no live version of this strategy, the 'backtest.py' contains all of the code. In order to use the backtest script, you must create an account with alpaca to get keys for their historical data API.

# Features <a name="features"></a>
### Data Collection <a name="data-collection"></a>

Stock pricing data is collected using the Alpaca-py SDK, 5 years of historical daily ticker data is collected for each stock. This data used consists of daily close prices for each stock, which this algorithm computes indicators and buy/sell positions from.

### Stock Selection <a name="stock-selection"></a>

Stocks are selected manually, with 10 large cap stocks being selected. Stocks were selected using the historical stock screener from ChartMills, the use of screening based on historical metrics eliminates bias in the stock selection process. This means that the algorithmic trading strategy presented in this report can be reliably compared to alternative investments.

The 10 stocks with the largest market capitalisation, within the IEX exchange, that meet these requirements are selected:

* free float > 20%
* EPS        > 0
* P/E        < 20 AND > 0
* P/S        < 14

The resulting stocks selected are:  

AAPL - Apple Inc  
BRK.B - Berkshire Hathaway Inc Class B  
NEE - NextEra Energy Inc  
JPM - JPMorgan Chase & Co  
T - AT&T Inc.  
PG - Procter & Gamble Co  
WMT - Walmart Inc  
VZ - Verizon Communications Inc.  
WFC - Wells Fargo & Co  
BAC - Bank of America Corp  

### Indicators <a name="indicators"></a>

The algorithm calculates two indicators using the daily closing prices, that is the MACD (moving average convergence divergence) and RSI (relative strength index)

MACD is calculated by subtracting the 26 day EMA (exponential moving average) from the 12 day EMA. A signal line is created using the 9 day EMA which the MACD can be compared to, to generate buy and sell signals.

RSI is calculated by looking at the previous 14 losses and gains to see if the price is trending upwards or downwards. Feel free to google exactly how it's calculated, Investopedia is a great source.

### Signal Generation <a name="signal-generation"></a>

A buy signal is generated if:
* The MACD value is greater than the signal value AND
* The RSI>30 OR The RSI value is greater than the value for the previous period

A sell signal is generated if:
* The MACD value is less than the signal value OR
* The RSI<70 OR The RSI value is less than the value for the previous period

### Portfolio Allocation <a name="portfolio-allocation"></a>

$10000 is allocated to each of the 10 stocks, and any losses or gains are applied to this value, so that underperforming stocks take up a smaller portion of the portfolio, whilst overperforming stocks take up a larger portion. Any buy or sell signal sells and buys a stock with all of the money available to use for that stock. When buying and selling stocks, zero fees are assumed.

### Performance <a name="performance"></a>

This algorithm was able to produce 31.76% returns over a 5 year period, with an annualised daily return standard deviation of 6.45%.  
A buy and hold strategy for the same 10 stocks yielded 56.67% over the same period, with an annualised daily return standard deviation of 19.46%.  
Investing in SPY yielded 59.41%, with an annualised daily return standard deviation of 20.23%  
  
Sharpe ratios for the 3 investment strategies are:
* Algorithm    -     0.612
* Buy and Hold -     0.4646
* SPY          -     0.4455

The sharpe ratios are calculated with a risk free rate of 1.809%, being the yield of the US 5 year treasury bond on Sep 1 2017.

These performance results indicate the the algorithmic trading strategy is able to reduce the risk compared to alternative investing strategies, such that the risk-adjusted returns are greater than that of the SPY. The SPY is a widely used passive investing strategy, which is often implimented as a benchmark due to it's historic performance and passive nature. These results indicate the algorithmic trading strategy being useful for investors wishing to sacrifice some of their returns to reduce risk.  
### Performance Charts
### AAPL
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/AAPL.png" alt="drawing" width="750"/> 

### BRK.B
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/BRK-B.png" alt="drawing" width="750"/> 

### NEE
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/NEE.png" alt="drawing" width="750"/>  

### JPM
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/JPM.png" alt="drawing" width="750"/>  

### T
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/T.png" alt="drawing" width="750"/>  

### PG
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/PG.png" alt="drawing" width="750"/>  

### WMT
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/WMT.png" alt="drawing" width="750"/>  

### VZ
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/VZ.png" alt="drawing" width="750"/>  

### WFC
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/WFC.png" alt="drawing" width="750"/>  

### BAC
<img src="https://github.com/finn-corbett/trading-algo-0.1/blob/main/Images/BAC.png" alt="drawing" width="750"/> 


### Conclusion <a name="conclusion"></a>

The trading strategy is able to produce steady returns with preferable risk characteristics through a reduction in volatility. It can be seen across the various performance graphs that the strategy is capable of preventing large losses, such as that of the market crash caused by COVID-19. This trading strategy is best suited towards low-risk investors.

The main concerns with this strategy and algorithm are:
* stop losses are not yet implimented, meaning that the algorithm may lose excessive amounts of money to large crashes.
* algorithm must wait 30 days to calculate indicators properly, resulting in 30 days downtime when it is initiated

Future versions should include:
* automated stock selection
* more technical indicators
* more computationally efficient indicator calculation
* Machine learning for signal generation
* more advanced and dynamic portfolio allocation
