# Bruni
This package allows you to compute the standard deviation of a portfolio, whatever it is the number of
 stocks that are in it, or the correlation table.

------------------------------------------------------------------------------------------------------
Arguments needed for .portfolio_std():
-list of the stock's tickers
-list of respective weights
-starting year from when collect data
-starting month from when collect data
-starting day from when collect data

--------------------------------------

Arguments needed for .portfolio_corr():
-list of the stock's tickers
-starting year from when to collect data
-starting month from when to collect data
-starting day from when to collect data

--------------------------------------
The algorithm for the computation of the standard deviation of the portfolio follow this formula and it's based on the returns of the stocks:

             σ² = Σ°Σ'[w°w'σ(R°,R')]


## Installation
```
pip install Bruni

```

## Usage
```
import Bruni.Pstd as bstd 

tickers =['AAPL','MSFT','TSLA'] #caps tickers
corr = bstd.portfolio_corr(tickers,2020,12,31) #getting the table of correlation

```
```
import Bruni.Pstd as bstd

tickers =['AAPL','MSFT','TSLA']
weights = [0.1,0.5,0.4] #for std are needed weights
std = bstd.portfolio_std(tickers,weights,2020,12,31) #weights must be passed in the function

```
