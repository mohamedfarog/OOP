
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