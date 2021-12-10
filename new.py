def how_much_i_love_you(nb_petals):
    how_much = ["I love you","a little","a lot","passionately","madly","not at all"]
    num = (nb_petals % 6)-1
    return how_much[num]
        

print(how_much_i_love_you(15))


#print((15 % 6)-1)
