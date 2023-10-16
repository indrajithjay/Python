# Array Functions
import csv

a = [1, 2, 3] # creating an array with integer type

for i in range(0, 3): #traversing through each element
    print(a[i]) #print the value

header = ['name', 'Age'] #create header
data = ['John', 62] #create data

f = open('list.csv', 'w') #open a file from the destination path to list.csv
writer = csv.writer(f) #create the csv writer
writer.writerow(header) #write the header
writer.writerow(data) #write the data
f.close()