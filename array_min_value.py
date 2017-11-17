# Created by: Kay Lin
# Created on: 16th-Nov-2017
# Created for: ICS3U
# This program displays finding the minimum value in array

from numpy import random

my_numbers = []

def smallest_array(array):
    # find the maximum value in array
    print('There are 10 random numbers:')
    
    # generate 10 random numbers
    for number in range(10):
        my_numbers.append(random.randint(1,100))
        print (my_numbers[number])
        
    # find the minimum value
    array_min = array[0]
    
    for a_value in my_numbers:
        if array_min == 0:
            array_min = a_value
        elif array_min > a_value :
              array_min = a_value
        else:
          array_min = array_min
          
    return array_min

return_value = smallest_array(my_numbers)
print ('The smallest value in the array is: ' + str(return_value))
