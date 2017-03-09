import string

my_write = open("text",'a')
my_write.write("This is newly added to the file")

my_write.close()

my_read = open("text",'r')
print(my_read.read())

