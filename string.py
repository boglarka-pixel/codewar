long_string = "I'll catch you if you fall - The Floor"

print(long_string[0:4]) # I'll

print(long_string[-5:]) # Floor

print(long_string[:-5]) #I'll catch you if you fall - The

print(long_string[:4] + " be there") # I'll be there

print("%c is my %s letter and my number %d number is %.5f "%
     ('X', 'favorite', 1, .14))
# X is my favorite letter and my number 1 number is 0.14000 

print(long_string.capitalize()) # I'll catch you if you fall - the floor

print(long_string.find('Floor')) # 33

print(long_string.isalpha()) # False, Check if all the characters in the text are letters:

print(long_string.isalnum()) # False, Check if all the characters in the text are alphanumeric:

print(len(long_string)) # 38

print(long_string.replace('Floor', 'Ground'))

print(long_string.strip()) #leszedi a felesleges white space-t

quote_list = long_string.split(" ") # listává darabolja
print(quote_list)