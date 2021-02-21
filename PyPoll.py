# The data we need to retrieve
# The total number of votes cast
# A complete list of candidatess who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won 
# The winner of the election based on the popular vote
import  csv
import os
file_to_load = 'election_results.csv'
file_to_save = "election_results.txt"

# Set total votes to 0
total_votes = 0

#Candidate list
candidate_options = []
#Candidate dictionary
candidate_votes = {}

#County list
county_list = []
#County dictionary
county_votes = {}

#largest county
largest_county = ""
#largest county number of voters
lgcounty_count= 0 

#winners values
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
# To Do read and analyze here
    file_reader = csv.reader(election_data) 
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        
        candidate_name = row [2]

        county_name = row [1]
        
        if candidate_name not in candidate_options:
             candidate_options.append(candidate_name)
             candidate_votes[candidate_name] = 0  
        candidate_votes[candidate_name] += 1
       # count of county votes
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name]= 0
        county_votes[county_name] += 1        
    #oercent of county votes
with open(file_to_save, "w") as txt_file:
       
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results) 
    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
            #format vote_percentage to one decimal   
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name  
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        winning_candidate_summary = (
            f"---------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------------\n"
            )
        print(winning_candidate_summary) 
    txt_file.write(winning_candidate_summary)
    for county_name in county_votes:

        cvotes = county_votes[county_name]
        cvote_percentage = float(cvotes) / float(total_votes) * 100   
        county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results,end="")
        txt_file.write(county_results)
        if (cvotes > lgcounty_count):
            lgcounty_count = cvotes
            largest_county = county_name
    largest_county_summary = (
        f"----------------------------------\n"
        f"Largest County: {largest_county}\n"
        f"Total Votes: {lgcounty_count:,}\n"
        f"----------------------------------\n"
        )
    print(largest_county_summary)
    txt_file.write(largest_county_summary)