#!/usr/bin/env python3

# return_text_value() function
# Author ID: jgylagan

def return_text_value():
    return "Hello world from inside a function" # return text function from part 2

# return_number_value() function

def return_number_value():
    number1 = 10
    number2 = 5
    return number1 + number2 # return number function from part 3



# Main Program


if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))
