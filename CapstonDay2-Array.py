#---------------------------------------------------------------------------------------
# ARRAY - Collection of diff data types stored in an address - At a time only 1 dara type. 
# Data stored on stack. FILO - first in last out
# Queue works on FIFO - first in first out
# Sorting - 

import array as arr
a = arr.array('i', [1, 2, 3])
print(a[0])

# Add an element
a.append(5)
print(a)

# Add multiple elements
a.extend([6,8,9])
print(a)
print(a[3])

print("\n")

# Output element at a specific element position
b = arr.array('i', [10, 20, 30])
print("Element at index position 2: ", b[2])
abc = arr.array('i', [10,20,30,40,50,60])
print("Element at index position", abc[5])

# Update Element
abc = arr.array('i', [10,20,30,40,50,60])
abc[1]=5
print("Updated Array", abc)

print("\n")

# Insert an Element
abc = arr.array('i', [10,20,30,40,50,60])
abc.insert(7, 4)
print("After Insertion", abc)
abc = arr.array('i', [10,20,30,40,50,60])
abc.insert(5, 9)
print("After Insertion", abc)

print("\n")

# Delete an Element
abc = arr.array('i', [10,20,30,40,50,60])
abc.remove(40)
print("After Deletion", abc)
abc = arr.array('i', [10,20,30,40,50,60])
abc.pop(4)
print("After Deletion", abc)

print("\n")

# Search an element
abc = arr.array('i', [10,20,30,40,50,60])
abc.insert(5, 4)
print("Index of 5: ", abc.index(50))

# Reversing an Array
abc.reverse()
print(abc)

print("\n")

# Sum of all Array Elements
print("Sum is: ", sum(abc))
# Smallest and Largest Element
print("Smallest number is: ",min(abc))
print("Largest number is: ",max(abc))

print("\n")

# Sorting - Acsending and Descending order
print("Sorted Array in Ascending Order: ", sorted(abc))
print("Sorted Array in Descending Order: ", sorted(abc, reverse=True))

print("\n")

# Create a Fixed Size Array
MAX_SIZE = 5
q = arr.array("i", [0]* MAX_SIZE)
print("Fixed Size Array: ", q)

print("\n")

# Pta nhi kya kia 😐
MAX_SIZE = 5
q = arr.array("i", [1,2,3,4,5,6])
if len(q)>MAX_SIZE:
    print("❌ -- Error: Array Overflow -- ❌")


print("\n")