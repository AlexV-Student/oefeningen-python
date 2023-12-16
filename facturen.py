import sqlite3, csv, sys, datetime, locale

# Selects the concatenated (concat adhv ||) first and last names of customers and the invoice date from the "invoices" table
# Joined with the "customers" table using the "CustomerId" column, where the invoice date is in December 2013
query = '''
SELECT customers.FirstName || '  ' || customers.LastName, invoices.InvoiceDate
FROM invoices JOIN customers USING(CustomerId)
WHERE invoices.InvoiceDate LIKE '2013-12%';
'''

# Connect to a SQLite database
try:
	dbconnectie = sqlite3.connect('chinook.db')
	mijncursor = dbconnectie.cursor()
except:
	print('Er ging iets fout bij het openen van de database.')
	sys.exit(-1)

# The script attempts to execute the SQL query stored in the query variable using the cursor (mijncursor).
# If successful, it fetches all the results and stores them in the invoices list.
invoices = []
try:
	mijncursor.execute(query)
	invoices = mijncursor.fetchall()
except:
	print('Er ging iets mis bij het uitvoeren van de query.')
	sys.exit(-1)

# The script sets the locale to 'nl_BE.UTF-8' for Dutch formatting of dates.
locale.setlocale(locale.LC_ALL, 'nl_BE.UTF-8')

# Opens a CSV file named 'invoices.csv' in write mode. It then creates a CSV writer (my_writer) and iterates through each invoice in the invoices list.
# For each invoice, it formats the date and writes the customer name and formatted date to the CSV file.
try:
	with open('invoices.csv', 'w') as invoice_file:
		my_writer = csv.writer(invoice_file)
		for invoice in invoices:
			my_invoice = []
			my_invoice.append(invoice[0])
			datum = datetime.datetime.strptime(invoice[1], '%Y-%m-%d %H:%M:%S')
			my_invoice.append(datetime.date.strftime(datum, '%A %d %B %Y'))
			my_writer.writerow(my_invoice)
except:
	print('Fout bij wegschrijven')
	sys.exit(-1)