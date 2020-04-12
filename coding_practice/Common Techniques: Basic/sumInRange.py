def sumInRange(nums, queries):
    memo = {}
    sum = 0
    i = 0
    for n in nums:
        memo[i] = n
        i +=1
    for e in queries:
        j = 0
        while j <= (e[1] - e[0]) :
            inde = e[0] + j 
            sum += memo[inde]
            j += 1
    return sum % (1000000000 + 7)
