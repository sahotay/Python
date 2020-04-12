from itertools import product


def pressingButtons(buttons):
    
    if not buttons:
        return []
    
    map = {'2': 'abc',
           '3': 'def',
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}
    
    return [''.join(i)
            for i in product(*[map[i]
                               for i in buttons])]
