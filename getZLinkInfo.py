import csv
import datetime
import urllib2

def ZData():

	now = datetime.datetime.now()
	
	name = str(datetime.datetime.now().date()) + ".csv"
	
	file_1 = open("ListOfURLs.txt", "r+") 
	file_2= open(name, "w")

	urlArray = file_1.readlines()

	results = []

	file_2.write("The data in the file was created at " + str(now)+ '\n')

	for urlcsv in urlArray:
		response = urllib2.urlopen(urlcsv)
		cr = csv.reader(response)
		count = -1
		
		for row in cr:
			count = count + 1
				
		file_2.write(row[1] + "," + str(count) + '\n')

	print "Success! Check the" + name + " file."


ZData()