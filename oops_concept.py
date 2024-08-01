class Animal(object):
    def __init__(self):
        print('This is the base class')

    def body(self):
        print('This is the body for Animal')


class pet(object):
    def __init__(self):
        print('This is pet Animal')


class Wild(object):
    def __init__(self):
        print('This is Wild Animal')


class dog(Animal, pet):
    def __init__(self):
        Animal.__init__(self)
        pet.__init__(self)

    def body(self):
        print('This is dog')
        Animal.body(self)


class Tiger(Animal, Wild):
    def __init__(self):
        Animal.__init__(self)
        Wild.__init__(self)

    def body(self):
        print('This is the Tiger')
        Animal.body(self)


if __name__ == '__main__':
    t = Tiger()
