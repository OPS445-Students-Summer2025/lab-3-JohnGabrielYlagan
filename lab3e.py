#!/usr/bin/env python3

'''Lab 3e - Lists '''
# Author ID: jgylagan

'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']
list3 = ['uli101', 1, 'ops235', 2, 'ops335', 3, 'ops445', 4, 'ops535', 5, 'ops635', 6]
# count from 0

# Choosing specific items
print(list1[0])  # the first item in list1
print(list2[1])  # Second item in list2
print(list3[-1]) # negative means go to the last

# choosing slices
print(list1[0:5]) # between 0 and 5
print(list2[2:4]) # Starting with 2nd and stopping before 4th
print(list3[3:])  # Starting with 3rd and going to the end
'''

# Create the list called "my_list" here, not within any function defined below.
my_list = [100, 200, 300, 'six hundred']
# That makes it a global object. We'll talk about that in another lab.


def give_list():
    # Does not accept any arguments
    return my_list
    # Returns all of items in the global object my_list unchanged


def give_first_item():
    # Does not accept any arguments
    return my_list[0]
    # Returns the first item in the global object my_list as a string
    


def give_first_and_last_item():
    # Does not accept any arguments
     return [my_list[0], my_list[-1]]
    # Returns a list that includes the first and last items in the global object my_list
   

def give_second_and_third_item():
    # Does not accept any arguments
    return [my_list[1], my_list[2]]
    # Returns a list that includes the second and third items in the global object my_list
    

    # Main code block

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
