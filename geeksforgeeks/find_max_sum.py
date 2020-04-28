'''
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.

Examples :

Input : arr[] = {5, 5, 10, 100, 10, 5}
Output : 110

Input : arr[] = {1, 2, 3}
Output : 4

Input : arr[] = {1, 20, 3}
Output : 20
'''
# Function to return max sum such that 
# no two elements are adjacent 
def find_max_sum(arr): 
	incl = 0
	excl = 0
	
	for i in arr: 
		
		# Current max excluding i (No ternary in 
		# Python) 
		new_excl = excl if excl>incl else incl 
		
		# Current max including i 
		incl = excl + i 
		excl = new_excl 
	
	# return max of incl and excl 
	return (excl if excl>incl else incl) 

# Driver program to test above function 
arr = [5, 5, 10, 100, 10, 5] 
print find_max_sum(arr) 

# This code is contributed by Kalai Selvan 
