def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 4, 5,7))

def calc(n, **kwargs):
    #for key, value in kwargs.items():
        #print(key)
        #print(value)
        #print(kwargs[add])
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)


calc(2, add = 3, multiply = 5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

my_car = Car(make = 'Nissan', model = 'gtr')

print(my_car.make)