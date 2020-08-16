# Importing modules 
import os, csv

# Assigning a variable to the file getting read
path = os.path.join("Resources", "budget_data.csv")

# Defining variables/lists
r_index = 1
months = 0 
total = 0
change_date = []
earnings = []

# Opening the variable storing the file
with open(path) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skiping headers
    if csv.Sniffer().has_header: 
        next(csv_reader)

        # First row will start making calculations
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
    
    # Avg. Profit/Loss change throught every month 
    avg_income_chage = round((sum(earnings)/len(earnings)), 2)

    # Greatest increase 
    max_increase = max(earnings)
    max_index = earnings.index(max_increase)
    max_date = change_date[max_index]

    # Greatest decrease
    max_decrease = min(earnings)
    min_index = earnings.index(max_decrease)
    min_date = change_date[min_index]

# Printing Results
print("Financial Analysis")
print("----------------------------") 
print(f"Total Months: {(months)}")   
print(f"Total: ${(total)}")
print(f"Avg. Change: ${(avg_income_chage)}")
print(f"Greatest Increase in Profits: {max_date} (${(max_increase)})")
print(f"Greatest Decrease in Profits: {min_date} (${(max_decrease)})")

# Creating/opening a .txt file 
results_file = open("PyBank_Results.txt", mode = "w")

# Printing Results within the .txt file 
results_file.write("Financial Analysis\n")
results_file.write("----------------------------\n")
results_file.write(f"Total Months: {(months)}\n")   
results_file.write(f"Total: ${(total)}\n")
results_file.write(f"Avg. Change: ${(avg_income_chage)}\n")
results_file.write(f"Greatest Increase in Profits: {max_date} (${(max_increase)})\n")
results_file.write(f"Greatest Decrease in Profits: {min_date} (${(max_decrease)})\n")

# Finishing results printing
results_file.close()

# Moving .txt file to correct directory
import shutil
shutil.move ("PyBank_Results.txt", "Analysis")