#!/usr/bin/env python3

'''Lab 3f - Lists Manipulation and Functions'''
# Author ID: jgylagan

'''

courses = ['uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635']
print(courses[0])
courses[0] = 'eac150'
print(courses[0])
print(courses)

courses.append('ops235')    # Add a new item to the end of the list object named courses
print(courses)

courses.insert(0, 'hwd101') # Add a new item to the specified index location, 
                            # the original item will be pushed to the next index location
print(courses)

courses.remove('ops335')    # Remove first occurrence of a matching item in the list object
print(courses)

sorted_courses = courses.copy() # Create a copy of the courses list
sorted_courses.sort()           # Sort the new list 
print(courses)
print(sorted_courses)


list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
length_of_list = len(list_of_numbers)    # Returns the length of the list
smallest_in_list = min(list_of_numbers)  # Returns the smallest value in the list
largest_in_list = max(list_of_numbers)   # Returns the largest value in the list

# Notice how the long line below is wrapped to fit on one screen:
print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))

      
# PArt 3
def square_list(number_list):
    new_list = []
    for number in number_list:
        new_list.append(number * number)
    return new_list

new_list_of_numbers = square_list(list_of_numbers)
print(list_of_numbers)
print(new_list_of_numbers)


list_of_numbers = [1, 5, 2, 6, 8, 5, 10, 2]
def delete_numbers(numbers):
    numbers.remove(5)
    numbers.remove(6)
    numbers.remove(8)
    numbers.remove(5)
delete_numbers(list_of_numbers)
print(list_of_numbers)
'''


# Create the main list (before functions)
my_list = [1, 2, 3, 4, 5]


def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    last_item = ordered_list[-1]
    new_item = last_item + 1
    ordered_list.append(new_item)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for number in items_to_remove:
        while number in ordered_list:
            ordered_list.remove(number)


# Main block

if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1, 5, 6]) # New line that removes the numbers for print below
    print(my_list)
