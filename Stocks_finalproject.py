##Final Project--Stock Data

!pip install yfinance==0.1.67
!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

#Using the Ticker module we can create an object that will allow us to access functions to extract data. 
#To do this we need to provide the ticker symbol for the stock, 
#here the company is Apple and the ticker symbol is AAPL.

apple = yf.Ticker("AAPL")

#Using the attribute info we can extract information about the stock as a Python dictionary.

apple_info=apple.info
apple_info
apple_info['country']

#Using the history() method we can get the share price of the stock over a certain period of time. 
#Using the period parameter we can set how far back from the present to get data. 
#The options for period are 1 day (1d), 5d, 1 month (1mo) , 
#3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
#The format that the data is returned in is a Pandas DataFrame. 
#With the Date as the index the share Open, High, Low, Close, Volume, 
#and Stock Splits are given for each day.

#We can reset the index of the DataFrame with the reset_index function. 
#We also set the inplace paramter to True so the change takes place to the DataFrame itself.
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.head()
apple_share_price_data.plot(x="Date", y="Open")

#dividends
apple.dividends
apple.dividends.plot()

#Example

amd = yf.Ticker("AMD")
amd_info = amd.info
amd_info['country']
amd_info['sector']
amd_price_data = amd.history(period = "max")
amd_price_data.head()


## Final Project--Webscraping
!pip install pandas==1.3.3
!pip install requests==2.26.0
!mamba install bs4==4.10.0 -y
!mamba install html5lib==1.1 -y
!pip install lxml==4.6.4
!pip install plotly==5.3.1

import pandas as pd
import requests
from bs4 import BeautifulSoup

#First we must use the request library to downlaod the webpage, and extract the text. 
#We will extract Netflix stock data 
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

#Now we can turn the html table into a pandas dataframe
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])

# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table
    netflix_data = netflix_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)    

netflix_data.head()

#We can also use the pandas read_html function using the url
read_html_pandas_data = pd.read_html(url)
read_html_pandas_data = pd.read_html(str(soup))
netflix_dataframe = read_html_pandas_data[0] #Beacause there is only one table on the page, we just take the first table in the list returned
netflix_dataframe.head()
 #### my turn ###
 url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data = requests.get(url).text
b_soup = BeautifulSoup(html_data, 'html5lib')

tag_title=b_soup.title
tag_title


amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

for row in b_soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    amazon_data = amazon_data.append({"Date":date, "Open":Open, "High":high, "Low":low, "Close":close, "Adj Close":adj_close, "Volume":volume}, ignore_index=True)

amazon_data.head()


