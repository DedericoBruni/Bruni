def portfolio_std(tickers, weights,Year,Month,Day):
    import pandas as pd
    import numpy as np
    import pandas_datareader as pdr
    import datetime as dt
    dim = len(tickers)
    start = dt.datetime(Year, Month, Day)
    data = pd.DataFrame()

    i = 0
    for i in range(dim):
        df = pdr.get_data_yahoo(tickers[i], start)
        df['Prev'] = df['Close'].shift(1)
        df['Returns'] = df['Close'] / df['Prev'] - 1
        df = df.dropna()
        df1 = pd.DataFrame(df['Returns']).copy()
        data[tickers[i]] = df1['Returns']
    weights = np.array(weights, dtype=np.float32)
    cov = data.cov().to_numpy()
    risk = np.sqrt(weights.dot(cov).dot(weights))
    return risk

def portfolio_corr(tickers,Year,Month,Day):
    import pandas as pd
    import pandas_datareader as pdr
    import datetime as dt
    dim = len(tickers)
    data = pd.DataFrame()
    start = dt.datetime(Year, Month, Day)

    i = 0
    for i in range(dim):
        df = pdr.get_data_yahoo(tickers[i], start)
        df['Prev'] = df['Close'].shift(1)
        df['Returns'] = df['Close'] / df['Prev'] - 1
        df = df.dropna()
        df1 = pd.DataFrame(df['Returns']).copy()
        data[tickers[i]] = df1['Returns']

    corr = data.corr()
    return corr

