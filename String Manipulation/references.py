# Code to format a reference inputted by the user into a proper format \
# Dylan Friedman
# FRDDYL002
# 23rd March 2022
# EG: poulo, lebeko bernard (2013) fine-grained scalability Of digital library services In The cloud, SAICSIT Conference 2014, ACM, pp23-34, 2014

ref = input('Enter the reference: \n') # user enters info into this string variable
print('Reformatted reference:') # outputs the quote

authors = ref[0:ref.find('(')] # splice the users input variable such that the authors names are a new variable
print(authors.title(), sep='', end='') # outputs the authors names with the first letter capatilised

year = ref[ref.find('('):ref.find(')')+2] # splice the variable sucht that the year is a new variable
print(year, sep='', end='') # outputs the year variable

aref = ref[ref.find(')')+2:] # splice the ref variable such that the rest of ref from the year is a new variable, aref.
title = aref[:aref.find(',')] # splice aref such that the title becomes a new variable, title.
print(title.capitalize(), sep='', end='') # output title with the first letter capitalized and everything else lower case

bref = aref[aref.find(','):] # splice aref such that the rest of the string from the end of title becomes a new variable, bref.
print(bref, sep='', end='') # output bref