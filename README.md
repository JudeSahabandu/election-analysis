# Auditing Election Results of the US Congressional Precinct of Colorado
---

## Overview - Election Audit

### Determining Audit Requirement

The US Congressional Precinct of Colorado has carried out thier elections. Post elections, the election audit team has obtained the final csv file containing all the election results, which need to be analysed using Python to determine the election outcome.

As part of the prework leading to the requirement of finalizing the election results, the python script included code to determine the following;

1. Total votes cast in the election
2. Identifying the list of candidates who ran for the election
3. Determining each candidate vote count and vote percentage
4. Identifying the winning candidate of the election
5. Determining the winning candidate's vote count and vote percentage

Post establishing the above, the next requirement was to determine the following;

2. Identifying the list of counties where the election was held
3. Determining each counties vote count and vote percentage
4. Identifying the largest county turnout of the election

Once the Python script was written to extract the data from the csvfile, the data was required to print through the following outputs;

1. Printing the election results to the command line
2. Saving the election results to a text file

The sections below highlight the approach towards writing Python script to obtain the above outputs.

## Election Audit Results

* ### Votes cast in the Colorado congressional election

When calculating total votes cast in the election, we need to first initialize a variable and equate it to 0.

This is done in the PyPoll_Challenge script using the following code: `total_votes = 0`

Once created the variable and intitalized to 0, the next step is to increase the variable by 1 as we iterate through the loop: `total_votes = total_votes + 1`

It is also worth noting to use `headers = next(file_reader)` statement to skip the header row of the file.

Once we run the code and use the `print` statement, we will get the total vote count output as 369,711 votes.

* ### Breakdown of vote count and vote percentage by county

Once we have obtained the total number of votes cast in the election, one of the key outputs is to determine the vote count and percentage by participating counties within the overall vote.

The participating list of counties were Jefferson, Denver and Arapahoe.

When determining the vote count by county, we first declared an empty dictionary using `county_votes = {}`.  

Once declared, the next step was to create a key for the unique counties. 

The following code needs to be executed inside an `if` statement. This is done to initiate each county as a key.

```
#Get the county name from each row.
        county_name = row[1]

#If the county does not match any existing county add it to the county list
        if county_name not in county_list:

#Add the county name to the county list.
            county_list.append(county_name)

#And begin tracking that counties voter count.
            county_votes[county_name] = 0

#Add a vote to that counties count
        county_votes[county_name] += 1
```

We need to ensure proper indents are used in the above scenario in order for the code to run correctly. 

To obtain vote percentages, the following block of code was used to obtain the percentage output;

```
for county_name in county_votes:

        # Retrieve the county vote count.
        county = county_votes.get(county_name)

        # Calculate the percentage of votes for the county.
        county_percentage = float(county) / float(total_votes) * 100

        # Print results as;
        county_results = (f"{county_name}: {county_percentage:.1f}% ({county:,})\n")
```

Once we run the code and use the `print` statement, we will get the county vote output as follows;

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

* ### County with the largest vote count

To identify the largest county of the election, first we declared the following variables and assigned them appropriate values;

`largest_county = ""`           - declare variable holding an empty string

`winning_county = 0`            - declare variable equal to 0 for winning county

`winning_county_percentage = 0` - declare variable equal to 0 for winning county percentage

Once the variables were declared, an if statement is required to obtain the winning county and its vote count.

```
if (county > winning_county) and (county_percentage > winning_county_percentage):
            winning_county = county
            largest_county = county_name
            winning_county_percentage = county_percentage
```

We can use the `print` statement to get the declaration of the largest county within an f-string.

* ### Breakdown of vote count and vote percentage by running candidate

One of the key outputs is to determine the vote count and percentage by running candidates within the overall vote.

The participating list of candidates were Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane.

When determining the vote by candidate, we declared an empty dictionary using `candidate_votes = {}`.  

Once declared, the next step was to create a key for the unique candidates. 

The following code needs to be executed inside an `if` statement. This is done to initiate each candidate as a key.

```
#Get the candidate name from each row.
        candidate_name = row[2]

#If the candidate does not match any existing candidate add it to
#the candidate list
        if candidate_name not in candidate_options:

#Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

#And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

#Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
```

We need to ensure proper indents are used in the above scenario in order for the code to run correctly. 

To obtain vote percentages, the following block of code was used to obtain the percentage output;

```
for candidate_name in candidate_votes:

#Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```

Once we run the code and use the `print` statement, we will get the county vote output as follows;

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

* ### Election data of winning candidate

Finally to determine the winning candidate of the election, first we declared the following variables and assigned them appropriate values;

`winning_candidate = ""` - declare variable holding an empty string

`winning_count = 0`      - declare variable equal to 0 for winning county

`winning_percentage = 0` - declare variable equal to 0 for winning county percentage

Once the variables were declared, an if statement is required to obtain the winning county and its vote count.

```
if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```

We can use the `print` statement to get the declaration of the largest county within an f-string.


## Summary

### Refactoring Script - Run for any election


