from torch.jit import interface


class Animal():
    #private variable
    __x=None
    #Protected
    _y=8
    def __init__(self):
        print('This is the Animal class')
        self.__x="Siyaram"

    def body(self):
        print('This is the body for Animal')


class Pet():
    def __init__(self):
        print('This is Petpet Animal')


class Wild():
    def __init__(self):
        print('This is Wild Animal')


class Dog(Animal, Pet):
    def __init__(self):
        Animal.__init__(self)
        Pet.__init__(self)

    def body(self):
        print('This is Dog')
        Animal.body(self)


class Tiger(Animal, Wild):
    def __init__(self):
        Animal.__init__(self)
        Wild.__init__(self)

    def body(self):
        print('This is the Tiger body')




if __name__ == '__main__':
    t = Tiger()
    t.body()
