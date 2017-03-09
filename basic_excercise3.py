class newMethod():

    def __init__(self, number):

        self.number = number
        print(self.number)

    def newnumber(self, number):
        self.number = number
        print(self.number)


# class anothernumber(newMethod):
#
#     def __init__(self):
#         super.__init__(self)

nm = newMethod(2)

nm.newnumber(5)





