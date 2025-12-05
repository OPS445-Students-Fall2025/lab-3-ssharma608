#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: ssharma608

import lab3b

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
         return lab3b.sum_numbers(number1, number2) 
    elif operator == 'subtract': 
         return lab3b.subtract_numbers(number1, number2)
    elif operator == 'multiply':
         return lab3b.multiply_numbers(number1, number2)
    else:
         return 'Error: function operator can be "add", "subtract", or "multiply"'


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))
