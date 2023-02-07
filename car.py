class Car(object):
    def __init__(self, company, colour, model, speedLimit):
        self.company=company
        self.colour=colour
        self.model=model
        self.speedLimit=speedLimit

    def startCar(self):
        print("started")

    def stopCar(self):
        print("car stopped")

    def accelerate(self):
        print("accelerating car")

BMW= Car("BMW","Black", "2a717", "800km/hr")
Lamborghini= Car("Lamborghini","Yellow", "4r618","1000km/hr")

print(BMW.model)
print(Lamborghini.colour)

