# Code for creating a graph of f(x) = x + 2 in the reagons 10 by 10 on the x and y axis  \  |
# FRDDYL002
# Dylan Friedman
# 23 March 2022


import math

fox = input('Enter a function f(x):\n')

for y in range(10,-11,-1):
    for x in range(-10,11,1):
        afox = fox[:fox.find('x')] + '(' + str(x) + ')'+ fox[fox.find('x')+1:]
        ifox = eval(afox)
        
        if round(ifox) == y:
            print('o', end='')
            
        else:
            if x == 0 and y == 0:
                print('+', end='')    
            elif x == 0:
                print('|', end='')                
            elif y == 0:
                print('-', end='')
            else:
                print(' ', end='')
                
    print()
    
        
    