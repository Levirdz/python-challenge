# Importing modules 
import os, csv

# Assigning a variable to the file getting read
path = os.path.join("Resources", "election_data.csv")

#Defining variables/lists
total_votes = 0
votes = [] 
candidate = 0
candidates = []
vote_percentage = []
winner = 0

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
            votes[candidate_1] = votes[candidate_1] + 1

        # If candidate doesn't exist, add it to candidate list
        else: 
            candidates.append(candidate)
            votes.append(1) 

    # Calculate vote % and determine winner
    winner_votes = votes[0]

    for i in range(len(candidates)):
        percentage = round((votes[i]/total_votes)*100,2)
        vote_percentage.append(percentage)

        if votes[i] > winner_votes:
            winner_votes = votes[i]
            winner = i
        elected = candidates[winner]

# Printing Results
print("Election Results")
print("-------------------------") 
print(f"Total Votes: {(total_votes)}")   
print("-------------------------")
for i in range (len(candidates)):
    print(f"{candidates[i]}: {vote_percentage[i]}% ({votes[i]})")
print("-------------------------")
print(f"Winner: {elected}")
print("-------------------------")

# Creating/opening a .txt file 
results_file = open("PyPoll_Results.txt", mode = "w")

# Printing Results within the .txt file 
results_file.write("Election Results\n")
results_file.write("-------------------------\n") 
results_file.write(f"Total Votes: {(total_votes)}\n")   
results_file.write("-------------------------\n")
for i in range (len(candidates)):
    results_file.write(f"{candidates[i]}: {vote_percentage[i]}% ({votes[i]})\n")
results_file.write("-------------------------\n")
results_file.write(f"Winner: {elected}\n")
results_file.write("-------------------------\n")

# Finishing results printing
results_file.close()

# Moving .txt file to correct directory
import shutil
shutil.move ("PyPoll_Results.txt", "Analysis")