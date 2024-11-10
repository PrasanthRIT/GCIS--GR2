import array
import random

# Function to generate random data and sort it using insertion sort
def generate_sorted_data(size):
    # Create an array of 'size' with initial values set to 0
    arr = array.array('i', [0] * size)
    
    # Populate the array with random integers between 1 and 100
    for i in range(size):
        arr[i] = random.randint(1, 100)
    
    # Print the original random data
    print("Original random data:",arr)
    
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
    
    # Return the sorted array
    return arr

# Display the sorted data
print("Sorted data:",generate_sorted_data(10))


