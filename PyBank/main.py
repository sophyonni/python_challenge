import csv
import os
csvpath = os.path.join("budget_data.csv")



data=[]
profits_losses=[]
list_profit_losses = []
previous_value = 0
# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    record = list (csvreader)
    #print (record)
    num_of_months=len(record)
    #print (num_of_months)
    # Loop through looking for the budget_data
  
    for row in record:
            #print(row)  
            amount = row[1]
            #print (amount)
            profits_losses.append (int(amount))
            profit_losses_changes = int (row[1]) - previous_value
            previous_value = int(row[1])
            list_profit_losses.append (profit_losses_changes)
    new_list=list_profit_losses[1:]
    #print(new_list)
    #print(list_profit_losses)
    totalpl = sum(profits_losses)
    avg=sum(new_list)/len(new_list)
    increase = max(new_list)
    decrease = min(new_list)




    #printing
output = (f'''financial analysis
--------------
Number of months: {num_of_months}
Total Proft/Losses: ${totalpl}
average change: {avg}
{increase}
{decrease}''')

print (output)

with open("output.txt", 'w') as file:
      file.write(output)