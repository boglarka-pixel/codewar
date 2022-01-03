
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


# print(valid_parentheses('po(ygq)(q)(sx()l)ftwqoy)(()'))
# print(valid_parentheses(' ('))
print(valid_parentheses('hi())('))
# print(valid_parentheses('hi(hi)()'))


# def valid_parentheses(string):
#     right = '('
#     left = ')'
#     count_r = 0
#     count_l = 0
#     list_of_p = []
#     for e in string:
#         if e == left:
#             list_of_p.append(e)
#             count_l+=1
#         if e == right:
#             list_of_p.append(e)
#             count_r+=1
#     if list_of_p == []:
#         return True
#     stringi = ''.join(list_of_p)
#     print(stringi)
#     if count_l == count_r and right != stringi[-1] and left != stringi[0]:
#         return True
#     else:
#         return False


# print(valid_parentheses('po(ygq)(q)(sx()l)ftwqoy)(()'))