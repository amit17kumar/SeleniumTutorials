# Find all the prime numbers between 10 and 30

for num in range(10,30):  #to iterate between 10 to 20
    for i in range(2,num): #to iterate on the factors of the number
        if num%i == 0:      #to determine the first factor
            break #to move to the next number, the #first FOR
    else:                  # else part of the loop
        print(num, 'is a prime number')





