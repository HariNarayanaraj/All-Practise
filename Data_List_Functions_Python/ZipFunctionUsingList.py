# Create a Python set such that it shows the element from both lists in a pair

list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]

# Use the zip() function. This function takes two or more iterables (like list, dict, string)
# aggregates them in a tuple, and returns it.

print("First List ", list1)

print("Second List ", list2)

result = zip(list1, list2)
result_set = set(result)
print(result_set)
