import array
import random
def generate_sorted_data(size):
    array_a=array.array('i',[0]*size)
    for i in range(len(array_a)):
        array_a[i]=random.randint(1,100)
    if size>999:
        

    return array_a


print(generate_sorted_data(5))




    # for i in range(1,len(array_a)):

    #     while array_a[i]<array_a[i-1]:
    #         array_a[i-1]=array_a[i]
    #         array_a[i]=...