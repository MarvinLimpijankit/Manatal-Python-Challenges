"""
Manatal Python Challenge (Exercise 1)
@author: marvinlimpijankit
Estimated Completion Time: ~10 minutes
"""

#import math library for pi
import math

class Circle: 
    
    #constructor, takes a radius
    def __init__(self, radius): 
        
        #set radius of the circle object
        self.radius = radius
        
    #compute area: πr^2
    def get_area(self): 
        
        return (math.pi)*(self.radius)**2
    
    #compute perimeter: 2πr
    def get_perimeter(self): 
        
        return 2*(math.pi)*(self.radius)
    
#code testing
if __name__ == '__main__': 
    
    #Create circle instances
    circle1 = Circle(1) 
    circle2 = Circle(5)
    circle3 = Circle(9)
    
    print("Testing a Circle with radius " + str(circle1.radius) + "...")
    print("Area: " + str(circle1.get_area()))
    print("Perimeter: " + str(circle1.get_perimeter()))
    print("\n")
    
    print("Testing a Circle with radius " + str(circle2.radius) + "...")
    print("Area: " + str(circle2.get_area()))
    print("Perimeter: " + str(circle2.get_perimeter()))
    print("\n")
    
    print("Testing a Circle with radius " + str(circle3.radius) + "...")
    print("Area: " + str(circle3.get_area()))
    print("Perimeter: " + str(circle3.get_perimeter()))
    print("\n")