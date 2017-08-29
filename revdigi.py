x = 12345
x_string = str(x)                           # "12345"
# uses reversed() directly on the string
x_reversedobject = reversed(x_string)       # <reversed object at 0x009D2D70>
x_reversedlist = list(x_reversedobject)     # ['5', '4', '3', '2', '1']
x_reversedstring = "".join(x_reversedlist)  # "54321"
x_reversed = int(x_reversedstring)          # 54321
print x_reversed
