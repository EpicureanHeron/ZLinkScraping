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
	# not sure if this part is working, tested in Ames and...internet is not good.
	# the 'a' should append the data at the end of the file
	log = open("log.txt", "a")

	urlArray = file_1.readlines()

	results = []

	file_2.write("The data in the file was created at " + str(now)+ '\n')
	print "Processing..."
	for urlcsv in urlArray:
		# to cut down on processing time I should try to just read how many rows, rather than clicking through each row (which is very ineffecient)
		# SO link https://stackoverflow.com/questions/16108526/count-how-many-lines-are-in-a-csv-python

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
	totalTime = (end-start)
	# hopefully appends the run time on the log, just so we are tracking it. Would like to get a current baseline in there.
	log.append(str(now) + ": " + str(totalTime) + '\n') 
	print "Success! Check the " + name + " file."


ZData()
