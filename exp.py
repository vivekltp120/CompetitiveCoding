
a=8

def func():
    global a;
    a+=2
    print(a)

func()
for i in reversed(range(0,3)):
    print(a)
    print(i)


