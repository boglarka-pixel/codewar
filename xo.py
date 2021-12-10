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
  

print(xo('zzoo'))


