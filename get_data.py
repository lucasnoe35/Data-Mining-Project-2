import yfinance as yf
import pandas as pd


def get_data(ticker):
    '''
    Create a new CSV file with the date, openening price, high price,
    low price, closing price, adjusted closing price, and the volume
    of a stock on a given day.

    Arguments:
        ticker - Ticker symbol of the specified stock.

    Assumptions:
        Stock ticker is in full capitalization.
    '''
    data = yf.download(f'{ticker}',
                       start='2018-01-01',
                       end='2020-11-06',
                       )
    data = data.reset_index()
    output_file = f'{ticker}_data.csv'
    return data.to_csv(output_file, index=False, header=None)


get_data('MSFT')
