"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for
a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""

def find_outlier(integers):

    is_odd = 0
    is_even = 0
    outlier_odd = 0
    outlier_even = 0

    for i in integers:
        if i%2 == 0:
            is_even += 1
            outlier_even += i
        else:
            is_odd +=1
            outlier_odd += i
    if is_even == 1:
        return outlier_even
    else:
        return outlier_odd

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
