import pandas as pd
import time
import datetime
import os

def getZLinkInfo():
	start = time.time()
	now = datetime.datetime.now()
	cwd = os.getcwd()
	name = cwd + '/ZLinkScraping/' + str(datetime.datetime.now().date()) + ".csv"
	file_1 = open(cwd + "/ZLinkScraping/ListOfURLs.txt", "r+") 
	file_2= open(name, "w")
	log = open(cwd + "/ZLinkScraping/log.txt", "a")
	urlArray = file_1.readlines()
	file_2.write("The data in the file was created at " + str(now)+ '\n')
	print("Processing...")

	for url in urlArray:

		data = pd.read_csv(url)
		try:
			file_2.write(data.iloc[0, 1] + "," + str(data.shape[0]) + '\n')
		except:
			file_2.write("keyword, 0" + '\n')

	end = time.time()
	totalTime = (end-start)
	log.write("date: " +str(now) + ", runtime: " + str(totalTime) + '\n') 
	print("Success! Check the " + name + " file.")

getZLinkInfo()
