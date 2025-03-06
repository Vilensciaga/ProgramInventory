from bs4 import BeautifulSoup
import requests
import array



# def loadData2():
#     scrapePage = requests.get("http://quotes.toscrape.com")
#     soup = BeautifulSoup(scrapePage.text, "html.parser")
#     print(soup.title.text)
#     quotes = soup.find_all("span", attrs={"class":"text"})
#     authors = soup.find_all("small", attrs={"class":"author"})


#     print(authors)
#     for quote, author in zip(quotes, authors):
#         print(quote.text + " - " + author.text)

def loadData():
    scrapePage = requests.get("http://quotes.toscrape.com")
    soup = BeautifulSoup(scrapePage.text, "html.parser")
    return soup
   

def quotes(soup):
    quotes = soup.find_all("span", attrs={"class":"text"})
    return quotes

def authors(soup):
    authors = soup.find_all("small", attrs={"class":"author"})
    return authors


def formatData(quotes, authors):
    arr = []

    for quote, author in zip(quotes, authors):
        #print(quote.text + " - " + author.text)
        arr.append(quote.text + " - " + author.text)

    return arr


def printData():
    for quote, author in zip(quotes, authors):
        print(quote.text + " - " + author.text)

    for author in authors:
        print(author.text)





    

