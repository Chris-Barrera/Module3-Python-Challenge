import csv
import os


my_report = open('Analysis/Report.txt', 'w')
data = csv.DictReader(open('Resources/election_data.csv'))

votes = 0
totals = 0
can_options = []
can_votes = {}

top_can = ""
top_count = 0
top_per = 0

for row in data:
    votes += 1

    candidate_name = row["Candidate"]
    
    ballots = int(row["Ballot ID"])
    
    totals += ballots 

    if candidate_name not in can_options:
        
        can_options.append(candidate_name)

        can_votes[candidate_name] = 0

    can_votes[candidate_name] += 1



output = f'''
   Election Results
-------------------------
Total Votes: {votes}
-----------------------------------'''


for candidate_name in can_votes:

        vote_count = can_votes[candidate_name]

        vote_per = float(vote_count)/float(votes) * 100

        can_results3 = (f"{candidate_name}: {vote_per:.1f}%) ({vote_count:,})\n")
        output += can_results3


output += '''-------------------------

Winner Diana DeGette'''


print(output)
my_report.write(output)