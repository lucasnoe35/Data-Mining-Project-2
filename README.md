#Data Mining
This repository is comprised of two python files with functions that pull data from Yahoo Finance and plot its Boolinger Bands in a PNG file which it creates and a day to day recommendation of if a stock should be bought or sold in CSV format. The default stock that these functions analyze is Microsoft (MSFT). Included in this repository is also the raw data of Microsofts stock infromation as well as the Bollinger Band plot and CSV data buy/sell sheet. The repository also includes a computational essay that anlyzes Microsoft's Bollinger Band data and how the function created the files it did. Included is also the pytests for the functions assuming they are ran on Microsofts stock ticker.  
  
* `yfinance`: The python files in this repository call on the Yahoo Finance libarary that can be insatlled with the command:  
`$ pip3 install yfinance`.
* `get-data.py`: This file creates a raw CSV file with data on a stock of the specified ticker. To change the stock that this function pulls data on, just change the ticker that defaults to MSFT when the function is called.  
* `summarize_data.py`: This file creates both the PNG of the Bollinger Band plot and the CSV with the Buy/Sell days. To change the stock that this file analyzes, when each function is called, change the ticker from the default MSFT of Microsfot. There are three instances that need to be changed so ideally use Ctrl f's replace option and replace all MSFT instances.  
  
