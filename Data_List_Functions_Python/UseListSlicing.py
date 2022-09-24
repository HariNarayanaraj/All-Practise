# Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# the expression list1[ start : stop : step] returns the portion of the list from index start to index stop, at a step size step.[slice method]

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

res = list()
odd_index_element = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_index_element)

even_index_element = list2[0::2]
print("Element at even-index positions from list two")
print(even_index_element)

print("Printing Final third list")
res.extend(odd_index_element)
res.extend(even_index_element)

print(res)
