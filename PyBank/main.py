# Import the os module 
import os 

# Import the csv reader module 
import csv 

# Assign a variable to the file getting read
path = os.path.join("budget_data.csv")

r_index = 1
months = 0 
total = 0
change_date = []
earnings = []


# "Open" the variable storing the file
with open(path) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skip headers
    if csv.Sniffer().has_header: 
        next(csv_reader)

        fst_row = next(csv_reader)
        income = int(fst_row[1])
        months += 1
        total += int(fst_row[r_index])

    for row in csv_reader: 
        months += 1
        change_date.append(row[0])

        total = total + int(row[1])

        # Profit/Loss avg. change
        income_change = int(row[1]) - income
        earnings.append(income_change)
        income = int(row[1])
    
    avg_income_chage = round((sum(earnings)/len(earnings)), 2)
