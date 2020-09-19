#Author: Deidre Mensah
#Date: 05/23/2020
#Webscraping addresses from SB One Bank
#import modules
import requests, csv

#imports Beautfiul soup library
from bs4 import BeautifulSoup

#opens your csv
output = open("SBOneBank.csv", "w", newline='')
#defines fields of csv
writing = csv.DictWriter(output, fieldnames=["Name", "Address"])
#writes the field names to a csv
writing.writeheader()

#gets url with get function from requests library
webpage_response = requests.get('https://www.sbone.bank/locations')

#stores content of the response into webpage variable
webpage = webpage_response.content

#converts HTML document into Beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

#grabs each store visible on page
containers = soup.findAll(attrs={"class":"addr-sec"})

#checks how many containers there are on the page
print (len(containers))

#grabs all separate store page lists for each state
for store in containers:
    name = store.select("h4")[0].get_text()
    address = store.select("p")[0].get_text()
    city = store.select("p")[1].get_text() #split function splits 1 time and takes the first part of the piece (or list)
    row = {"Name":name, "Address": address + ", " + city}
    writing.writerow(row)
    print (name + ", " + city +  ", " + address)