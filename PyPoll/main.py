import csv

#find csv file path
csvpath = "/Users/yuhsichen/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

#read csv path

       
#The total number of votes cast
votes_count = 0
with open (csvpath, 'r') as csvfile:

    pypoll = csv.reader(csvfile, delimiter=',')
    next(pypoll,None)
    for row in pypoll:
        votes_count = votes_count + 1
print("Election Results")
print("---------------------------------------------")
print("Total votes:"+ str(votes_count))
print("---------------------------------------------")

#A complete list of candidates who received votes
candidates_list = []

with open (csvpath, 'r') as csvfile:

    pypoll = csv.reader(csvfile, delimiter=',')
    next(pypoll,None)
    for row in pypoll:
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            

# The percentage of votes each candidate won
CCS_vote_count = 0
DD_vote_count = 0 
RAD_vote_count = 0

with open (csvpath, 'r') as csvfile:

    pypoll = csv.reader(csvfile, delimiter=',')
    next(pypoll,None)
    for row in pypoll:
        if row[2] == "Charles Casper Stockham":
            CCS_vote_count = CCS_vote_count + 1

        elif row[2] == "Diana DeGette":
            DD_vote_count = DD_vote_count + 1

        elif row[2] == "Raymon Anthony Doane":
            RAD_vote_count = RAD_vote_count + 1



CCS_vote_percent = (CCS_vote_count/votes_count)*100
DD_vote_percent = (DD_vote_count/votes_count)*100
RAD_vote_percent = (RAD_vote_count/votes_count)*100



#The total number of votes each candidate won





#The winner of the election based on popular vote.
vote_count_list= [CCS_vote_count, DD_vote_count, RAD_vote_count]
final_list = list(zip(vote_count_list,candidates_list))

print(f"{candidates_list[0]} : {CCS_vote_percent}% ({CCS_vote_count})")
print(f"{candidates_list[1]} : {DD_vote_percent}% ({DD_vote_count})")
print(f"{candidates_list[2]} : {RAD_vote_percent}% ({RAD_vote_count})")
print("---------------------------------------------")


Highest_votes, Winner = max(final_list)
print(f"Winner is {Winner} and he/she wins {Highest_votes} votes")
print("---------------------------------------------")










