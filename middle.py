def get_middle(s):
    if len(s)%2 == 0:
        middle = int(len(s) / 2)
        result = s[middle-1:middle+1]
    else:
        middle = int(len(s) // 2)
        result = s[middle]
    return result