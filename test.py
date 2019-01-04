import urllib.request
import csv 

# test = 'http://z.umn.edu/shortener/urls/168552/csv/click_data.csv'

test = 'http://z.umn.edu/shortener/urls/154723/csv/click_data.csv'

#test = 'https://google.com'
request = urllib.request.Request(test)
print(request)
response = urllib.request.urlopen(request)
renderedResponse = response.read()

renderedCSV = csv.reader(renderedResponse, dialect='excel', 'rt')

for x in renderedCSV:
    print(x)
# print(response)

# test2 = 'https://z.umn.edu/shortener/urls/168552/csv/click_data.csv'

# request2 = urllib.request.Request(test2)
# print(request2)
# response2 = urllib.request.urlopen(request2)

# print(response2)