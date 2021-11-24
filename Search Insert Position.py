def searchInsert(nums,target):
    #using binary search
    low = 0
    high = len(nums)
    while low < high:
        mid = (high + low) //2
        if nums[mid] == target:
            return mid
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


a1 = [1, 3, 5, 6]
a2 = 5
b1 = [1, 3, 5, 6]
b2  =2
c1 = [1, 3, 5, 6]
c2 = 7
d1 = [1, 3, 5, 6]
d2 = 0
e1 = [1]
e2 = 1
print(searchInsert(a1,a2)) # 2
print(searchInsert(b1,b2)) # 1
print(searchInsert(c1,c2)) # 4
print(searchInsert(d1,d2)) # 0
print(searchInsert(e1,e2)) # 0
