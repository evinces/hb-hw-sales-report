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
        # Define the position as the index of salespesron in salespeople
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


# Below is my alternate implementation:


def parse_file_into_dict(filename):
    """Read file and parse into dict

    Dict format:
        key = salesperson_name
        value = melons_sold

    """

    sales_report = {}

    sales_file = open(filename)
    for line in sales_file:
        line = line.strip()
        entries = line.split('|')
        name = entries[0]
        qty_sold = int(entries[2])

        sales_report[name] = sales_report.get(name, 0) + qty_sold

    return sales_report


def print_sales_report(sales_report):
    """Print formatted sales report from dict, sorted alphabetically

    >>> sales_report = {"Alice": 4}
    >>> print_sales_report(sales_report)
    Alice sold 4 melons

    """

    for name, qty_sold in sorted(sales_report.items()):
        print "{} sold {} melons".format(name, qty_sold)


sales_report = parse_file_into_dict("sales-report.txt")
print_sales_report(sales_report)
