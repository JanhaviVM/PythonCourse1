# classes are like blueprints when we want to create something

# we want to create objects with classes

class Vehicle:
    # class can have properties and methods/actions

    # we want to set the make and model for vehicle, using initializer function
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # method, self is referring to itself

    def moves(self):
        print("Moves Along...")

    def get_make_model(self):
        print(f"I'm a {self.make} and {self.model}")


# my_Car is object created from class Vehicle
my_car = Vehicle("Tata", "Model2")

print(my_car.make)
print(my_car.model)
my_car.moves()

my_car.get_make_model()

your_car = Vehicle("Cadillac", "Escalade")

your_car.get_make_model()
your_car.moves()


# classes that depend on vehicle class, inheritance,
# also adding additional properties to innit that is inherited

class Airplane(Vehicle):
    # def __init__(self, make, model, faa_id):
    #     self.make = make
    #     self.model = model
    #     self.faa_id = faa_id
    # above is a longer way to write it, below is simpler way
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    # inheriting parent properties and methods
    pass


cessna = Airplane("Cessna", "Skyhawk", "F-12350")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


# Next we study Polymorphism

# Polymorphism is the ability to behave differently in response to the same input

print("\n\n\n")

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
