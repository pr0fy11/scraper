from bs4 import BeautifulSoup 
import requests


cars = requests.get("https://www.mobile.bg/")
soup = BeautifulSoup(cars.text,"html.parser")
names = soup.findAll("div", attrs={"class":"ime"})
prices = soup.findAll("div", attrs={"class":"cena"})

for name in names:
    print(name.text)
for price in prices:
    print(price.text)