# total number of months included in the dataset
# Net total amount of "Profit/Losses" over the entire period
# Avg of the changes in "Profit/Losses" over the entire period
# Greatest increase in profits (date and amount) over the entire period
# Greatest decrease in losses (date and amount) over the entire period
#-----------------------------------------------------------------

import os
import csv
#SAVE current work dir. this will allow us to know where we are. Also helps top errors.
cwkdir = os.getcwd()
filepath = os.path.join( cwkdir,'PyBank','budget_data1.csv')
textfile = os.path.join("PyBank", "PyBankAnalysis.txt")

# Starting variables we will use
total_months = []
total_profitloss = []
monthly_profit_change = []
 
# SAVE THIS FOR FUTURE CSV STUFF. This is basically a default CSV read-only file. 
with open(filepath,newline="", encoding="utf-8") as budget:

     #Lets us put our data in the variable CSV.
    csvreader = csv.reader(budget,delimiter=",") 

    # We are skipping the header to have just data.
    header = next(csvreader)  

    # Iterate through all rows.
    for row in csvreader: 

        # Append the months and profit/loss by their appropriate rows.
        total_months.append(row[0])
        total_profitloss.append(int(row[1]))

    # Iterate through to get difference between months
    for i in range(len(total_profitloss)-1):
        
        # Difference between months.
        monthly_profit_change.append(total_profitloss[i+1]-total_profitloss[i])
        
# This will give max and min values.
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Will tie max/min to the correct month. Use +1 or it'll be thrown off.
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1 
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# Print.
output = (
    f"PyBank Financial Analysis\n"
    f"____________________________\n"
    f"Total Months: {len(total_months)}\n"
    f"Total: ${sum(total_profitloss)}\n"
    f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n"
    f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n"
    f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n"
)
print(output)

with open(textfile, "w") as txt_file:
    txt_file.write(output)