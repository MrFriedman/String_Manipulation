# Code to convert digital time into a explained format with words   EG:  2021-04-09 04:33 === 4:33 am on the 9th of April '21
# FRDDYL002
# Dylan Friedman
# 22 March 2022

time = input('Enter the date and time (yyyy-mm-dd hh:mm): \n') # the user inputs the date into a string

year = time[:4] # splice from start to position 4
imonth = time[5:7] # splice from position 5 to 7
day = time[8:10] # splice from position 8 to 10
hour = time[11:13] # splice from position 11 to 13
minute = time[14:16]# splice from position 14 to 16

# The numerical date with its corresponding month
if imonth == '01': smonth = 'January' 
elif imonth == '02': smonth = 'February' 
elif imonth == '03': smonth = 'March' 
elif imonth == '04': smonth = 'April' 
elif imonth == '05': smonth = 'May' 
elif imonth == '06': smonth = 'June' 
elif imonth == '07': smonth = 'July' 
elif imonth == '08': smonth = 'August' 
elif imonth == '09': smonth = 'September' 
elif imonth == '10': smonth = 'October' 
elif imonth == '11': smonth = 'November' 
elif imonth == '12': smonth = 'December'

if day.find('3') == 1: # if the string number ends in 3
    suffex = 'rd'
elif day.find('2') == 1: # if the string number ends in 2
    suffex = 'nd'
elif (day.find('1') == 1) and (day != '11'): # if the string number ends in 1
    suffex = 'st'
else:# for everything else
    suffex = 'th'
    
if (int(hour) < 12 or int(hour) == 24) and int(hour) != 0: # FOR ALL HOURS IN THE MORNING INCLUDING 24 HOURS
    print(int(hour), ':', minute, ' am on the ', sep='', end='')
    print(int(day), suffex, ' of ', smonth, " '", year[2:4], sep='', end='')
    
elif int(hour) == 0: # IF THE HOUR IS 12
    print('12', ':', minute, ' am on the ', sep='', end='')
    print(int(day), suffex, ' of ', smonth, " '", year[2:4], sep='', end='')    
elif int(hour) == 12: # FOR ALL HOURS IN THE EVENING BESIDES FOR 12 DUE TO OUTPUT REQUIREMENTS
    print(int(hour), ':', minute, ' pm on the ', int(day), suffex, ' of ', smonth, " '", year[2:4], sep='')
    
else: # FOR ALL HOURS IN THE EVENING BESIDES FOR 12 DUE TO OUTPUT REQUIREMENTS
    print(int(hour) - 12 , ':', minute, ' pm on the ', int(day), suffex, ' of ', smonth, " '", year[2:4], sep='')
    