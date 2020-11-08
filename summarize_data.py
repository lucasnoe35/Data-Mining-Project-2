import pandas as pd
from matplotlib import pyplot as plt


def sort_data(ticker):
    '''
    Return the data from a CSV file with column headers and the date as
    the index column.

    Argumemts:
        ticker - Ticker symbol of the specified stock.

    Assumptions:
        Stock ticker is in full capitalization.

    The return value of this function is a pandas dataframe.
    '''
    with open(f'{ticker}_data.csv') as file:
        column_names = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close',
                        'Volume']
        data = pd.read_csv(file, names=column_names)
        data.set_index('Date', drop=True, append=False, inplace=True,
                       verify_integrity=False)
        return data


data = sort_data('MSFT')


def make_plot(ticker, data):
    '''
    Create the other three Bollinger Bands and make a plot with the four
    Bollinger bands with date on the X-axis and price (USD) on the Y-axis.

    Arguments:
        ticker - Ticker symbol of the specified stock.
        data - The pandas dataframe of the price statistics.

    Assumumptions:
        Stock ticker is in full capitalization.

    Creates a PNG file of the chart that is created.
    '''
    data['MiddleBand'] = data['Close'].rolling(window=20).mean()
    data['UpperBand'] = (data['MiddleBand'] + 1.96 * data['Close']
                         .rolling(window=20).std())
    data['LowerBand'] = (data['MiddleBand'] - 1.96 * data['Close']
                         .rolling(window=20).std())
    data[['Close', 'MiddleBand', 'UpperBand',
          'LowerBand']].plot(figsize=(12, 6))
    plt.title(f'Bollinger Band for {ticker}')
    plt.ylabel('Price (USD)')
    plt.savefig(f'{ticker}_plot.png', dpi=300, bbox_inches='tight')


make_plot('MSFT', data)


def buy_or_sell(data, ticker):
    '''
    Return a new CSV file with the date, closing price, and if the stock should
    be bought or sold that day.

    Arguments:
        ticker - Ticker symbol of the specified stock.
        data - The pandas dataframe of the price statistics.

    Assumumptions:
        Stock ticker is in full capitalization.
    '''
    data['MiddleBand'] = data['Close'].rolling(window=20).mean()
    data['UpperBand'] = (data['MiddleBand'] + 1.96 * data['Close']
                         .rolling(window=20).std())
    data['LowerBand'] = (data['MiddleBand'] - 1.96 * data['Close']
                         .rolling(window=20).std())
    arrBuySell = ["BUY"] * len(data)
    for i in range(1, len(data)):
        if(data.iloc[i].Close > data.iloc[i].UpperBand):
            arrBuySell[i] = 'SELL'
        elif(data.iloc[i].Close < data.iloc[i].LowerBand):
            arrBuySell[i] = 'BUY'
        else:
            arrBuySell[i] = 'N/A'
    data['BuySell'] = arrBuySell
    stock = pd.DataFrame({'Price': data.Close, 'BUY_SELL': data.BuySell})
    output_file = f'{ticker}_buyORsell.csv'
    stock = stock.reset_index()
    stock.columns = ['Date', 'Price', 'Buy/Sell']
    stock.to_csv(output_file, index=False)
    return stock


buy_or_sell(data, 'MSFT')
