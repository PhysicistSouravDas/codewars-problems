"""
https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python
Instructions:
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a,b):
    ans = a+b
    result = ""
    while ans!=0:
        result += str(ans%2)
        ans = ans//2
    return result[::-1]


# Sample Tests
# Test.describe("Basic tests")
# Test.assert_equals(add_binary(1,1),"10")
# Test.assert_equals(add_binary(0,1),"1")
# Test.assert_equals(add_binary(1,0),"1")
# Test.assert_equals(add_binary(2,2),"100")
# Test.assert_equals(add_binary(51,12),"111111")
# Test.assert_equals(add_binary(5,9),"1110")
# Test.assert_equals(add_binary(10,10),"10100")
# Test.assert_equals(add_binary(100,100),"11001000")
# Test.assert_equals(add_binary(4096,1),"1000000000001")
# Test.assert_equals(add_binary(0,2174483647),"10000001100110111111110010111111")

# Test.describe("Random tests")
# from random import randint
# sol_binary=lambda a,b: bin(a+b)[2:]

# for _ in range(40):
#     top=10**randint(1,32)
#     a,b=randint(0,top),randint(0,top)
#     Test.it("Testing for "+str(a)+" + "+str(b))
#     Test.assert_equals(add_binary(a,b),sol_binary(a,b),"It should work for random inputs too")