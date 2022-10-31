import csv
# find out csv path
csvpath = "/Users/yuhsichen/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

#read csv path
row_count = 0
with open (csvpath, 'r') as csvfile:

    pybank = csv.reader(csvfile, delimiter=',')
    next(pybank,None)
    for row in pybank:
        row_count =  row_count +1

# The toal number of months included in the dataset
print("Financial Analysis")
print("---------------------------------------------")
print("Total Months: " + str(row_count))

#The net total amount of "Profit/Loses" over the entire period
profit_losses = 0 

with open (csvpath, 'r') as csvfile:
    pybank = csv.reader(csvfile, delimiter=',')
    next(pybank,None)
    for row in pybank:
        profit_losses = profit_losses + int(row[1])
       

print("Total: $"+ str(profit_losses))



#Create a list for value change.
greatest_increase = 0
greatest_increase_month = 0
value_change_list = []
pre_value = 0

with open (csvpath, 'r') as csvfile:
    pybank = csv.reader(csvfile, delimiter=',')
    next(pybank,None)
    for row in pybank:
        value_change = int(row[1])- pre_value
        pre_value = int(row[1])
        value_change_list.append(value_change)

    value_change_list[0] = 0

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

average_change = sum(value_change_list)/(row_count-1)
print("Average Change: $" + str(average_change))



#Create a list for date.

date_list = []

with open (csvpath, 'r') as csvfile:
    pybank = csv.reader(csvfile, delimiter=',')
    next(pybank,None)
    for row in pybank:
        date_list.append(row[0])
       
#Zip date and value change in one list.       
final_list = list(zip(value_change_list,date_list))

#Print out Greatest Increase in Profits.
Highest_change, Highest_date = max(final_list)
print(f"Greatest Increase in Profits: {Highest_date} (${Highest_change})")


#The greatest decrease in profits (date and amount) over the entire period
Lowest_change, Lowest_date = min(final_list)
print(f"Greatest Decrease in Profits: {Lowest_date} (${Lowest_change})")

