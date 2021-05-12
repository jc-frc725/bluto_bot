# test.py
import responses
import bs4
import requests

stockResponse = requests.get("https://finance.yahoo.com/quote/gme").content

soup = bs4.BeautifulSoup(stockResponse, "html.parser")
stock = soup.find(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
print(stock)
print('text found?')

