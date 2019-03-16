import csv

employee_id = []
full_name = []
dob = []
ssn = []
state = []

with open('employee_data.csv', 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        employee_id.append(row[0])
        full_name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])

b = len(full_name)
name = []
lastname = []

updated_name = ['Name', 'Lastname']
for i in range(1,b):
    current_name = []
    current_name = ((str(full_name[i]).split()))
    updated_name.append(current_name[0])
    updated_name.append(current_name[1])

year = []
month = []
day = []

for i in range(1,b):
    current_dob = []
    current_dob = str(dob[i]).split("-")
    year.append(current_dob[0])
    month.append(current_dob[1])
    day.append(current_dob[2])

updated_dob = ['DOB']
for i in range(1,b):
    jointdob = month[i-1] + "/" + day[i-1] + "/" + year[i-1]
    updated_dob.append(jointdob)

updated_ssn = ['SSN']

for i in range(1,b):
    current_ssn = []
    current_ssn = str(ssn[i]).split("-")
    updated_ssn.append(current_ssn[2])

for i in range(1,b):
    updated_ssn[i] = "***-**-"+updated_ssn[i]

len(updated_ssn)

us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR','California': 'CA',
'Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE','Florida': 'FL','Georgia': 'GA','Hawaii': 'HI',
'Idaho': 'ID','Illinois': 'IL','Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN','Mississippi': 'MS',
'Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV','New Hampshire': 'NH','New Jersey': 'NJ',
'New Mexico': 'NM','New York': 'NY','North Carolina': 'NC','North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK',
'Oregon': 'OR','Pennsylvania': 'PA','Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD',
'Tennessee': 'TN','Texas': 'TX','Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV',
'Wisconsin': 'WI','Wyoming': 'WY',}

updated_state = ['State']

for i in range(1,b):
    updated_state.append(us_state_abbrev[(state[i])])

output = open('updated_employee_data.csv', 'w')

for i in range(0,b):
    output.write(employee_id[i]+",")
    output.write(updated_name[2*i]+",")
    output.write(updated_name[2*i+1]+",")
    output.write(updated_dob[i]+",")
    output.write(updated_ssn[i]+",")
    output.write(updated_state[i]+",\n")

output.close()