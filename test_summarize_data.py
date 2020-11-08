"""
Test Summarize Data
"""
import pytest
import pandas as pd
import summarize_data
from summarize_data import sort_data
from summarize_data import make_plot
from summarize_data import buy_or_sell


def test_sort_data0():
    # Test that the return of the function sort_data(ticker) is
    # a pandas dataframe.
    assert isinstance(sort_data('MSFT'), pd.DataFrame)


def test_sort_data1():
    # Test the index column name of the pandas dataframe created
    # in sort_data(ticker) is 'Date'.
    assert sort_data('MSFT').index.name == 'Date'


def test_sort_datas2():
    # Test the first column in the pandas dataframe has the
    # header 'Open' to ensure that 'Date' is not now the header
    # of both the index and the first column.
    assert sort_data('MSFT').columns[0] == 'Open'


def test_sort_data3():
    # Test that the last column header is 'Volume' to make
    # sure that the rest of the headers are lined up properly.
    assert sort_data('MSFT').columns[-1] == 'Volume'


def test_buy_or_sell0():
    # Test the function buy_or_sell() creates a pandas dataframe
    # before making that dataframe into a CSV file.
    assert isinstance(buy_or_sell(sort_data('MSFT'), 'MSFT'),
                      pd.DataFrame)


def test_buy_or_sell1():
    # Test the function buy_or_sell's dataframe says 'BUY'
    # when the closing cost is below the upper Bollinger Band
    assert str(buy_or_sell(sort_data('MSFT'),
               'MSFT').iloc[0][[2]]) == 'Buy/Sell    BUY\nName:\
                    0, dtype: object'


def test_buy_or_sell2():
    # Test the function buy_or_sell's dataframe says 'SELL'
    # when the closing cost is above the upper Bollinger Band
    assert str(buy_or_sell(sort_data('MSFT'),
               'MSFT').iloc[72][[2]]) == 'Buy/Sell    SELL\nName:\
                   72, dtype: object'


def test_buy_or_sell3():
    # Test the function buy_or_sell's dataframe says 'N/A'
    # when the closing cost is between the upper and lower
    # Bollinger Bands
    assert str(buy_or_sell(sort_data('MSFT'),
               'MSFT').iloc[1][[2]]) == 'Buy/Sell    N/A\nName:\
                    1, dtype: object'
