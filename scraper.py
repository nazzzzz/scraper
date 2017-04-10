import requests
from bs4 import BeautifulSoup
import sys

def getSlickDeals(q):
    titles = []

    baseUrl = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q=" + q
    html = requests.get(baseUrl).text
    soup = BeautifulSoup(html,"html.parser")

    deals = soup.select(".dealWrapper .dealTitle")

    for deal in deals:
        dealTitle = deal.get("title")
        titles.append(dealTitle)
        print("---------------------------------------------------------------------")
        print (dealTitle)
        print("---------------------------------------------------------------------")

    return titles

getSlickDeals(sys.argv[1])