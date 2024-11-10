import array
import random
def generate_sorted_data(size):
    arr=array.array('i',[0]*size)
    for i in range(len(arr)):
        arr[i]=random.randint(1,100)
    if size>999:
        if len(arr)>1:
            left_arr=arr[:len(arr)//2]
            right_arr=arr[len(arr)//2:]

            merge_sort(left_arr)
            merge_sort(right_arr)

            i=0
            j=0
            k=0

            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<right_arr[j]:
                    arr[k]=left_arr[i]
                    i+=1
                else:
                    arr[k]=right_arr[j]
                    j+=1
                k+=1
            
            while i<len(left_arr):
                arr[k]=left_arr[i]
                i+=1
                k+=1
            while j<len(right_arr):
                arr[k]=right_arr[j]
                j+=1
                k+=1
    

        

    return array_a


print(generate_sorted_data(5))




    # for i in range(1,len(array_a)):

    #     while array_a[i]<array_a[i-1]:
    #         array_a[i-1]=array_a[i]
    #         array_a[i]=...