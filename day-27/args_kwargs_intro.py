def add(*args):
    print(args)
    suma = 0
    for n in args:
        suma += n
    print(suma)


add(1, 5, 3, 9, 5, 6)


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # get() - if you dont get this value ten is None = becomes optional (despite of kw["model"])
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
