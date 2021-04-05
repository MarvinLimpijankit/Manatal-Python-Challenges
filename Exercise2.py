"""
Manatal Python Challenge (Exercise 2)
@author: marvinlimpijankit
Estimated Completion Time: ~10 minutes
"""

#import library to generate random numbers
import random

def generate_lottery_output(): 
    
    #list
    list = []
    
    #counter to keep track of how many balls pulled so far
    i = 0
    
    #loop through picking out 10 balls 
    while i < 10:
        
        #select a random number 1 to 50
        x = random.randint(1, 50)
        
        #make sure it has not already been picked (no duplicates)
        if(x not in list): 
            
            #append to list and adjust the counter
            list.append(x)
            i += 1
        
    #sort the list in ascending order
    list.sort()
    
    return list

#code testing
if __name__ == '__main__': 
    
    print(generate_lottery_output())

"""
Q: Describe which unit tests you could implement to test the output 
of your function. 

A: We could test to ensure that: 
    
    1) No duplicates are being drawn
    2) Exactly 10 balls are returned every time in ascending order
    3) All numbers drawn are between 1-50 (inclusive)
    
"""