#Author: Deidre Mensah
#Date: 05/04/2020
#Webscraping addresses from scraper friendly sites

#import modules
import requests, csv

#imports Beautfiul soup library
from bs4 import BeautifulSoup

#opens your csv
output = open("EileenFisher.csv", "wb")
#defines fields of csv
writing = csv.DictWriter(output, fieldnames=["Address","Address_2", "City", "State"])
#writes the field names to a csv
writing.writeheader()

#gets url with get function from requests library
webpage_response = requests.get('https://locations.eileenfisher.com/us/')

#stores content of the response into webpage variable
webpage = webpage_response.content

#converts HTML document into Beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

#grabs each store visible on page
containers = soup.findAll("div", attrs={"class":"info-address"})

#checks how many containers there are on the page
print len(containers)

#grabs all separate store page lists for each state
for store in containers:
    building = store.select("div")[1].get_text()
    city = store.select("div")[2].get_text().split(",",1)[0]#split function splits 1 time and takes the first part of the piece (or list)
    state = store.select("div")[2].get_text().split(",",1)[1]#split function splits 1 time and takes the second part of the piece (or list)
    address = store.select("div")[0].get_text("|") #puts pipe between the text and that splits it by that new delimeter and only grabs first item [0]
    row = {"Address": address, "Address_2": building, "City":city, "State":state}
    writing.writerow(row)
    print (address + ", " + city + "," + state, ", " + building)

