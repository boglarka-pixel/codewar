def opposite(number):
    return -number

print(opposite(777))


# ##########################

def positive_sum(arr):
    positive_arr = []
    for a in arr:
        if a > 0:
            positive_arr.append(a)
    if len(positive_arr) == 0:
        return 0
    return sum(positive_arr)

print(positive_sum([-1,2,3,4,-5]))

############################

def how_much_i_love_you(nb_petals):
    how_much = ["I love you","a little","a lot","passionately","madly","not at all"]
    num = (nb_petals % 6)-1
    return how_much[num]
        

print(how_much_i_love_you(15))

#################################################

def spin_words(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
            result = f'{result} {word}'
        else:
            result = f'{result} {word}'
            
    return result[1:]


##############################################
#    16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6

def digital_root(n):
    while n > 9:
        n = sum(map(int, str(n)))
    return n


###############################################


pin = input()
def pinFun():
    result = ''
    for p in pin:
        if p.isnumeric() != True:
            result = 'Please enter a number'
        elif p.isnumeric() == False:
            result = 'Pin s created'
    return result
 
print(pinFun())




            
			