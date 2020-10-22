class Car:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def getMaxSpeed(self):
        return self.max_speed

    def getMileage(self):
        return self.mileage

#second class
class Toyota(Car):  #inheritance, penurunan sifat class

    def __init__(self, model=None, color=None):
        self.model = model
        self.color = color

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    @classmethod
    def getOwner(cls):
        print('This is the owner')

toyo = Toyota("camry", "black")
print(toyo.model)
toyo.max_speed = 200
print(toyo.getMaxSpeed())

print(Toyota.getOwner)



