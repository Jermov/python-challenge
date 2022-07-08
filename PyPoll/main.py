###Instructions for PyPoll
###PyBank Instructions
### import libraries needed to read csv file
import pandas as pd
import os,sys
import numpy as np

###Bring in resources csv (election_data.csv)--issues here
###path=github (for graders to leverage)- causes errors works using pandas. Not gone over in class.
##using raw, copy/paste of link to data without the 'raw' selection results in errors
###Works!
df=pd.read_csv("C:/Users/jess/Documents/python-challenge/PyPoll/Resources/election_data.csv")
###find the total number of votes cast
item_count=df.shape[0]
##print out results formatted the way displayed in readme file

#create variables to store the count of all each candidate's votes
charles_count=np.sum(df['Candidate']=='Charles Casper Stockham')
diana_count=np.sum(df['Candidate']=='Diana DeGette')
raymon_count=np.sum(df['Candidate']=='Raymon Anthony Doane')
#create variables to store percentage of the vote each candidate received
charles_pct=round((charles_count/item_count*100),3)
diana_pct=round((diana_count/item_count*100),3)
raymon_pct=round((raymon_count/item_count*100),3)
#print out the results of count and percent for each candidate and formatted to match 'ish' the readme file

#Determining winner- if statement to determine which candidate had the most votes and formatting to match 'ish' the readme file
if diana_pct > raymon_pct and diana_pct>charles_pct:
    print("Winner: Diana DeGette")
elif raymon_pct>diana_pct and raymon_pct>charles_pct:
    print("Winner: Raymon Anthony Doane")
elif charles_pct>diana_pct and charles_pct>raymon_pct:
    print("Winner: Charles Casper Stockham")
print("------------------------------------------------")

##Solution to push the output both to terminal and to an analysis file

f = open('c:\\Users\\jess\\Documents\\python-challenge\\PyPoll\\analysis\\analysis.txt','w')
output_results="Election Results\n"
output_results=output_results+"------------------------------------------------\n"
output_results=output_results+ "Total Votes:     "+ str(item_count)+"\n"
output_results=output_results+ "------------------------------------------------"+"\n"
output_results=output_results+"Charles Casper Stockham: " +(str(charles_pct)) +'%'+    "   (" +(str(charles_count)) +")\n"
output_results=output_results+"Diana DeGette: " +(str(diana_pct)) + '%'+  "   (" +(str(diana_count)) +")\n"
output_results=output_results+"Raymon Anthony Doane: " +(str(raymon_pct)) +'%'+   "   (" +(str(raymon_count)) +")\n"
output_results=output_results+"------------------------------------------------\n"
output_results=output_results+"Winner: Diana DeGette\n"
output_results=output_results+"------------------------------------------------\n"



print(output_results)
f.write(output_results)
f.close()

