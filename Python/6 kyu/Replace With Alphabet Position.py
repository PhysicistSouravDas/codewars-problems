"""
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
Instructions:
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
"""

from string import ascii_lowercase
def alphabet_position(text):
    fltrd_text = ""
    for letter in text.lower():
        if (letter.isalpha()):
            fltrd_text += letter
    ans_val = []
    for letter in fltrd_text:
        ans_val.append(str(ascii_lowercase.index(letter) + 1))
    return " ".join(ans_val)


# Sample Tests
# import string
# import random
# def ap(text):
#         text = text.lower().strip()
#         return " ".join([str(ord(x) - ord("a") + 1) for x in text if x in string.ascii_letters] )

# print("Tests for each letter:")
# for letter in string.ascii_lowercase:
#     test.assert_equals(alphabet_position(letter), ap(letter))
# print("Tests for non-letters:")
# test.assert_equals(alphabet_position("-.-'"), "")

# print("Randomly generated tests:")
# for i in range(100):
#     x = ''.join(random.choice(string.ascii_letters) for _ in range(100))
#     print("Testing \"{0}\":".format(x))
#     test.assert_equals(alphabet_position(x), ap(x))