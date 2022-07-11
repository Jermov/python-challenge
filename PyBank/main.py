###PyBank Instructions
### import libraries needed to read csv file
import pandas as pd
import os,sys
import numpy as np

###Bring in resources csv (budget.csv)--issues here
df=pd.read_csv("C:/Users/jess/Documents/python-challenge/PyBank/Resources/budget_data.csv")
item_count=df.shape[0]

###collecting net total amount of "Profit/Losses" over the entire period
toadi=sum(df["Profit/Losses"])
print("Total:            ",toadi)

# OOL variables
##Finding total row count to loop through data (pandas counts every cell- this dataframe has two columns
##Dividing the df.size by number of columns gives me the last row number
csv_length = df.shape[0]
# \o/ \o/ \o/

##if loop checks and no previous profit/loss is found, sets profit/loss to 0 as initial amount
previous_pl = 0
##stepper to increment and move to next row
stepper = 0
##sets initial amount for total difference between first profit/loss and before it (unknown values)
total_running_difference = 0
##sets initial lowest row (greatest decrease in profits) to zero prior to beginning loop
lowest_row = 0
##sets initial highest row (greatest increase in profits) to zero prior to beginning loop
highest_row = 0
# STEP THROUGH ROWS
##as long as the stepper count is less than the last row count do the following loop
 # READ NEXT profit/loss CELL
 # STORE DIFFERENCE AS VARIABLE to compare through the loop
 # ADD DIFFERENCE TO THE RUNNING 'DIFF' TOTAL
  ##checks if the variable set to lowest_row (greatest decrease) was found within profit/losses, to print the row (date and profit/loss) of that rownum
  ##checks if the variable set to highest_row (greatest increase) was found within profit/losses, to print the row (date and profit/loss) of that rownum
while stepper < csv_length:
  current_pl = df.at[stepper,"Profit/Losses"]
  diff = current_pl - previous_pl
  if current_pl < df.at[lowest_row,"Profit/Losses"]:
    lowest_row = stepper

  if current_pl > df.at[highest_row,"Profit/Losses"]:
    highest_row = stepper

# INCREASE COUNTER
  stepper = stepper + 1
# SET CURRENT PL TO 'PREVIOUS' PL
  previous_pl = current_pl
# RESTART LOOP
#name the average change and set decimal places to prevent the 20 decimals it was spitting out
avg=round(total_running_difference/stepper,2)
# STEPPER = # OF ROWS
# total_running_difference = the total of the 'DIFFERENCES'
# Therefore, total_running_difference / stepper should be the average
#-------------------------------------
#-------------------------------------

##last instruction was to write print statements both in terminal and as a file- used stdout and saved as txt file
f = open('c:\\Users\\jess\\Documents\\python-challenge\\PyBank\\analysis\\analysis.txt','w')
output_string = "Financial Analysis\n"
output_string = output_string + "-----------------------------------------------------------------\n"
output_string = output_string + "Total Months:     " + str(item_count) + "\n"
output_string = output_string + "Total:            " + str(toadi) + "\n"
output_string = output_string + "Greatest Increase in Profits: "+ df.at[highest_row,"Date"] + "     ("+str(df.at[highest_row,"Profit/Losses"])+")\n"
output_string = output_string + "Greatest Decrease in Profits: "+ df.at[lowest_row,"Date"] + "     ("+str(df.at[lowest_row,"Profit/Losses"])+")\n"
print(output_string)
f.write(output_string)
f.close()
