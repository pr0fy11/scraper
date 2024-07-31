from bs4 import BeautifulSoup 
import requests
import csv

cars = requests.get("https://www.mobile.bg/")
soup = BeautifulSoup(cars.text,"html.parser")
names = soup.findAll("div", attrs={"class":"ime"})
prices = soup.findAll("div", attrs={"class":"cena"})
file = open("scrapedData.csv", 'w')
writer = csv.writer(file)

writer.writerow(["TITLE", "PRICE"])

for name, price in zip(names, prices):
    print(name.text + ' ' + price.text)
    writer.writerow([name.text, price.text])
file.close
