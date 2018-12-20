class animal(object):
    def __init__(self):
        print('This is the base class')

    def body(self):
         print ('This is the body for animal')

class pet(object):
    def __init__(self):
        print('This is pet animal')

class wild(object):
    def __init__(self):
        print('This is wild animal')

class dog(animal,pet):
    def __init__(self):
        animal.__init__(self)
        pet.__init__(self)

    def body(self):
        print('This is dog')
        animal.body(self)


class tiger(animal,wild):
    def __init__(self):
        animal.__init__(self)
        wild.__init__(self)

    def body(self):
        print('This is the tiger')
        animal.body(self)


if __name__=='__main__':
      t=tiger()