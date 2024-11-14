def merge_sort (arr: list)->list:
    if len(arr)<= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge (left_half, right_half)

def merge(left: list, right: list) -> list:
    result=[]
    i=j=0

    while i < len(left) and j < len(right):
        if right[i]<right[j]:
            result.append(left[i])
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result. extend(right[j:])

    return result

def get_user_input()->list:
    try:
        input_str= input( "Enter numbers separated by spaces:")
        input_list=[int(num) for num in input_str.split()]
        return input_list
    except ValueError:
        print("Invalid input.please enter valid intergers separated by space")
        return []
    
if __name__=="__main__":
    user_input=get_user_input()
    if user_input:
        sorted_array=merge_sort(user_input)
        print("Original array : ",user_input)
        print("sorted array",sorted_array)
    else:
        print("No valid input provided")