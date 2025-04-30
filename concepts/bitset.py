def exp_bit():
    #left shift
    for i in range(4):
        # print('shift {3} -> {4} by {0} - {1} -> {2}'.format(i,a<<i,bin(a<<i),a,bin(a)))
        # print('shift {3} -> {4} by {0} - {1} -> {2}'.format(i,b<<i,bin(b<<i),b,bin(b)))
        print(2<<i)
    print(a^b)


if __name__=='__main__':
    a=0
    b=3
    exp_bit()

