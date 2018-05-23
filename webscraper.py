import csv
import datetime
import urllib2

def ZData():

	now = datetime.datetime.now()
	
	name = str(datetime.datetime.now().date()) + ".txt"
	
	
	
	file_1 = open("ListOfURLStest.txt", "r+") 
	file_2= open(name, "w")

	#https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python

	#I could create a text file that can be read in as a list (or dictionary with URL : CR#) which prints its findings puts it in another file based on the count

	urlArray = file_1.readlines()

	results = []

	

	file_2.write("The data in the file was created at " + str(now)+ '\n')

	for urlcsv in urlArray:
		response = urllib2.urlopen(urlcsv)
		cr = csv.reader(response)
		count = -1
		
		for row in cr:
			count = count + 1
		
		
		file_2.write(row[1] + " " + str(count) + '\n')

	#' '.join('{}{}'.format(key, val) for key, val in results.items())

	print "Success! Check the Results.txt file."


ZData()


# https://z.umn.edu/shortener/urls/154734/csv/click_data.csv URL for CR13 before clicked the export to CSV button, the screen defaults in on "last 24 hours" which is 0 currently and aftering
# running this program it returns 51 which is the all time amount

#After hitting the "export to csv" button I got this URL https://z.umn.edu/shortener/urls/154734/csv/click_data.csv and it is sitll on the graph for the last 24 hours, still at 51

#Click on last 30 days, the url https://z.umn.edu/shortener/urls/154734/csv/click_data.csv the data still shows as 51 and 


#I'm not sure how the csv data works...the URL doesn't change but the data CAN change and it doesn't seem to be dictated by the tab using. I have got data that is not the "all time data"...but I can't recreate that for w/e reason