import requests
from bs4 import BeautifulSoup
import pandas


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

url = 'https://finance.yahoo.com/quote/%5EBVSP/history/'

print('Request: ')
response = requests.get(url, headers=headers)
print("Status:", response.status_code)
print(response.text[:600])

print('\nBeautifulSoup: ')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print('\nPandas: ')
url_dados = pandas.read_html(response.text)
print(url_dados[0].head(10))