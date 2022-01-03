# num = int(input())

# n = int(input("How many terms? "))


def fibonacci(n):
# first two terms
    n1, n2 = 0, 1
    count = 0

# check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
# if there is only one term, return n1
    elif n == 1:
        
        return 1
# generate fibonacci sequence
    else:
        
        while count < n:
            print(n1)
            nth = n1 + n2
       # update values
            n1 = n2
            n2 = nth
            count += 1

fibonacci(6)