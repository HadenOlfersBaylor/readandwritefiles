import csv

# Open a file named EmployeePay.csv
EmployeePay = open('EmployeePay.csv', 'r')

# Create reader object
reader = csv.reader(EmployeePay)

# Skip field names
next(reader)

# Input
user_input = 'continue'

# Loop and read
for row in reader:
    salary = float(row[3])
    bonus = float(row[4])
    total_pay = salary * (1+bonus)

    print('ID: ', row[0])
    print('FirstName: ', row[1])
    print('LastName: ', row[2])
    print('Salary: ', row[3])
    print('Bonus: ', row[4])
    print('Total Pay: ', format(total_pay, '.2f'))
    user_input = input('Press any key to continue, press ''q'' to quit: ')
    print('')
    if user_input != 'q':
        continue
    else:
        break

# Close file
EmployeePay.close()
