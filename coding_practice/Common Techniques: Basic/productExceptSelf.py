def productExceptSelf(nums, m):

    length = len(nums)
    r = [1] * length
    a,b = 1,1

    for i in range(length):
        r[i] = r[i] * a
        a *= nums[i]
        r[-i-1] = r[-i-1] * b
        b *= nums[-i-1]
        
    r = [x%m for x in r]
    return sum(r) % m