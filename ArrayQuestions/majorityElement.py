arr = [3,3,2]

# def majorityElement(arr):
#     max_count = 0
#     max_element = None
#     maj = len(arr) / 2

#     for i in range(len(arr)):
#         count = 0
#         for j in range(i, len(arr)):
#             if arr[i] == arr[j]:
#                 count+= 1
        
#         if count > max_count:
#             max_count = count
#             max_element = arr[i]

#     if max_count > maj:
#         return max_element
    

# result = majorityElement(arr)
# print(result)


# Approach - 2      Using Boyer Moore Voting Algorithm

def BoyerMajorityElement(arr):
    candidate = None
    count = 0

    for i in range(len(arr)):
        if count == 0:
            candidate = arr[i]    
        print("candidate is:", candidate)
        print("Count is: ", count)
        count += (1 if candidate == arr[i] else -1)
    return candidate


def isMajorityElement(candidate, nums):
    count = 0 
    n = len(nums)

    for i in range(n):
        if nums[i] == candidate:
            count+=1
    if count > n/2:
        return 1
    else:
        return 0 
        
def printMajorityElement(nums):
    cand = BoyerMajorityElement(nums)
    if isMajorityElement(cand, nums):
        print("Majority element is", cand)
    else:
        print("No majority element is present")


printMajorityElement(arr)