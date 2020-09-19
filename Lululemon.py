#Author: Deidre Mensah
#Date: 04/26/2020
#Webscraping Addresses from Bloomingdale's - Applying lessons from CodeAcademy

##PREPARING THE SITE
#import modules
import requests, csv

#imports Beautfiul soup library
from bs4 import BeautifulSoup

#gets url with get function from requests library
webpage_response = requests.get('https://shop.lululemon.com/stores/all-lululemon-stores')

#stores content of the response into webpage variable
webpage = webpage_response.content

#converts HTML document into Beautiful soup object
soup = BeautifulSoup(webpage, "html.parser")

#--------------------
#opens Bloomingdale's csv
output = open("Lululemon.csv", "w", newline='')
#defines fields of csv
writer = csv.DictWriter(output, fieldnames=["Address"])
#writes the field names to a csv
writer.writeheader()
#-----------------------

#specifies attributes to grab from HTML document using BeautifulSoup functions,
#which in this case is a class with a list of all the store links inside
store_links = (soup.find_all(attrs={"class":"store-link basic"}))
#intializes list to append links to
links = []

#loops through each attribute on page with the store-link basic class
for link in store_links:
    #gets URL for each individual page
    webpg_response = link.get("href")
    #gets the HTML document from each URL
    actualpg = requests.get(webpg_response)
    #gets content from each HTML document
    pg_content = actualpg.content
    #parses content as a html
    store_page = BeautifulSoup(pg_content, "html.parser")
    #appends each html file to links list that we we will access later
    links.append(store_page)

for link in links:
    #goes through each html doc and grabs attributes the class that has the address text inside
    store = link.find_all(attrs={"class":"basic contact-link lll-stack-lvl2"})[0].get_text().strip() #the 0 gets the first text element inside, since get_text can only get the 1st bit of text
    row = ({"Address": store})
    #writes row to csv file
    writer.writerow(row)
    print(store)