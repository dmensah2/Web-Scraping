#Author: Deidre Mensah
#Date: 04/26/2020
#Webscraping Addresses from Warby Parker

##PREPARING THE SITE
#import modules
import requests, csv

#imports Beautfiul soup library
from bs4 import BeautifulSoup

#gets url with get function from requests library
webpage_response = requests.get('https://www.warbyparker.com/retail')

#stores content of the response into webpage variable
webpage = webpage_response.content

#converts HTML document into Beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

##WRITE OUT ATTRIBUTES TO CSV
output = open("WarbyParker_Location.csv", "w", newline='')
writer = csv.DictWriter(output, fieldnames=["Name","Address"])
writer.writeheader()

##SPECIFYING ATTRBIUTES TO GRAB FROM HTML DOC
names = soup.find_all(attrs={"class":"css-uuvmxa"})
addresses = soup.find_all(attrs={"class":"css-wseqxu"})

def print_locations(store_names, store_addresses):
    for name, address in zip(names, addresses):
        name_text = name.get_text()
        address_text = address.get_text("|")
        corrected_address_text = address_text
        row = ({"Name": name_text, "Address": corrected_address_text})
        writer.writerow(row)
        print(name_text + ", " + address_text)

print_locations(names, addresses)
