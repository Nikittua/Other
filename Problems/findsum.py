# Перебор пары чисел
def twosum(nums: list, k: int)->list:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i]+nums[j]==k):
                return [nums[i], nums[j]]
            
    return []


#hashset
def hashset(nums: list, k: int) -> list:
    ourset = {0}
    for num in nums:
        numberToFind = k - num
        if ourset.__contains__(numberToFind):
            return [numberToFind, num]
        ourset.add(num)

    return []    


#binarysearch
def binarysearch(nums: list, k: int) -> list:
    for i in range(len(nums)):
        numberToFind = k - nums[i]
        left =i+1; right = len(nums)-1
        while(left<=right):
            mid = left+(right-left)//2
            if(nums[mid] == numberToFind):
                return [nums[i], nums[mid]]
            if (numberToFind < nums[mid]):
                right = mid-1
            else:
                left =mid+1

    return []

#TwoPointers
def TwoPointers(nums: list, k: int) -> list:
    left=0; right = len(nums)-1
    while(left<right):
        sum = nums[left]+nums[right]
        if(sum ==k):
            return [nums[left], nums[right]]
        if(sum < k):
            left+=1
        else:
            right-=1
    return []
            


     



if __name__ == "__main__":
    print(twosum([-1,2,5,8],7))
    print(hashset([-1,2,5,8],7))
    print(binarysearch([-1,2,5,8],7))
    print(TwoPointers([-1,2,5,8],7))



