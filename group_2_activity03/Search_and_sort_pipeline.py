"""This Python Program generates a custom array based on user's size and sorts it either by
   Insertion sorting method
   Recursive Merge Sorting method
   Moreover, this program contains binary search to search for a target value for the user.
   we then compare linear search and binary search efficiency through time module,specifically using the time.prefcounter()
"""
#importing libaries
import array
import random
import time

def generate_sorted_data(size):

    #Phase 1

    # Create an array of 'size' with initial values set to 0
    arr = array.array('i', [0] * size)
    
    # Populate the array with random integers between 1 and 100
    for i in range(size):
        arr[i] = random.randint(1, 100)
    
    if size<=999:
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
        def merge_sort(arr):
            if len(arr) > 1: #starts sorting only if length of array is greater than 1

                ratio = 0.5  #50-50 split
                split_index = int(len(arr) * ratio) #int() rounds to the nearest integer, effectively finding the mid point
                left_arr = arr[:split_index]
                right_arr = arr[split_index:]
                
                merge_sort(left_arr)
                merge_sort(right_arr)
                

                i=0 #index of left array
                j=0 #index of right array
                
                for k in range(len(arr)): # k is the index of the final array
                    if i < len(left_arr) and (j >= len(right_arr) or left_arr[i] < right_arr[j]): #if length of right array is smaller or left_arr is less than right array and i less than length of left array
                        arr[k] = left_arr[i] #placing value of left_Arr in K index of final array
                        i += 1
                    else:
                        arr[k] = right_arr[j] #placing value of right_Arr in K index of final array
                        j += 1
                    
            return arr
        
        #implementing merge_sort
        arr=merge_sort(arr)
    
    # Return the sorted array
    return arr

#Phase 2
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

def linear_search(arr,target_value):
    for i in range(len(arr)):
        if arr[i]==target_value:
            return i
        else:
            return None

#Phase 4
def main():
    arr=generate_sorted_data(1000)

    start=time.perf_counter()
    linear_search(arr,72)
    end=time.perf_counter()
    elapsed_time=end-start
    print("Elapsed time for linear search:",elapsed_time)

    start=time.perf_counter()
    binary_search(arr,72)
    end=time.perf_counter()
    elapsed_time=end-start
    print("Elapsed time for Binary search:",elapsed_time)

if __name__=="__main__":
    main()