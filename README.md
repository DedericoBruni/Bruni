# Bruni
This package allows you to compute the standard deviation of a portfolio, whatever it is the number of
 stocks that are in it, or the correlation table.

------------------------------------------------------------------------------------------------------
Arguments needed for .portfolio_std():
- list of the stock's tickers
- list of respective weights
- starting year from when collect data
- starting month from when collect data
- starting day from when collect data

--------------------------------------

Arguments needed for .portfolio_corr():
- list of the stock's tickers
- starting year from when to collect data
- starting month from when to collect data
- starting day from when to collect data

--------------------------------------

Arguments needed for .portfolio_return():
- list of the stock's tickers
- list of respective weights
- starting year from when to collect data
- starting month from when to collect data
- starting day from when to collect data

--------------------------------------

Arguments needed for .find_best_allocation():
- list of the stock's tickers
- starting year from when to collect data
- starting month from when to collect data
- starting day from when to collect data
- numbers of iterations for the montecarlo simulation (suggested > 5000)

--------------------------------------

The algorithm for the computation of the standard deviation of the portfolio follow this formula and it's based on the returns of the stocks:

             σ² = Σ°Σ'[w°w'σ(R°,R')]


## Installation
```
pip install Bruni
```

## Usage
Correlation
```
import Bruni.Pstd as brn 

tickers =['AAPL','MSFT','TSLA'] #caps tickers
corr = brn.portfolio_corr(tickers,2020,12,31) #getting the table of correlation
```

Standard deviation
```
import Bruni.Pstd as brn

tickers =['AAPL','MSFT','TSLA']
weights = [0.1,0.5,0.4] #for std are needed weights
std = brn.portfolio_std(tickers,weights,2020,12,31) #weights must be passed in the function
```

Portfolio Return
```
import Bruni.Pstd as brn

tickers =['AAPL','MSFT','TSLA']
weights = [0.1,0.5,0.4] #for std are needed weights
ret = brn.portfolio_return(tickers,weights,2020,12,31) #weights must be passed in the function
```

Portfolio Best Allocation
```
import Bruni.Pstd as brn

tickers =['AAPL','MSFT','TSLA']
alloc = brn.find_best_allocation(tickers,2020,12,31,5000) #in the example N=5000, higher is better
```
