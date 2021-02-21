# Election_analysis_project
Tabulating the results of a local election
Overview of Election Audit: The purppose of this audit was to count all the election ballots used in this election, and provide a statisical breakdown of the results.

Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

Number of votes cast: 369,711
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
Largest County: Denver
Total Votes: 306,055
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This code can be used to tabulate the number of votes for any county given that the data come in the safe raw csv formatting. Some things that could change for larger election would the addtions of occupation, ethnicty, age. 
For these elections we would want to include the same statistical breakdown for each of these categories. To do so we would just follow the same pattern. Ex. This can be done as many times as needed
#ID category row
#ethnicty list
ethnicty_options = []
#ethnicty dictionary
ethnicty_votes = {}
ethnicty_name = row[4]
# count of ethnic votes
        if ethnicty_name not in ethnicty_list:
            ethnicty_list.append(ethnicty_name)
            ethnicty_votes[county_name]= 0
        ethnicty_votes[ethnicty_name] += 1 
        
