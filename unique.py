from itertools import groupby


#1
def unique_in_order0(iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order0('DDDFVVV'))


#2
def unique_in_order1(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res
            

print(unique_in_order1('AACTT'))


#3
def unique_in_order2(iterable):
    arrayOfletters = []
    current_letter = ''
    for letter in iterable:
        if letter != current_letter:
            arrayOfletters.append(letter)
            current_letter = letter
    return arrayOfletters


print(unique_in_order2('aaabbccdaaaa'))



