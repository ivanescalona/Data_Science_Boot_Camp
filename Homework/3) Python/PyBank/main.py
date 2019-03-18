#import csv statement to be able to use open and csv reader.
import csv

#Creates the new list to store the data from the file
data = []

#csv reader syntax
with open ("budget_data.csv", 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Reads each row from the .csv file
    for row in csvreader:
        #appends each row element to the data list
        data.append(row)

#Taking out the first element of the data list, which are just the titles
titles = data.pop(0)

#initializes an int variable to 0. This will be used to sum all the profits and losses
total = 0

#sums all the profits and losses
for row in data:
    total += int(row[1])

#Initializing two variables that will be included in the following for loop.
total_change = 0
average = 0.0

#For loop for adding all the changes between profit/loss in two consecutive months
for i in range(1,len(data)):
    change = int(data[(i)][1])-int(data[(i-1)][1])
    total_change += change

#The average of change will be total change divided by the number of points - 1 
average = total_change/(len(data)-1)

#Initializing greatest increase list which will hold a string (destined for the date) and an int (destined for the value of max profit)
great_inc = ["",0]

#Initializing greatest decrease list which will hold a string (destined for the date) and an int (destined for the value of max loss)
great_dec = ["",0]

#For loop that compares all the values in the data list and determines which ones are the greatest increase and decrease in profit and loss respectively
for i in range(1,len(data)):
    if (int(data[i][1]) > great_inc[1]) and int(data[i][1]) > 0:
        great_inc[0] = data[i][0]
        great_inc[1] = int(data[i][1])
    elif (int(data[i][1]) < great_dec[1]) and int(data[i][1]) < 0:
        great_dec[0] = data[i][0]
        great_dec[1] = int(data[i][1])

#Accounts for the possibility of no profits for greatest increase.
if (great_inc[1] == 0):
    great_inc = ["There were no profits", "N/A"]
elif (great_dec == 0): #Accounts for the possibility of no losses for greatest decrease.
    great_dec = ["There were no losses", "N/A"]

#Prints a chain of "-" symbols to the console
dash_line = ""
for dash in range(25):
    dash_line = dash_line + "-"

#Stores all the relevant data to be printed
total1 = "Total Months: {}".format(len(data)) 
total2 = "Total : ${}".format(total)
ave_string = "Average Change: ${}".format(average)
great_inc_str = "Greatest Increase in Profits: {} ${}".format(great_inc[0], great_inc[1])
great_dec_str = "Greatest Decrease in Profits: {} ${}".format(great_dec[0], great_dec[1])

financial1 = "Financial Analisis"

#Prints all the relevant data
print (financial1)
print(dash_line)
print(total1)
print(total2)
print(ave_string)
print(great_inc_str)
print(great_dec_str)

#Prints the report to a text file
output =  open ("pybank.txt", 'w')

output.write(financial1+"\n")
output.write(dash_line+"\n")
output.write(total1+"\n")
output.write(total2+"\n")
output.write(ave_string+"\n")
output.write(great_inc_str+"\n")
output.write(great_dec_str+"\n")

output.close()