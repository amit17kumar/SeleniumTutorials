class addTwoLists():
    new_list = []

    def AddNumberByIndex(self,x,y):

        if len(x) >= len(y):
            length = len(y)
            for item in range(0, length):
                list = x[item] + y[item]
                self.new_list.append(list)
        else:
            print("Length of Y is greater then X")

        for num in range(len(y), len(x)):
            self.new_list.append(x[num])

        return self.new_list

x = [1,2,3,4,5,6]
y = [6,7,8,9]

final = addTwoLists()
final_list = final.AddNumberByIndex(x,y)

print(final_list)









