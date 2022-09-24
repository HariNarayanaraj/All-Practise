# Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

list1 = [34, 54, 67, 89, 11, 43, 94]

# Use the list methods, pop(), insert() and append()

# pop(index): Removes and returns the item at the given index from the list.
# insert(index, item): Add the item at the specified position(index) in the list
# append(item): Add item at the end of the list.

sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)
