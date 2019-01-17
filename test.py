import urllib.request
import csv 
import pandas
# test = 'http://z.umn.edu/shortener/urls/168552/csv/click_data.csv'

test = 'http://z.umn.edu/shortener/urls/154723/csv/click_data.csv'

#test = 'https://google.com'
request = urllib.request.Request(test)
#print(request)
response = urllib.request.urlopen(request)
#print(response)
# reads csv results but not as a csv????? Seems to be the raw response including \n for new lines and all.
# I don't think the response is the csv...so how do i get that ?
# had to decode the renderped response (not sure if 'ASCII' or "utf-8"), however, when I run the decoded data through the below
# counter, it displays as a 5 digit number rather than the expected 77-78. 
# could be the delimiter...or the decoding, not sure which
# similair issue reported here: https://stackoverflow.com/questions/18897029/read-csv-file-from-url-into-python-3-x-csv-error-iterator-should-return-str


renderedResponse = response.read().decode('utf8')
#spamreader = csv.reader(renderedResponse)




with open(renderedResponse, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', newline='\n')
    i = 0
    for x in spamreader:
        print(x)
        print()
        i+=1





# ------------------------


# print(spamreader)
# for row in spamreader:
#     print(row)
# row_count = sum(1 for row in spamreader)
# print(row_count - 1)

#----------------------------
#print(renderedResponse)

## Reads local file and counts the lines 
# MUCH more efficient that previous 

# with open(renderedResponse, 'r') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', newline='\n')
#     print("this triggered")
#     row_count = sum(1 for row in spamreader)
    
#     print(row_count - 1)
        