# Z Link Scraping

## Problem
z.umn.edu provides URL shortening, however when a collection of z links are created, it becomes cumbersome to manually click through each separate z link. Furthermore, to track data on a weekly basis requires this task to be done ad nauseam. 


## Solution
Utilizing Python  along with the libraries Pandas, datetime, and urllib2 all of the data can be scraped and put into a .csv file.

## Set Up

In order to get the program to work, a .txt files must exist (in this repo there is a sample one provided) which is called "ListOfURLs.txt". 

Each z link has a public facing .csv file associated with it. In the .txt file, each z link's .csv should be listed out. 

To get a z links .csv location do the following:

* Log into [z.umn.edu](z.umn.edu)
* Click on the number listed in the "Clicks" column  
* On the "Information about your link" page, right click on the "Export to CSV" button
* Select "Copy Link Address"
* Paste link 
* Navigate back to the list of z links associated with your account and repeat the previous steps

The .txt file should end up looking like this:

```
https://z.umn.edu/shortener/urls/111111/csv/click_data.csv
https://z.umn.edu/shortener/urls/111112/csv/click_data.csv
https://z.umn.edu/shortener/urls/111113/csv/click_data.csv
https://z.umn.edu/shortener/urls/111114/csv/click_data.csv

```
Note that each z link is its own line.

For whatever reason, the path to get the .csv requires a log in, but the .csv files themselves are public facing.

## Running the program

* Navigate to the directory in terminal or powershell
* Enter the command `python getZLinkInfo.py`
* Program will run and produce a dated .csv file with the results



## .bat file

A .bat file is included but only works on my local machine. Need to recode or not include it. 
