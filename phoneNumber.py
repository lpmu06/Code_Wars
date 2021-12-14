"""
Write a function that accepts an array of 10 integers (between 0 and 9,
that returns a string of those numbers in the form of a phone number.
Example: create_phone_number([1,2,3,4,5,6,7,8,9,0]) >>> returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses
"""

def cpn(number):  # cpn = create phone number
    if type(number) == int:
        number = str(number)
    phone = ''
    for n in number:
        phone += str(n)
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

print(cpn('1234567890'))
print(cpn([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(cpn(1234567890))
