# Count the occurrence of each element from a list

# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show
# the count of each element

list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# use dict() function [creates a dictionary].

print("original value ", list1)

# creates a dictionary
count_dict = dict()

for item in list1:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

