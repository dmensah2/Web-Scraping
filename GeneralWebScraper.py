#Author: Deidre Mensah
#Date: 05/04/2020
#Webscraping addresses from scraper friendly sites

#import modules
import requests, csv

#imports Beautfiul soup library
from bs4 import BeautifulSoup

#opens your csv
output = open("test.csv", "wb")
#defines fields of csv
writing = csv.DictWriter(output, fieldnames=["State", "City", "Address"])
#writes the field names to a csv

#gets url with get function from requests library
webpage_response = requests.get('https://www.bebitalia.com/en/stores')

#stores content of the response into webpage variable
webpage = webpage_response.content

#converts HTML document into Beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

#grabs each store visible on page
containers = soup.find_all(attrs={"class":"padd"})

#checks how many containers there are on the page
print (len(containers))

#grabs all separate store page lists for each state
for store in containers:
    state = store.select("h3")[0].get_text()
    city = store.select("h1")[0].get_text().split(",",1)[0] #split function splits 1 time and takes the first part of the piece (or list)
    address = store.select("p", attrs={"class":"css-1nc"})[0].get_text("|").split("|",1)[0] #puts pipe between the text and that splits it by that new delimeter and only grabs first item [0]
    row = {"State": state, "City":city, "Address": address}
   # writing.writerow(row)
    print (state + ", " + city + ", " + address)

