import random
import time

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x ==pivot]
    right=[x for x in arr if x>pivot]

    return quick_sort(left)+middle+quick_sort(right)

def measure_sort_time(n):
    random_list=[random.randint(1,1000)for _ in range(n)]
    start_time=time.time()
    sorted_list=quick_sort(random_list)
    end_time=time.time()
    elapsed_time=end_time-start_time
    return sorted_list,elapsed_time

if __name__=="__main__":
    n=5000
    sorted_list,elapsed_time=measure_sort_time(n)
    print(f"Sorted list :{sorted_list[:100]}")
    print(f"Time taken to sort : {elapsed_time:.6f} seconds")
