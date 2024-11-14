import random
import time

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time_complexity(n,runs=5):
    total_time=0
    for _ in range(runs):
        arr=[random.randint(1,10000) for _ in range(n)]
        start_time=time.time()
        merge_sort(arr)
        end_time=time.time()
        total_time+=(end_time-start_time)
    return total_time/runs

if __name__=="__main__":
    random.seed(42)

    for n in[5000,10000,15000,20000]:
        time_taken=measure_time_complexity(n)
        print(f"Average time taken to sort {n} elements : {time_taken:.6f} seconds")