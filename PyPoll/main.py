# Importing modules 
import os, csv

# Assigning a variable to the file getting read
path = os.path.join("Resources", "election_data.csv")

#Defining variables/lists
total_votes = 0
votes = [] 
candidate = 0
candidates = []



# Opening the variable storing the file
with open(path) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skiping headers
    if csv.Sniffer().has_header: 
        next(csv_reader)

        for row in csv_reader: 
            total_votes += 1
            candidate = row[2]

        # Adding votes to candidates
        if candidate in candidates: 
            candidate_1 = candidates.index(candidate)
            votes[candidate_1] = votes[candidate_1 + 1]

        # If candidate doesn't exist, add it to candidate list
        else: 
            candidates:append(candidate)
            votes.append(1) 

# Printing Results
print("Election Results")
print("-------------------------") 
print(f"Total Votes: {(total_votes)}")   
print("-------------------------")

print("-------------------------")


print("-------------------------")


# Creating/opening a .txt file 
results_file = open("PyPoll_Results.txt", mode = "w")

# Printing Results within the .txt file 
print("Election Results\n")
print("-------------------------\n") 
print(f"Total Votes: {(total_votes)}\n")   
print("-------------------------\n")

print("-------------------------\n")


print("-------------------------\n")

# Finishing results printing
results_file.close()

# Moving .txt file to correct directory
import shutil
shutil.move ("PyPoll_Results.txt", "Analysis")