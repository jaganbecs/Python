s='abcdef'
x=list(s)
x[::2],x[1::2]=x[1::2],x[::2]
''.join(x)
print(x)
