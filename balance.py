
def balance(left, right):
  left_count = left.count("!")*2 + left.count("?")*3
  right_count = right.count("!")*2 + right.count("?")*3

  if(left_count > right_count):
    return "Left"
  elif(right_count>left_count):
    return "Right"
  else:
    return "Balance"


def move_zeros(array):
   
    indices = []
    
    for i in range(len(array)):
        if array[i] == 0:
         indices.append(i)

    reverse_indices = indices[::-1]
    for i in reverse_indices:
        #print(i)
        #print(reverse_indices)
        #print(array)
        del array[i]
    
    count = len(indices)

    for i in range(count):
        array.append(0)

    return array




def move_zeros2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))


def move_zeros3(array):
    newarr =[]
    zeroarr=[]
    for item in array:
        if item!= 0 or type(item)== bool :
            newarr.append(item)
        else:
            zeroarr.append(item)
            
            
    newarr.extend(zeroarr)
    return(newarr)



# def pig_it(text):
#     words = text.split(' ')
#     result= []
#     for w in words:
#         w = w[::-1]
#         print(w)
#         newW = w + 'ay'
#         result.append(newW)
#     return ' '.join(result)

    

# print(pig_it('Pig latin is cool'))


def pig_it(text):
    lst = text.split()
    
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)

print(pig_it('Pig latin is cool!'))

