import csv
import os

# Open a file named customers.csv
sales = open('sales.csv', 'r')
sales_report = open('salesreport.csv', 'w', newline='')

# Create reader object
reader = csv.reader(sales)

# Skip fields name row
next(reader)

# Create writer object
writer = csv.writer(sales_report, delimiter=',')

# Write field names
fieldnames = ['Customer |', 'Total']
writer.writerow(fieldnames)

# Dictionaries
id_salaryDict = {}

# Loop customer_name
for row in reader:
    customer_ID = int(row[0])
    SubTotal = float(row[3])
    TaxAmt = float(row[4])
    Freight = float(row[5])
    total = SubTotal + TaxAmt + Freight

    if customer_ID in id_salaryDict:
        id_salaryDict[customer_ID] += total
    else:
        id_salaryDict[customer_ID] = total

for cust_ID, total in id_salaryDict.items():
    new_row = [format(cust_ID, '>d'), format(total, '<.2f')]
    writer.writerow(new_row)

# Close file
sales.close()
sales_report.close()
