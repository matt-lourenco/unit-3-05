# Created by: Matthew Lourenco
# Created on 17 Oct 2016
# This program calculates factorials

print('Please enter an integer and I will calculate the factorial of that integer.')

while 1 == 1:
    
    count = raw_input()
    
    try:
        count = int(count)
        number = count
        
        while count > 1:
            count = count - 1
            number = number * count
        print('The factorial is: ' + str(number))
    
    except:
        print(count + ' is not an integer. Please enter an integer.')
