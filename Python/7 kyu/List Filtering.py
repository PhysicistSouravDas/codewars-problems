"""
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    '''
    l : a list containing positive numbers and strings
    return a new list with the strings filtered out
    e.g: list = [1, 2, 3, 'abc', 'xyz', 5, 11], then new list, list = [1, 2, 3, 5, 11]
    '''
    newList = []
    for i in l:
        if type(i) == str:
            newList = newList    #doing nothing
        else:
            newList.append(i)
    return newList


# Sample Test
# test.assert_equals(filter_list([1,2,'a','b']),[1,2])
# test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
# test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])
# test.assert_equals(filter_list(['a','b','1']),[])
# test.assert_equals(filter_list([1,2,'a','b']),[1,2])
