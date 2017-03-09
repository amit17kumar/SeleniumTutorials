# Absolute function

# x = -7
# print(abs(x)) # Output = 7 , it gives distance of the value from 0 in both the direction.

# all() - return true if all the values are ture in an iterable
# any()- return ture if any of the values is true in an iterable

#chr() - Returns the ascii character of the given value

# print(chr(97)) #output a

# x = "abcde"
# print(x)
# dir(x)
# print(dir(x))
#
# x.__getattribute__()

import string

#a= "this is the string to parse"

#x = formatter.parse(a)

#print(x)


# a = (1,2,3,4,5)
#
# b=a[1]
#
# print(b)


a= 10

def test_method():
    global a
    print("Value of a is " + str(a))
    a = 20
    print(a)

test_method()
print(a)



#8*****************************************

a=1
b=2

c = min(a,b)

print(c)






