import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    
    companies_and_tickers = []
    for row in table.findAll('tr')[1:]:
        company = row.findAll('td')[1].text
        ticker = row.findAll('td')[0].text[:-1]
        company_and_ticker = company + " " + "(" + ticker + ")"
        companies_and_tickers.append(company_and_ticker)
    
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(companies_and_tickers, f)

    return companies_and_tickers