import random
a="hello python"
b=8
print(a,b)
print(random.randrange(1,10))
# multiline strings
s1="""
Hello how are you,
hope you are doing good,
let me know if anything is requitred there
"""
print(s1)

# string slicing
print(a[3:6])
print(a[2:])
print(a[:6])
# string modification
s2="Apple"
print(s2.upper())
print(s2.lower())
print(len(s2))
#formatting the string
print(f"This is your age {b}")
#python boolean
print(3>7)
print(3==8)
print(7<9)
com=67+78j
print(com)
print(type(com))