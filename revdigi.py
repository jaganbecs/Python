x=12345
x_string = str(x)                   
# uses reversed() directly on the string
x_reversedobject = reversed(x_string)
x_reversedlist = list(x_reversedobject)
x_reversedstring = "".join(x_reversedlist)
x_reversed = int(x_reversedstring)
print x_reversed
