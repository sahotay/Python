#!/usr/local/bin/python3
arr = [1,2,4,10,10,-10,1,-1]
def large_cont_sumM1(arr):
    # edge case sum
    if len(arr)==0:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum,max_sum)
    return max_sum

print(f"Calling fn:large_cont_sumM1, Max sum is: {large_cont_sumM1(arr)}")