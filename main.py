import requests
from bs4 import BeautifulSoup
import pandas as pd


API = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"

full_page = requests.get(API)
soup = BeautifulSoup(full_page.content, features="lxml")


def exchange_rates():
    names = soup.findAll("txt")
    price = soup.findAll("rate")
    date = soup.find("exchangedate").get_text()

    data = []

    for i in range(len(names)):
        row = [names[i].get_text(),
               price[i].get_text()]
        data.append(row)

    table = pd.DataFrame(data, columns=["name", "price"])
    pd.set_option("display.max_rows", None)
    return f"Обмінний курс гривні за {date} число. \n\n {table}"


result = exchange_rates()
print(result)
