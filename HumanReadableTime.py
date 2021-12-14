
"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""

# 1 hora = 3600 segs
# 1 min = 60 segs
# Deve haver um jeitinho tricky de fazer...
# Ok, foi mais fácil do que eu esperava =)

def make_readable(seconds):
    hora = 0
    minuto = 0
    segundo = seconds
    while segundo >= 3600:
        hora += 1
        segundo -= 3600

    while segundo >= 60:
        minuto += 1
        segundo -= 60

    return ("{:02d}:{:02d}:{:02d}").format(hora, minuto, segundo)

print(make_readable(0))
