cars = {'Make': 'Honda', 'Model':'Accord SE', 'Year': '2015'}
#,'Colour':'Blue'

class car():
    def __init__(self):
        print("This is the init method")


    def colorKey(self, colour):
        global cars
        #print(cars['Colour'])
        try:
            print("Colour of the car is " + cars['Colour'])
        except:
            print(colour + " key is not available in the cars")
        finally:
            print("Please try a different key")


ca = car()

ca.colorKey("Colour")









