"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# Original use: define two empty lists to sort the data
# Better alternative: define dict using names as keys and melons_sold as values
salespeople = []
melons_sold = []

# Open a file to loop though
f = open("sales-report.txt")
# Lopp through the file line-by-line
for line in f:
    # Remove trailing whitespace from line
    line = line.rstrip()
    # Split line into list based, delimiting on |
    entries = line.split("|")
    # Element 0 of entries is the salesperson's name
    # Better alternative: use salesperson as the key in a dict
    salesperson = entries[0]
    # Element 2 of entries is the # of melons sold, cast string as int
    # Better alternative: store as value in a dict
    melons = int(entries[2])

    # Check to see if salesperson is already added to the list
    if salesperson in salespeople:
        # Define the position as the index of salesperon in salespeople
        position = salespeople.index(salesperson)
        # Add # of melons sold to parallel position in melons_sold
        melons_sold[position] += melons
    # Salesperson is not in salespeople list
    else:
        # Add salesperson to salespeople list
        salespeople.append(salesperson)
        # Add # of melons sold to melons_sold, assumed parallel position
        melons_sold.append(melons)

# Loop through salespeople by index
for i in range(len(salespeople)):
    # Assume lists are parallel, print both lists
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
