#import csv statement to be able to use open and csv reader.
import csv

#creating the two lists that will hold both the voter ID's and the votes
voter_id = []
votes = []

#csv reader syntax
with open ("election_data.csv", 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Reads each row from the .csv file
    for row in csvreader:

        #appends each row element to the respective working list
        voter_id.append(row[0]) #row[0] is the voter ID column
        votes.append(row[2]) #row[2] has the name of the candidate the respective voter_id casted their vote for

#Taking out the first element of the data lists, which are just the columns' headers
voter_id.pop(0)
votes.pop(0)

#Creates a set by adding all the elements in the voter_id list 
seen = set()
for row in voter_id: 
    seen.add(row)

#Compares the "seen" set's length with the length of the original voter_id list
#If the set and the list have different lengths, then there was a repeated voter_id in the list, which might imply double voting.
if (len(seen) != len(voter_id)):
    print("There seems to have been double voting in this election.")

#Prints the number of votes casted in the election
total_votes = len(votes)

#Creates a new set that will contain single names for the candidates
candidates_set = set()

for row in votes:
    candidates_set.add(row)

#Since the set is not hashable, a candidates_list containing a single name for each candidate was created 
candidates_list = []
i = 1
for i in range(len(candidates_set)):
    candidates_list.append(candidates_set.pop())
    i += 1

#This list is created to hold size 2 lists with each candidate and the number of votes they got
final_counting = []

for item in candidates_list:
    counter = 0
    for row in votes:
        if row == item:
            counter += 1
    final_counting.append([counter, item])

#The list is then sorted in descending order
final_counting.sort(reverse = True)

#Creates a function that will print "-" a specified number of times
def dash_line(num):
    dash_line = ""
    for dash in range(num):
        dash_line = dash_line + "-"
    return dash_line

#Prints the report
print("Election Results")
print(dash_line(25))
print(f"Total Votes: {total_votes}")
print(dash_line(25))

#The for each loop will calculate the percent of votes that each candidate got and prints them to the report
for item in final_counting:
    percent = item[0]/total_votes
    print("{}: {:.2%} ({})".format(item[1],percent,item[0]))

print(dash_line(25))

#Since the greatest number of votes will be in the first element, the first element of the "final_counting" list will hold the winner
print(f"Winner: {final_counting[0][1]}")

#Prints the report to a text file "pypoll.txt"
output =  open ("pypoll.txt", 'w')

line = dash_line(25)+"\n"
output =  open ("pypoll.txt", 'w')

output.write("Election Results\n")
output.write(line)
output.write(f"Total Votes: {total_votes}\n")
output.write(line)
for item in final_counting:
    percent = item[0]/total_votes
    output.write("{}: {:.2%} ({})\n".format(item[1],percent,item[0]))
output.write(line)
output.write(f"Winner: {final_counting[0][1]}\n")
output.write(line)

output.close()