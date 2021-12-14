"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    new_s = ""
    for char in s:
        if char == char.upper():
            new_s += " "
            new_s += char
        else:
            new_s += char
    return new_s


print(solution("breakCamelCase"))