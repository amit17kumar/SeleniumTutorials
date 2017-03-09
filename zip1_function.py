x = [1, 2, 3, 4]
y = [4, 5, 6]

zipped = [a + b for a, b in zip(x, y)]

print(zipped)


x = 1
y = 2

x,y = y,x

print(x)
print(y)

