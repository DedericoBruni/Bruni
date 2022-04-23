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

def portfolio_return(tickers,weights,Year,Month,Day):
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
    return data.mean().dot(weights)

def find_best_allocation(tickers,Year,Month,Day,N):
    def returns(tickers,Year,Month,Day):
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
        return data
    def port_returns_s(data,weights):
            weights = np.array(weights, dtype=np.float32)
            exp_ret = data.mean().to_numpy()
            return exp_ret.dot(weights)
    def port_std_s(data,weights):
        cov = data.cov().to_numpy()
        risk = np.sqrt(weights.dot(cov).dot(weights))
        return risk
    sharp_list=[]
    w_list = []
    i = 0
    data = returns(tickers,Year,Month,Day)
    for i in range(N):
        w = np.random.random(len(tickers))
        w = w/w.sum()
        w_list.append(w)
        ret = port_returns_s(data,w)
        std = port_std_s(data,w)
        sr = ret/std
        sharp_list.append(sr)
    max_sr = np.max(sharp_list)
    alloc = w_list[np.argmax(sharp_list)]
    return alloc
