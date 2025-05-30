#!/usr/bin/env python3

'''Lab 3 Part 1 script - functions'''
# Author ID: jgylagan

def sum_numbers(number1, number2): # function that adds the inputs
    return number1 + number2

def subtract_numbers(number1, number2): # function that substracts the inputs
    return number1 - number2

def multiply_numbers(number1, number2): # function that multiplies the inputs
    return number1 * number2

if __name__ == '__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
    # printing out the outputs