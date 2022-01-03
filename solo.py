nums = (55, 44, 33, 22)

print(max(min(nums[:2]), abs(-42)))


nums = {1, 2, 3, 4, 5, 6}

nums = {0, 1, 2, 3} & nums

nums = filter(lambda x: x > 1, nums)

print(len(list(nums)))

try:

  print(1)

  assert 2 + 2 == 5

except AssertionError:

  print(3)

except:

  print(4)


nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x:x%2==0, nums))
print(res)



pin = input()

if not pin.isnumeric():
    print('Please enter a number')
else:
    print('PIN code is created')




# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1