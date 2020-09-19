#Author: Deidre Mensah
#Date: 05/04/2020
#Webscraping addresses from scraper friendly sites

#import modules
import requests, csv

#imports Beautfiul soup library
from bs4 import BeautifulSoup

#opens your csv
output = open("LaPerla.csv", "w", newline='')
#defines fields of csv
writing = csv.DictWriter(output, fieldnames=["Address"])
#writes the field names to a csv
writing.writeheader()

#gets url with get function from requests library
webpage_response = requests.get('https://www.laperla.com/us/stores')

#stores content of the response into webpage variable
webpage = webpage_response.content

#converts HTML document into Beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

#grabs each store visible on page
containers = soup.findAll(attrs={"class":"store"})

#checks how many containers there are on the page
print (len(containers))

#grabs all separate addresses on the page
for store in containers:
    address = (store.p).get_text().encode("utf-8")
    row = {"Address": address}
    writing.writerow(row)
    print (address)