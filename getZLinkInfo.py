import csv
import datetime
import urllib2
import time


def ZData():

	start = time.time()
	now = datetime.datetime.now()
	
	name = str(datetime.datetime.now().date()) + ".csv"
	
	file_1 = open("ListOfURLs.txt", "r+") 
	file_2= open(name, "w")

	urlArray = file_1.readlines()

	results = []

	file_2.write("The data in the file was created at " + str(now)+ '\n')
	print "Processing..."
	for urlcsv in urlArray:
		try: 
			response = urllib2.urlopen(urlcsv)
			cr = csv.reader(response)
			count = -1
			
			for row in cr:
				count = count + 1
					
			file_2.write(row[1] + "," + str(count) + '\n')
		except: 
			print urlcsv + " failed! "
	end = time.time()
	print (end - start) 
	print "Success! Check the " + name + " file."


ZData()
