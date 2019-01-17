import pandas as pd
file_1 = open("ListOfURLs.txt", "r+") 
urlArray = file_1.readlines()
for url in urlArray:


    data = pd.read_csv(url)
    print(data.shape[0] -1)

#print(data)

## THIS DISPLAYS THE ROWS!!! 
