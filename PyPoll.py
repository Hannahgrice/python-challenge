import csv

# CSV file path
csv_file = 'election_data.csv'  # Replace 'election_data.csv' with the actual file path

# Initialize variables 
total_votes = 0
candidate_votes = {}

# Open the CSV file and read
with open(csv_file, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Skip header 
    next(csv_reader, None)
    
    # Iterate over each row 
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]  # Assuming 'Candidate' is the third column (index 2)
        candidate_votes[candidate] = candidate_votes.get(candidate, 0) + 1

# Print election results
print("Election Results")
print("----------------------")
print("Total Number of Votes:", total_votes)
print("-----------------------")

# Print individual results
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes}/{total_votes})")

# Find winner
winner = max(candidate_votes, key=candidate_votes.get)
print("-----------------------")
print("Winner:", winner)
print("-----------------------")