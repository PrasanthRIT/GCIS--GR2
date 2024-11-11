import array
import random

def generate_sorted_data(size):

    #Phase 1

    # Create an array of 'size' with initial values set to 0
    arr = array.array('i', [0] * size)
    
    # Populate the array with random integers between 1 and 100
    for i in range(size):
        arr[i] = random.randint(1, 100)
    
    if len(size)<=999:
        # Perform insertion sort on the generated array
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            # Shift elements of arr[0..i-1] that are greater than key, to one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]  # Move the element one position ahead
                j -= 1               # Move to the next element on the left
                
            # Place the key in its correct sorted position
            arr[j + 1] = key

    #Phase 3
    else:
        ...
    
    # Return the sorted array
    return arr

#Phase 2
# Binary search function
def binary_search(sorted_array, target):
    mid_index = len(sorted_array) // 2

    # Base case: if array is empty
    if len(sorted_array) == 0:
        return None

    # If the middle element is the target, return the middle index
    if sorted_array[mid_index] == target:
        return mid_index

    # If the target is less than the middle element, search the left half
    elif sorted_array[mid_index] > target:
        return binary_search(sorted_array[:mid_index], target)

    # If the target is greater, search the right half
    else:
        result = binary_search(sorted_array[mid_index + 1:], target)
        # Adjust index if found in the right half
        if result == None:
            return None
        return mid_index + 1 + result

