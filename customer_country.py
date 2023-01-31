import csv
import os

# Open a file named customers.csv
customer_file = open('customers.csv', 'r')
customer_country = open('customer_country.csv', 'w', newline='')

# Create reader object
reader = csv.reader(customer_file)

# Skip fields name row
next(reader)

# Create writer object
writer = csv.writer(customer_country, delimiter=',')

# Variables
customer_count = 0

# Write field names
fieldnames = ['Customer_Name', ' Country']
writer.writerow(fieldnames)

# Loop customer_name
for row in reader:
    customer_count += 1
    customer_name = row[1] + ' ' + row[2]
    country = ' ' + row[4]
    new_row = [customer_name, country]
    writer.writerow(new_row)

formatted_count = ' ' + str(customer_count)
total_row = ['Total Number: ', formatted_count]
writer.writerow(total_row)

# Close file
customer_file.close()
customer_country.close()
