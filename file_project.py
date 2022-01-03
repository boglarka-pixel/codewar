list = ['Harry Potter\n', 'The Hunger Games\n', 'Pride and Prejudice\n', 'Gone with the Wind']

#elegáns

newList = []
for l in list:
    newList.append(l.replace("\n", ""))

for l in newList:
  
    print(l[0] + str(len(l)))


#nem elegáns

# print(list[0][0] + str(len(list[0])-1))
# print(list[1][0] + str(len(list[1])-1))
# print(list[2][0] + str(len(list[2])-1))
# print(list[3][0] + str(len(list[3])))


