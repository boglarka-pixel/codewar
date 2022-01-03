def xo(s):
     xx = []
     oo = []
     for letter in s:
        letter=letter.lower()
     
        if letter == 'x':
            xx.append(letter)
        if letter == 'o':
            oo.append(letter)
        if letter != 'x' and letter != 'o':
         return True
     
     return len(xx) == len(oo)
  

# print(xo('zzoo'))


def solution(string, ending):
    if len(ending) == 0:
        return True
    
    end_count = len(ending)
    print(end_count)
    
    if string[-end_count:] == ending:
        return True
    else:
        return False
   




print(solution('abcde', 'cde')) #ture
print(solution('abcde', 'abc')) # false
print(solution('abcde', '')) #true
print(solution('samurai', 'ai')) # true

# string = 'valamike'

# print(string[-1:])


