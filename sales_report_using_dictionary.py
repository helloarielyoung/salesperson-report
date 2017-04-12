"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

#initializing lists to hold salesperson and melon data
salespeople = []
melons_sold = []

#open the file. if you put this in a function, you could pass file name
#f is not a great var, how about sales_file?
f = open("sales-report.txt")

#loop through the file's data
for line in f:
    #strip off white space from each line
    line = line.rstrip()
    #from each line put into a list salesperson, total $, total # melons sold
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])

#right here you could put salesperson, $, melons into a dictionary
#with salesperson as the key, and $, melons in a tuple
#or i guess you could diciontary within dictionary and have
#a key like "total_sales" and the $ and "total_melons" with the count

    if salesperson in salespeople:
        #puts salesperson name in list salespeople
        position = salespeople.index(salesperson)
        #puts number of melons sold into list melons_sold at the same index
        #position as the salesperson
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

print melons_sold

for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
