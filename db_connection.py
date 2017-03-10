import pytest
import string


chars = "Thi is a tongue twister"

list1 = list(string.ascii_lowercase)
final_list ={}
for list in list1:
    count = chars.lower().count(list)
    if count != 0:
        final_list[list] = count
        #print("Comment Updated")

    else:
       continue

print(final_list)
# num =7
#
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)


