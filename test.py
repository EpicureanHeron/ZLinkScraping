import urllib.request
import csv 

# test = 'http://z.umn.edu/shortener/urls/168552/csv/click_data.csv'

test = 'http://z.umn.edu/shortener/urls/154723/csv/click_data.csv'

#test = 'https://google.com'
request = urllib.request.Request(test)
print(request)
response = urllib.request.urlopen(request)
print(response)
# reads csv results but not as a csv????? Seems to be the raw response including \n for new lines and all.
# I don't think the response is the csv...so how do i get that ?
renderedResponse = response.read()
print(renderedResponse)

## Reads local file and counts the lines 
# MUCH more efficient that previous 
with open('click_data.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    row_count = sum(1 for row in spamreader)
    
    print(row_count)
        