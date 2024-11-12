import array
import random

# Function to generate random data and sort it using insertion sort
def generate_sorted_data(size):
    arr = array.array('i', [0] * size)
    
    # Populate the array with random integers between 1 and 100
    for i in range(size):
        arr[i] = random.randint(1, 100)
    
    print("Original random data:", arr)
    
    # Perform insertion sort on the generated array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

# Binary search function
def binary_search(sorted_array, target):
    mid_index = len(sorted_array) // 2

    # if array is empty
    if len(sorted_array) == 0:
        return None

    # If the middle element is the target then return the middle index
    if sorted_array[mid_index] == target:
        return mid_index

    # If the target is less than the middle element then search the left half
    elif sorted_array[mid_index] > target:
        return binary_search(sorted_array[:mid_index], target)

    # If the target is bigger then search the right half
    else:
        result = binary_search(sorted_array[mid_index + 1:], target)
        # update the index if found in the right half
        if result == None:
            return None
        return mid_index + 1 + result

#print sorted data
sorted_data = generate_sorted_data(10)
print("Sorted data:", sorted_data)

# do binary search with target
print("Index of target 29:", binary_search(sorted_data, 13))   # Expected output: index of 29 or None 
print("Index of target 100:", binary_search(sorted_data, 24)) # Expected output: None









