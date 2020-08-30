"""
https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
Instructions:
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""

def xo(s):
    s = s.lower()
    xs = [i for i in s if i == 'x']
    os = [i for i in s if i == 'o']
    if len(xs) == len(os):
        return True
    return False


# Sample Tests
# Test.expect(xo('xo'), 'True expected')
# Test.expect(xo('XO'), 'True expected')
# Test.expect(xo('xo0'), 'True expected')
# Test.expect(not xo('xxxoo'), 'False expected')

# Test.expect(xo(''),'Empty string contains equal amount of x and o');
# Test.expect(xo('xxxxxoooxooo'), 'True expected');
# Test.expect(xo('xxxxxoooXooo'),'Comparison is case-insensitive');
# Test.expect(xo('abcdefghijklmnopqrstuvwxyz'),'Alphabet contains equal amount of x and o')

# from random import randint, shuffle
# for _ in range(0, 20):
#     x,exp = randint(10,30), False
#     s = list(x*"o" + x*"x" + "AbCdEfGhJkLmNpQrStUvWyZ"[0:x%24])
#     shuffle(s)
#     s = "".join(s)
#     if x%2 :
#         exp = True
#         r = randint(0,5)
#         if r==1 : s = s.replace('x','X')
#         if r==2 : s = s.replace('o','O')
#     else:
#         s = s.replace( 'o', '', 1+randint(0,10) )
#     Test.assert_equals(xo(s),exp)