"""
https://www.codewars.com/kata/55685cd7ad70877c23000102/train/python
Instructions:
In this simple assignment you are given a number and have to make it negative. 
But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
"""

def make_negative( number ):
    if number == 0:
        number = 0
    else:
        number = 0-abs(number)
    return number


# Sample Tests
# Test.assert_equals(make_negative(42),-42)
# Test.assert_equals(make_negative(-9),-9)
# Test.assert_equals(make_negative(0),0)
# Test.assert_equals(make_negative(1),-1)
# Test.assert_equals(make_negative(-1),-1)

# from random import randint as rnd

# for _ in range(10):
#     number = rnd(1, 1000)
#     Test.assert_equals(make_negative(number),-abs(number))
#     number = rnd(-1000,0)
#     Test.assert_equals(make_negative(number),-abs(number))