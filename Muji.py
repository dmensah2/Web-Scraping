#Author: Deidre Mensah
#Date: 05/28/2019
# Python program to get a set of
# places according to your search
# query using Google Places API

#import modules
import requests,json
import csv

#opens your csv
output = open(r"C:\Programming\WebScraping\Muji.csv", "wb")
#defines fields of csv
writer = csv.DictWriter(output, fieldnames=["Name", "Address", "Lat", "Long"])
#writes the field names to a csv
writer.writeheader()

# enter your api key here
api_key = ['YOUR_API_KEY']

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
query = input('Search query: ')

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query + '&key=' + api_key)

# json method of response object convert
#  json format data into python format data
x = r.json()

# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']

# keep looping up to length of y
for i in range(len(y)):
    # Print value corresponding to the
    # 'name' key at the ith index of y
    name = (y[i]['name']).encode('ascii', 'ignore')
    address = (y[i]["formatted_address"]).encode('ascii', 'ignore')
    lat = str((y[i]["geometry"]["location"]["lat"]))
    long = str((y[i]["geometry"]["location"]["lng"]))
    row = {"Name": name, "Address": address, "Lat":lat, "Long":long}
    writer.writerow(row)
    print (name + ", " + address + ", " + lat + ", " + long)
