"""
Task:

Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.

Division by zero should return an empty value.

"""

def remainder(a,b):
    
    if a >= b and b != 0:
        return a % b
    elif b > a and a !=0:
        return b % a
    elif a == 0 or b == 0:
        return None


def remainder2(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a