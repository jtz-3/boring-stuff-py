"""
Mar 5 2025.

A practice challenge given in Ch. 7 of 'Automate the Boring Stuff With Python' by Al Sweigart.

Given an input date in DD/MM/YYYY, this script determines if it is a valid date or not,
using regular expressions to simplify the validation of the date format.
"""

import re

dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

while True:
	dateInput = input('Enter a date to check (DD/MM/YYYY): ')
	result = dateRegex.search(dateInput)
	valid = True

	if result is None:
		print('Invalid format - enter as DD/MM/YYYY and try again.')
		continue
	else:
		day, month, year = int(result.group(1)), int(result.group(2)), int(result.group(3))

		if day > 31:									# This day would not be valid for any month 
			valid = False								# 	(particularly for Jan, Mar, May, Jul, Aug, Oct, and Dec).
		elif month > 12:								# This month would not be valid for any year.
			valid = False
		elif (month in [4, 6, 9, 11]) and (day > 30):	# Validate days for Apr/Jun/Sep/Nov:
			valid = False
		elif month == 2:								# Validate Feb
			if day > 29:
				valid = False
			elif not ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))) and day > 28:
				valid = False

		if valid:
			print('Valid date.')
		else:
			print('Invalid date.')