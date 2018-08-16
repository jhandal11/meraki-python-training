class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @staticmethod
    def make_car_sound():
        print('VRooooommmm!')

    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2


if __name__ == "__main__":

    mustang = Car('Ford', 'Mustang')

    print("Class wheels set to 4")
    print("Mustang   wheels:",mustang.wheels)
    print("Car Class wheels:",Car.wheels)
    print()

    Car.wheels = 6
    print("Class wheels set to 6")
    print("Mustang   wheels:",mustang.wheels)
    print("Car Class wheels:",Car.wheels)
    print()

    mustang.wheels = 5
    print("Mustang wheels set to 5")
    print("Mustang   wheels:",mustang.wheels)
    print("Car Class wheels:",Car.wheels)
    print()

    Car.wheels = 10
    print("Class wheels set to 10")
    print("Mustang   wheels:",mustang.wheels)
    print("Car Class wheels:",Car.wheels)
    print()

    trans_am = Car('Pontiac', 'TransAm')
    print("Mustang   wheels:",mustang.wheels)
    print("TransAm   wheels:",trans_am.wheels)
    print("Car Class wheels:",Car.wheels)
    print()
    
    print(trans_am.make_car_sound())