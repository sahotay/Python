#!/usr/local/bin/python3

'''
For arr = [3, 1, 0], the output should be
missingNumber(arr) = 2.
'''
def find_missing(lst):
    missinglist = []
    for x in range(1, lst[-1]+1):
        if x not in lst:
            missinglist.append(x)
    return missinglist
def main():
    # Driver code
    lst = [1, 2, 4, 6, 7, 9, 10]
    print(find_missing(lst))
if __name__ == '__main__':
    main()