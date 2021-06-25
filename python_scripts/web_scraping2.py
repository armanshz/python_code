# simple webscraping practice
import requests
from bs4 import BeautifulSoup
url = "https://scrapingclub.com/exercise/list_basic/?page=1"
# points the script to the url to be parsed
response = requests.get(url)
# collects all the html from the webpage using response.text, and using the lxml parser to parse through it
soup = BeautifulSoup(response.text,"lxml")
items = soup.find_all("div",class_="col-lg-4 col-md-6 mb-4")
count=1
for i in items:
    itemName = i.find("h4",class_="card-title").text
    itemPrice = i.find("h5").text
    print(count,") price: ",itemPrice,", item name: ", itemName)
    count+=1
