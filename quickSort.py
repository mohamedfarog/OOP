
# Important Note: quickSort function will pause the call each time a new call is made the resume the call later
# in step by step control follow.  
def partition(input_list,low,high):
    i = (low - 1)
    pivot = input_list[high]
    print(pivot)
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1],input_list[high] = input_list[high],input_list[i+1]
    return (i+1)

def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)


#input_l = [9, -3, 5, 2, 6, 8, -6, 1, 3]
input_l = [19, 3, -2, 8, 6, 5, -1, 4]
list_length = len(input_l)
quickSort(input_l, 0, list_length -1)
print(input_l)

#https://www.youtube.com/watch?v=COk73cpQbFQ