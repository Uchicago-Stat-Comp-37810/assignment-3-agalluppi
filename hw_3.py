# Name: Zander Galluppi
import math
import random

# ********** Exercise 1 ********** 

# Function that returns "True" if the argument m is divisible by argument n
def is_divisible(m,n):
    if n == 0:
        return print("Error: Division by 0")
    return m % n == 0
    
# Test cases for is_divisible

is_divisible(10, 5)  # This should return True
is_divisible(18, 7)  # This should return False
is_divisible(42, 0)  # What should this return?

# ********** Exercise 2 ********** 

# Function that returns "True" if the arguments are equal
def are_equal(m,n):
    return m-n == 0
    
are_equal(5,-5)
are_equal(-1,-1)
are_equal(9, 0)

# ********** Exercise 3 ********** 

# Function that returns a*b+c
def multadd(a,b,c):
    return a*b+c

# Test Cases
angle_test = multadd(math.cos(math.pi/4),1/2,math.sin(math.pi/4))
print("sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(2, math.log(12,7), math.ceil(276/19))
print("ceiling(276/19) + 2 log_7(12) is:")
print(ceiling_test)


# ********** Exercise 4 **********

# Generates a random integer from 0 to 100 and returns "True" if the integer is divisble by 3
def rand_divis_3():
    a = random.randint(0,100)
    print(a)
    return(a % 3 == 0)
    
# Test Cases
a = 0
print(a)
a % 3 == 0 # Should be true
    
a = 100
print(a)
a % 3 == 0 # Should be false
    
a = 15
print(a)
a % 3 == 0 # Should be true
    
    

