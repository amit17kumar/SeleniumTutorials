class Fruit():

    def __init__(self):
        print("This is the init method of the super class")

    def nutrition(self, fruitname):
        fruits = {'Mango':100, 'Orange': 80, 'Guava': 10}

        if fruitname in fruits:
            print("Nutrition value is the " + fruitname + " is " + str(fruits[fruitname]))

    def fruishape(self,fruitname):
        fruitsshape = {'Mango': 'MangoShape', 'Orange': 'RoundO', 'Guava': 'RoundG'}

        if fruitname in fruitsshape:
            print("Shape of the fruit " + fruitname + " is " + str(fruitsshape[fruitname]))

class Orange(Fruit):

    def __init__(self):
        Fruit.__init__(self)
        print("Init method for Orange class")


    def nutrition(self, fruitname):
        fruits = {'Mango':20, 'Orange': 60, 'Guava': 100}

        if fruitname in fruits:
            print("Nutrition value is the " + fruitname + " is " + str(fruits[fruitname]))

    def colour(self, fruitname):
        fruitcolour = {'Mango':'Yellow', 'Orange': 'Narangi', 'Guava': 'Green'}

        if fruitname in fruitcolour:
            print("Colour of the fruit" + fruitname + " is " + str(fruitcolour[fruitname]))

Fr = Fruit()
Fr.nutrition("Orange")

Or = Orange()

Or.fruishape("Orange")
Or.colour("Orange")
Or.nutrition("Orange")


