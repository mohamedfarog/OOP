
# Note: in buble sort we compare the first element array with the second element 
# if first element is greater we swap first with second
# in each loop we decrement the value of i and j loop in range from 0 to value of current i 

def bubleSort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp =  nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp



nums = [7,5,2,-1,6,9]
bubleSort(nums)
print(nums)

