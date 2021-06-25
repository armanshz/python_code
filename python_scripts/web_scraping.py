# simple web scraper to get quotes from website - from LinkedIn Learning course

import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
# points the script to the url to be parsed
response = requests.get(url)
# collects all the html from the webpage using response.text, and using the lxml parser to parse through it
soup = BeautifulSoup(response.text,"lxml")
# soup.find_all("tag_name", class_"name" that the information is stored in)
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small",class_="author")
tags = soup.find_all("div",class_="tags")
for i in range(len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
# extra for loop to drill down the "a" tag, into the "tag" class
    quoteTags = tags[i].find_all("a",class_="tag")
    # tag.text extracts the actual text inside the "tag" class, inside the "a" tag
    for tag in quoteTags:
        print(tag.text)