# polish national identification number (PESEL) generator
# ________________________________________________________


# requirements for validity:

# 873208|7901|5

# the first 6 digits are for d.o.b.: respectively: year, month, day

# for distinguishing 20th century years from the 21st ones:
# years 1900 - 1999 have normal months numbers (1 - 12)
# years 2000 - 2099 have normal months numbers + 20 (21 - 32)

# the following four digits are random (well, excluding last one coz it stands for sex)

# the last digit comes out of a equation, and it is for checking the validity

# equation: 1*a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j
# (where the a-j letters are standing for the digits of first ten digits of PESEL number respectively)
# then: 10 - (the last digit of the equation result) gives you the last digit of PESEL number
# (if the last digit of the equation was 0, then it is the last digit of PESEL as well)


# examples:
# 02103032074
# 55092784844
# 28301156598

# ________________________________________________________


import random

def pesel():

	year = random.randint(1900,2099)


	if year <= 1999:
		month = random.randint(1,12)

	elif year >= 2000:
		month = random.randint(1,12) + 20 # to distinguish between centuries


	# I need to put months in a category to choose correct range of possible days for each one
	odd_months = (1, 3, 5, 7, 8, 10, 12, 21, 23, 25, 27, 28, 30, 32)
	even_months = (4, 6, 9, 11, 24, 26, 29, 31)

	if month in odd_months:
		day = random.randint(1,31)

	elif month in even_months:
		day = random.randint(1,30)
	# this is for february
	else:
		if year % 4 == 0 and year != 1900:
			day = random.randint(1,29) # leap year

		else:
			day = random.randint(1,28) # usual year





	four_random = random.randint(1000,9999)
	four_random = str(four_random)




	# here comes the equation part, it calculates the last digit

	y = '%02d' % (year % 100)
	m = '%02d' % month
	dd = '%02d' % day

	a = y[0]
	a = int(a)

	b = y[1]
	b = int(b)

	c = m[0]
	c = int(c)

	d = m[1]
	d = int(d)

	e = dd[0]
	e = int(e)

	f = dd[1]
	f = int(f)

	g = four_random[0]
	g = int(g)

	h = four_random[1]
	h = int(h)

	i = four_random[2]
	i = int(i)

	j = four_random[3]
	j = int(j)

	check = a + 3 * b + 7 * c + 9 * d + e + 3 * f + 7 * g + 9 * h + i + 3 * j

	if check % 10 == 0:
		last_digit = 0
	else:
		last_digit = 10 - (check % 10)

	# printing the final number out

	a = ('%02d' % (year % 100))
	b = ('%02d' % month)
	c = ('%02d' % day)
	d = (four_random)
	e = (last_digit)
	return str(a) + str(b) + str(c) + str(d) + str(e)




