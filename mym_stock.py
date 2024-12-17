import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage content
url = 'https://stockanalysis.com/list/bursa-malaysia/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Parse the stock data
stock_data = []
table = soup.find('table')  # Locate the table containing the stock data
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    if len(columns) > 1:  # Ensure the row contains data
        symbol = columns[0].text.strip()
        company_name = columns[1].text.strip()
        market_cap = columns[2].text.strip()
        stock_price = columns[3].text.strip()
        stock_data.append([symbol, company_name, market_cap, stock_price])

# Step 3: Save the data to a CSV file
df = pd.DataFrame(stock_data, columns=['Symbol', 'Company Name', 'Market Cap', 'Stock Price'])
df.to_csv('bursa_malaysia_stocks.csv', index=False)
