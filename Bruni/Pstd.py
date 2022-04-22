def portfolio_std(tickers, weights,Year,Month,Day):
    import pandas as pd
    import numpy as np
    import pandas_datareader as pdr
    import datetime as dt
    dim = len(tickers)
    start = dt.datetime(Year, Month, Day)
    data = pd.DataFrame()
    std_list = []

    i = 0
    for i in range(dim):
        df = pdr.get_data_yahoo(tickers[i], start)
        df['Prev'] = df['Close'].shift(1)
        df['Returns'] = df['Close'] / df['Prev'] - 1
        df = df.dropna()
        df1 = pd.DataFrame(df['Returns']).copy()
        data[tickers[i]] = df1['Returns']
        std_ = df['Returns'].std()
        std_ = str(round(std_, 2))
        std_list.append(std_)
    std_list = np.array(std_list, dtype=np.float32)
    corr = data.corr()
    i = 0
    for i in range(len(tickers)):
        corr = corr.rename(columns={tickers[i]: i})

    i = 0
    j = 0
    k = 0
    for i in range(len(tickers)):
        k = k + (weights[i] ** 2) * (std_list[i] ** 2)

    i = 0
    g = 0
    j = 0
    for i in range(len(tickers)):
        j = i + 1
        while j < len(tickers):
            g = g + 2 * weights[i] * weights[j] * std_list[i] * std_list[j] * round(corr[j].iloc[i], 6)
            j = j + 1
    portfolio_std = round((g + k) ** 0.5, 6)
    return portfolio_std

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

