"""
Manatal Python Challenge (Exercise 3)
@author: marvinlimpijankit
Estimated Completion Time: ~20 mins
"""

class IntegerToRomanConverter:
    
    def int_to_roman(self, integer): 
    
        #list of roman symbols and their corresponding decimal values
        roman_digits = [("M", 1000),("CM", 900), ("D", 500), ("CD", 400), 
                        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        
        #list for the symbols in our final result
        converted_roman = []
        
        #loop through the roman digits from highest to lowest
        for roman_symbol, decimal_value in roman_digits: 
            
            #if current number is 0 we are done so break
            if integer == 0: 
                
                break
            
            #get the quotient, remainder of the int / roman numberal we are on
            # update the integer to be the remainder
            multiple, integer = divmod(integer, decimal_value)
            
            #append 'multiple' roman symbols to result accordingly
            for i in range(multiple): 
                
                converted_roman.append(roman_symbol)
                
        #concatenate the symbols with no spaces
        return "".join(converted_roman)

#code testing
if __name__ == '__main__': 

    Converter = IntegerToRomanConverter()
    
    #should return LXVII
    print("67 in roman numerals is: " + Converter.int_to_roman(67))
    
    #should return MCMXXXIV
    print("1934 in roman numerals is: " + Converter.int_to_roman(1934))