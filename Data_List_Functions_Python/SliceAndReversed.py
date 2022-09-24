# Slice list into 3 equal chunks and reverse each chunk

list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Get the length of a list using a len() function
# Divide the length by 3 to get the chunk size
# Run loop three times
# In each iteration, get a chunk using a slice(start, end, step) function and reverse it using the reversed() function
# In each iteration, start and end value will change

print("Original list ", list1)

length = len(list1)
chunk_size = int(length / 3)
start = 0
end = chunk_size

for i in range(3):
    # get indexes
    indexes = slice(start, end)
    # get chunk
    list_chunk = list1[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size




