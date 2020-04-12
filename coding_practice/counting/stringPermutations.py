#!/usr/local/bin/python3

def stringPermutations(string, prefix, permutation_list):
    #Edge case check
    if len(string) == 0:
        permutation_list.append(prefix)
    else:
        for i in range(len(string)):
            rem = string[0:i] + string[i + 1:]
            stringPermutations(rem, prefix + string[i], permutation_list)
    return sorted(list(dict.fromkeys(permutation_list)))

def main():
    permutation_list = []
    print(stringPermutations('ABA','', permutation_list))

if __name__ == '__main__':
    main()


# def stringPermutations(s):
#         news = s
#         if len(news) == 1:
#             return [news]
#         res = []
#         for permutation in stringPermutations(news[1:]):
#             for i in range(len(news)):
#                 res.append(permutation[:i] + news[0:1] + permutation[i:])
#         # To Remove Duplicates From a Python List: list(dict.fromkeys(res))
#         # To Sort List : sorted()
#         return sorted(list(dict.fromkeys(res)))

